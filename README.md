# Monthly Budget Planner
This is a simple Monthly Budget Planner program written in Python using MySQL as the database to store the data. The program is designed to take in a user's monthly budget and help them plan their expenses accordingly. The program prompts the user to enter the list of their needs and wants and then calculates the remaining budget after fulfilling those needs and wants. It also saves the data to the MySQL database for future reference.

## Prerequisites
- Python 3.x
- MySQL
## Getting Started
1. Clone the repository to your local machine.
2. Open the budget_planner.py file in a text editor.
3. Replace the host, user, password, and database values in the mysql.connector.connect() function with your own database credentials.
4. Open the terminal or command prompt and navigate to the project directory.
5. Run the following command to install the required packages:
```py
  pip install mysql-connector-python
```
6. Run the following command to start the program:
```py
  python budget_planner.py
```
## How to use the program
1. When you run the program, you will be prompted to enter your name and monthly budget.
2. Next, you will be prompted to enter the list of your needs and wants along with their priority and price.
3. The program will then calculate the remaining budget after fulfilling those needs and wants and save the data to the database.
4. You can view the data in the database by running the following command:
```sql
  SELECT * FROM budget_planner;
```

![Logo](https://www.mysql.com/common/logos/logo-mysql-170x115.png)
![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/115px-Python-logo-notext.svg.png?20220821155029)


