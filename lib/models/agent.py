from models.__init__ import CURSOR, CONN

class Agent:

    all = {}

    def __init__(self, name, gender, id=None):
        self.name = name
        self.gender = gender
        self.id = id

    def __repr__(self):
        return f'<Agent {self.id}: {self.name}, gender: {self.gender}>'
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name)>= 2:
            self._name = name
        else:
            raise ValueError(
                "Name must be a string of at least 2 characters"
            )

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        # Ensure the gender is either 'M' or 'F'
        if gender not in ('M', 'F'):
            raise ValueError("Gender must be 'M' (Male) or 'F' (Female)")
        self._gender = gender

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Agent instances """
        sql = """
            CREATE TABLE IF NOT EXISTS agents (
            id INTEGER PRIMARY KEY,
            name TEXT,
            gender TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists agent instances """
        sql = """
            DROP TABLE IF EXISTS agents;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and gender values of the current Agent instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO agents (name, gender)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.gender))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, gender):
        """ Initialize a new Agent instance and save the object to the database """
        agent = cls(name, gender)
        agent.save()
        return agent

    def update(self):
        """Update the table row corresponding to the current Agent instance."""
        sql = """
            UPDATE agents
            SET name = ?, gender = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.gender, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Agent instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM agents
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Agent object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        agent = cls.all.get(row[0])
        if agent:
            # ensure attributes match row values in case local instance was modified
            agent.name = row[1]
            agent.gender = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            agent = cls(row[1], row[2])
            agent.id = row[0]
            cls.all[agent.id] = agent
        return agent

    @classmethod
    def get_all(cls):
        """Return a list containing a Agent object per row in the table"""
        sql = """
            SELECT *
            FROM agents
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Agent object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM agents
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Agent object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM agents
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

  
    def agent_total_sales(self):
        """Return total sales for a particular agent"""
        from models.sale import Sale
        sql = """
            SELECT * FROM sales
            WHERE agent_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        sales_list = [Sale.instance_from_db(row) for row in rows]
        total_sales = sum(sale.amount for sale in sales_list)
        return total_sales
    
    
    def display_total_sales_report():
        """Fetch and display total sales per agent, including agent names."""
        sql = """
            SELECT a.id, a.name, SUM(s.amount) as total_sales
            FROM sales s
            JOIN agents a ON s.agent_id = a.id
            GROUP BY a.id
        """
        try:
            CURSOR.execute(sql)
            rows = CURSOR.fetchall()

            if not rows:
                print("No sales data found.")
                return

            print("Total Sales per Agent Report:")
            print(f"{'Agent ID':<10} {'Agent Name':<20} {'Total Sales'}")
            print("-" * 50)

            # Printing the sales total for each agent 
            for row in rows:
                agent_id, agent_name, total_sales = row
                print(f"{agent_id:<10} {agent_name:<20} {total_sales}")

        except Exception as e:
            print(f"Error generating total sales per agent report: {e}")
    @classmethod
    def get_agent_with_highest_sales(cls):
        """Fetch the agent with the highest total sales."""
        sql = """
            SELECT a.id, a.name, SUM(s.amount) as total_sales
            FROM sales s
            JOIN agents a ON s.agent_id = a.id
            GROUP BY a.id
            ORDER BY total_sales DESC
            LIMIT 1
        """
        try:
            CURSOR.execute(sql)
            row = CURSOR.fetchone()

            if not row:
                print("No sales data found.")
                return None

            agent_id, agent_name, total_sales = row
            # print(f"Agent with the highest sales is: {agent_name} with total sales of {total_sales}")
            # print(f"Agent ID: {agent_id}")
            # print(f"Agent Name: {agent_name}")
            # print(f"Total Sales: {total_sales}")

            return (agent_id, agent_name, total_sales)

        except Exception as e:
            print(f"Error fetching the agent with the highest sales: {e}")
            return None
    
