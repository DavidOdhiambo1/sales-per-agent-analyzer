# Project name: Sales-per-Agent-Analyzer
---
This project allows for the management of agents and their sales. The core functionality includes adding, updating, and deleting agents and sales records, as well as generating reports such as total sales per agent and identifying the agent with the highest sales.



# Features

---

## Agent Management:
    - Create, update, and delete agents.
    - View a list of all agents.
    - Find an agent by name or ID.
## Sales Management:
    - Create, update, and delete sales records.
    - List all sales for a specific agent.
    - View details of individual sales by ID.
## Reporting:
    - Generate total sales per agent report.
    - Identify the agent with the highest sales.

# Requirements
---

- Python 3.x

- SQLite (or any relational database of your choice)


# Installation

***
1. Clone the repository to your local machine:
```bash
git clone https://github.com/DavidOdhiambo1/sales-per-agent-analyzer
```
2. Navigate into the project directory:
```bash
cd sales-per-agent-analyzer
```
3. Install the required Python dependencies:
4. Set up the database (ensure SQLite is set up or configure your own database):
```bash
python lib/seed.py
```
# Usage
---
## Running the CLI
Once the database is set up, you can run the project via the command line to interact with the system:

1. Start the program:

```bash
python lib/cli.py
```
2. You will be prompted with a menu to select different operations:

*Please select an option:*
- Exit the program
- List all agents
- Find agent by name
- Find agent by id
- Create new agent
- Update agent's details
- Delete agent
- List all sales
- Find sale by id
- Create new sale
- Update sale
- Delete sale
- Total sales for an agent
- Total sales per agent report
- Best sales agent

# Contributing
---
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add feature').
5. Push to the branch (git push origin feature-branch).
6. Create a pull request.

# License
---
This project is licensed under the MIT License - see the LICENSE file for details.