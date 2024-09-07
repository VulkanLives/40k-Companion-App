from tkinter import *
import random

root = Tk()

root.title("Welcome to the dice roller")
root.geometry("700x700")


e = Entry(root, width = 50)
e.grid(row=40, column=20)



def button_click2():
#creating instances of buttons and label and canvas etc
    userInput = e.get() #get user input,will be as string
    amount_of_dice = int(userInput) #convert user string into int
    confirmationClick = Label(root, text= userInput) #display user entry
    confirmationClick.grid(row=25, column=20)
    rollDice(amount_of_dice) #call roll function and pass it number entered by user

def rollDice(amountOfDice):
  totalSum = 0
  possibleFaces = [1,2,3,4,5,6]
  for die in range(amountOfDice):
    roll = random.choice(possibleFaces)
    print("Die ", die + 1, ": ", roll)
    totalSum += roll
  average = totalSum / amountOfDice
  print("Total sum: ", totalSum)
  print("Average roll: ", average)


button2 = Button(root, text= "Roll Dice", command=button_click2) #"command" makes the calls the above function, fg is text colour "foreground" and Bg = background
# print the items from the above into window
button2.grid(row=31, column=20) # same methid for creating this button





root.mainloop()