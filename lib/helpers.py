from models.agent import Agent
from models.sale import Sale


def exit_program():
    print("Exiting program!")
    exit()


def list_agents():
    agents = Agent.get_all()
    for agent in agents:
        print(agent)


def find_agent_by_name():
    name = input("Enter the agent's name: ")
    agent = Agent.find_by_name(name)
    print(agent) if agent else print(
        f'Agent {name} not found')


def find_agent_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the agent's id: ")
    agent = Agent.find_by_id(id_)
    print(agent) if agent else print(f'Agent {id_} not found')


def create_new_agent():
    name = input("Enter the agent's name: ")
    gender = input("Enter the department's gender: ")
    try:
        agent = Agent.create(name, gender)
        print(f'Success: {agent}')
    except Exception as exc:
        print("Error creating agent: ", exc)


def update_agent():
    id_ = input("Enter the agent's id: ")
    if agent := Agent.find_by_id(id_):
        try:
            name = input("Enter the agent's new name: ")
            agent.name = name
            gender = input("Enter the agent's new gender: ")
            agent.gender = gender

            agent.update()
            print(f'Success: {agent}')
        except Exception as exc:
            print("Error updating agent: ", exc)
    else:
        print(f'Agent {id_} not found')


def delete_agent():
    id_ = input("Enter the agent's id: ")
    if agent := Agent.find_by_id(id_):
        agent.delete()
        print(f'Agent {id_} deleted')
    else:
        print(f'Agent {id_} not found')


def list_sales():
    sales = Sale.get_all()
    for sale in sales:
        print(sale)


def find_sale_by_id():
    id_ = input("Enter the sale's id: ")
    sale = Sale.find_by_id(id_)
    print(sale) if sale else print(f'Sale {id_} not found')


def create_new_sale():
    amount = input("Enter the sale's amount: ")
    date = input("Enter the sale's date: ")
    agent_id = input("Enter the sale's agent id: ")
    try:
        sale = Sale.create(amount, date, agent_id)
        print(f'Success: {sale}')
    except Exception as exc:
        print("Error creating sale: ", exc)


def update_sale():
    id_ = input("Enter the sale's id: ")
    if sale := Sale.find_by_id(id_):
        try:
            amount = input("Enter the sale's new amount: ")
            sale.amount = amount
            date = input("Enter the sale's new date: ")
            sale.date = date
            agent_id = input("Enter the sale's new agent id: ")
            sale.agent_id = agent_id

            sale.update()
            print(f'Success: {sale}')
        except Exception as exc:
            print("Error updating sale: ", exc)
    else:
        print(f'Sale {id_} not found')


def delete_sale():
    id_ = input("Enter the sale's id: ")
    if sale := Sale.find_by_id(id_):
        sale.delete()
        print(f'Sale {id_} deleted')
    else:
        print(f'Sale {id_} not found')



def list_agents_sales():
    id_ = input("Enter the agent's id: ")
    if agent := Agent.find_by_id(id_):
        sales = agent.sales()
        for sale in sales:
            print(sale)
    else:
        print(f'Agent {id_} not found')