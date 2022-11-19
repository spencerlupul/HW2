category: str = [[],[1, ' - Groceries'],[2, ' - Rent'],[3, ' - Clothing'],
            [4, ' - Entertainment'],[5, ' - Dining out'],[6, ' - Electronics'],
            [7, ' - Insurance'],[8, ' - Medical Expenses'],[9, ' - Taxes'],
            [10, ' - Transportation'],[11, ' - Groceries']]

categories 1 = ["Groceries", "Rent", "Clothing", "Entertainment", "Dining out", "Electronics"]

class main:
    def __init__(self):
        pass
    def run():
        print(
            'What function should be performed?', '\n',
            '1 - add expense', '\n',
            '2 - export expenses to Excel', '\n',
            '3 - quit', '\n',)
        alpha = input(">")

class expense:
    def __init__(self):
        print(category[1])
        question_1: str = (
            "Which expense category (enter the number) is chosen? ")
        question_2: str = (
            "Please enter  the amount of the expense: ")
        question_3: str = (
            "What is the date of the expense?")
        alpha = input(question_1)
        beta = input(question_2)
        gamma = input(question_3)

run = main.run()

run.main

i=1
x=1
while i < len(category):
    print(category[x]), '\n'
    x = x+1
    if x == len(category):
        break