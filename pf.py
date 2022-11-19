options = ["add expense", "export expenses to Excel", "exit"]

categories = ["Groceries", "Rent", "Clothing", "Entertainment", "Dining out", 
            "Electronics", "Insurance", "Medical expenses", "Taxes", 
            "Transportation", "Utilities"]

    

def main():
    print("What function should be performed? ")
    for i, val in enumerate(options):
        print(i+1, "-", val)
    nselection = int(input(">"))

    for i, val in enumerate(categories):
        print (i+1, "-",val)

    nchoice = int(input("Please choose an expense category? Enter a number. "))
    rchoice = categories[nchoice-1]



if __name__ == "__main__":
    main()