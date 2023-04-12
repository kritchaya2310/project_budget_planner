import time
import mysql.connector
# connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost", port="3306", user="root", password="", database="budget_planner")
    if conn.is_connected():
        print("Connected successfully to the database.")
    else:
        print("Failed to connect to the database.")

    cursor = conn.cursor()
except Exception as e:
    print("Error connecting to the database:", e)


need_d = {}
want_d = {}
saving = 0
budget = 0


def need_wants():
    print("\n\n***Please enter the list of your needs***")
    print("\n Don't forget to provide the price and priority value")
    print("\n The Priority will be marked on a scale of 0-10, 10 means it has the hightest priority")
    size = int(input("\n\n Enter the number of needs you have = "))
    for i in range(1, size+1):
        print("Enter the need , priority and the cost requried for the need: ")
        need, priority, price = (map(str, input().split()))
        need_d[int(priority)] = [need, int(price)]

    print("\n\n***Please enter the list of your needs***")
    print("\n Don't forget to provide the price and priority value")
    print("\n The Priority will be marked on a scale of 0-10, 10 means it has the hightest priority")
    size = int(input("\n\n Enter the number of needs you have = "))
    for i in range(1, size+1):
        print("Enter the wants:\n")
        need, priority, cost = (map(str, input().split()))
        want_d[int(priority)] = [need, int(cost)]


diff = budget - saving


sorted_need_d = {}
sorted_want_d = {}


def calculation(diff, saving, username):
    spent = 0
    print("\n So as per The given data your Monthly Budget will be as followed :")
    print("\n ::::::::::::YOURS NEED'S LIST::::::::::::")
    print("\n | Name |       | Priority |       | Price | \n")
    for i in sorted_need_d:
        print("\n ", sorted_need_d[i][0], "\t\t",
              i, "\t\t", sorted_need_d[i][1], "\n")
        # insert data into the database
        add_need = ("INSERT INTO budget_planner "
                    "(username, item_type, name, priority, price) "
                    "VALUES (%s, 'need', %s, %s, %s)")
        data_need = (username, sorted_need_d[i][0], i, sorted_need_d[i][1])
        cursor.execute(add_need, data_need)
        conn.commit()

    print("\n ::::::::::::YOURS WANT'S LIST::::::::::::")
    print("\n | Name |       | Priority |       | Price | \n")
    for j in sorted_want_d:
        print("\n ", sorted_want_d[j][0], "\t\t",
              j, "\t\t", sorted_want_d[j][1], "\n")
        # insert data into the database
        add_want = ("INSERT INTO budget_planner "
                    "(username, item_type, name, priority, price) "
                    "VALUES (%s, 'want', %s, %s, %s)")
        data_want = (username, sorted_want_d[j][0], j, sorted_want_d[j][1])
        cursor.execute(add_want, data_want)
        conn.commit()

    for i in sorted_need_d:
        if((diff-sorted_need_d[i][1]) >= 0):
            diff = diff-sorted_need_d[i][1]
            spent = spent+sorted_need_d[i][1]
            print("\n Amount left after fulfilling your ",
                  sorted_need_d[i][0], "need is: ", diff)
        else:
            print(
                "\n So sorry but your "+sorted_need_d[i][0], " need can't be satisfied as it exceeds your Budget")

    for j in sorted_want_d:
        if((diff-sorted_want_d[j][1]) >= 0):
            diff = diff-sorted_want_d[j][1]
            spent = spent+sorted_want_d[j][1]
            print("\n Amount left after fulfilling your ",
                  sorted_want_d[j][0], "want is: ", diff)
        else:
            print(
                "\n So sorry but your "+sorted_want_d[j][0], " need can't be satisfied as it exceeds your Budget")
        # insert data into the database
        add_spending = ("INSERT INTO budget_planner "
                        "(username, diff, saving, spent) "
                        "VALUES (%s, %s, %s, %s)")
        data_spending = (username, diff, saving, spent)
        cursor.execute(add_spending, data_spending)
        conn.commit()


def start():
    s = "\n ***** Welcome to the Monthly Budget Planer *****"
    for i in s:
        print(i, end=" ")
        time.sleep(0.01)
    username = input("\n\n:::::::::::: What is your name? ::::::::::::\n : ")
    budget = float(input("\n\nPlease enter your Monthly budget = "))
    saving = float(input("\nPlease enter the amount you want to save = "))
    diff = budget - saving

    if(saving > budget):
        print("\nYou can't save more than your budget ... Please provide your input again ")
        start()
    need_wants()
    need_k = sorted(need_d.keys(), reverse=True)
    for i in need_k:
        sorted_need_d[i] = need_d[i]
    want_k = sorted(want_d.keys(), reverse=True)
    for i in need_k:
        sorted_need_d[i] = need_d[i]
    for i in want_k:
        sorted_want_d[i] = want_d[i]
    print("\n You have provide all your input")
    print("\n Calculation your finalized Budget")
    calculation(diff, saving, username)


print(start())
