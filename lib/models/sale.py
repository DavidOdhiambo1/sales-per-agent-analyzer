from models.__init__ import CURSOR, CONN
from models.agent import Agent
from datetime import datetime


class Sale:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, amount, date, agent_id, id=None):
        self.id = id
        self.amount = amount
        self.date = self.validate_date(date)
        self.agent_id = agent_id

    def __repr__(self):
        return (f"<Sale {self.id}: {self.amount}, Agent: {self.agent_id} " )

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, int) and amount>0:
            self._amount = amount
        else:
            raise ValueError("Amount must be a positive integer")

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def department_id(self, agent_id):
        if type(agent_id) is int and Agent.find_by_id(agent_id):
            self._agent_id = agent_id
        else:
            raise ValueError(
                "agent_id must reference an agent in the database")
    
    def validate_date(self, date):
        # Check if date is a string and try to parse it into a datetime object
        if isinstance(date, str):
            try:
                return datetime.strptime(date, "%Y-%m-%d")  # YYYY-MM-DD format
            except ValueError:
                raise ValueError("Date must be in 'YYYY-MM-DD' format")
        elif isinstance(date, datetime):
            return date  # date is already a datetime object
        else:
            raise ValueError("Date must be a string or datetime object")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Sale instances """
        sql = """
            CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            count INTEGER,
            date TEXT,
            agent_id INTEGER,
            FOREIGN KEY (agent_id) REFERENCES agents(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Sale instances """
        sql = """
            DROP TABLE IF EXISTS sales;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the amount and agent id values of the current Sale object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO sales (amount, date, agent_id)
                VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.amount, self.date, self.agent_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Sale instance."""
        sql = """
            UPDATE sales
            SET amount = ?, date = ?, agent_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.amount, self.date,
                             self.agent_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Sale instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM sales
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, amount, date, agent_id):
        """ Initialize a new Sale instance and save the object to the database """
        sale = cls(amount, date, agent_id)
        sale.save()
        return sale

    @classmethod
    def instance_from_db(cls, row):
        """Return a Sale object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        sale = cls.all.get(row[0])
        if sale:
            # ensure attributes match row values in case local instance was modified
            sale.amount = row[1]
            sale.date = row[2]
            sale.agent_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            sale = cls(row[1], row[2], row[3])
            sale.id = row[0]
            cls.all[sale.id] = sale
        return sale
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Sale object per table row"""
        sql = """
            SELECT *
            FROM sales
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Sale object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM sales
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None