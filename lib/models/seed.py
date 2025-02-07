from models.__init__ import CONN, CURSOR
from models.agent import Agent
from models.sale import Sale

def seed_database():
    Sale.drop_table()
    Agent.drop_table()
    Agent.create_table()
    Sale.create_table()

    # Create seed data
    agent1 = Agent.create("Peter", "M")
    agent2 = Agent.create("Chloe", "F")
    Sale.create(500, "2025-01-01", agent1.id)
    Sale.create(1200, "2025-02-01", agent1.id)
    Sale.create(5000, "2025-02-01", agent1.id)
    Sale.create(1500, "2025-02-01", agent2.id)
    Sale.create(2200, "2025-03-01", agent2.id)


seed_database()
print("Seeded database")