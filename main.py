name = input("What is your name?")
friends = int(input("How many friends?"))
chocolates = int(input("How many chocolates?"))
share = chocolates//friends
remainder = chocolates%friends
print("You will give",share,"chocolates to every friend and you will have",remainder,"left.")