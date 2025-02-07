from models.__init__ import CONN, CURSOR
from models.agent import Agent
from models.sale import Sale

def seed_database():
    Sale.drop_table()
    Agent.drop_table()
    Agent.create_table()
    Sale.create_table()

    # Create seed data
    peter = Agent.create("Peter", "M")
    chloe = Agent.create("Chloe", "F")
    
    Sale.create(500, "2025-01-01", peter.id)
    Sale.create(1200, "2025-02-01", peter.id)
    Sale.create(5000, "2025-02-01", peter.id)
    Sale.create(1500, "2025-02-01", peter.id)
    Sale.create(2200, "2025-03-01", chloe.id)


seed_database()
print("Seeded database")