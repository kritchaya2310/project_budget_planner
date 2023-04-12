
# Project Budger Planner

WORKFLOW:

This project is a budget management program that connects to a MySQL database and performs the following tasks:

1.Import Modules and Connect to the Database:

The code starts by importing the required modules: time and mysql.connector. Then, it tries to connect to the MySQL database with the provided credentials.

2.Check Connection Status:

If the connection is successful, it prints "Connected successfully to the database." Otherwise, it prints "Failed to connect to the database."

3.Initialize Variables:

Next, it defines two empty dictionaries (need_d and want_d) to store the user's needs and wants. It also initializes two variables (saving and budget) to 0.

4.Get User Inputs:

The function need_wants() is called to get the user's needs and wants. It takes input from the user for the name, priority, and price of each need and want and stores them in the dictionaries.

5.Sort Dictionaries:

The dictionaries need_d and want_d are sorted in descending order of priority to get the list of needs and wants in priority order.

6.Calculate Monthly Budget:

The function calculation() is called to calculate the monthly budget. It takes the difference between the budget and the savings and the username as input.

7.Print List of Needs and Wants:

The function prints the list of needs and wants along with their priorities and prices. It also inserts the data into the database.

8.Check Budget Constraints:

For each need and want, the function checks if it can be fulfilled within the available budget. If yes, it deducts the price of the need or want from the available budget and adds it to the spent amount. If not, it prints a message saying that the need or want cannot be fulfilled within the available budget.

9.Insert Data into the Database:

Finally, it inserts the data (difference, saving, and spent) into the database.

10.Start the Program:

The function start() is called to start the program. It takes input from the user for their name, monthly budget, and savings. It also checks if the savings are greater than the budget or not. If yes, it prints a message saying that savings cannot be greater than the budget and prompts the user to enter the input again.

![Logo](https://www.mysql.com/common/logos/logo-mysql-170x115.png)
![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/115px-Python-logo-notext.svg.png?20220821155029)


