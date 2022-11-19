categories = ["Groceries", "Rent", "Clothing", "Entertainment", "Dining out", 
            "Electronics", "Insurance", "Medical expenses", "Taxes", 
            "Transportation", "Utilities"]



def main():
    for i, val in enumerate(categories):
        print (i+1, "-",val)

    nchoice = int(input("Please choose an expense category? Enter a number. "))
    rchoice = categories[nchoice-1]
    
    



if __name__ == "__main__":
    main()