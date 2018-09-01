"""Calender to show, add, delete events"""

from time import sleep, strftime

user_name = "JOHN"
calender = {}

def welcome():
  print("Welcome! "+ user_name)
  print("Calender is opening...")
  sleep(1)
  print("Today is: "+strftime("%A %B %d, %Y"))
  print("Time: "+strftime("%H:%M:%S"))
  sleep(1)
  print("What would you like to do?")
  
def start_calender():
  welcome()
  start = True
  while start:
    user_choice = input("Enter 'A' to add 'U to update 'V' to view 'D' to delete and 'X' to exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calender.keys())<1:
        print("Your calender is Empty")
      else:
        print(calender)
    elif user_choice == "U":
      date = input("what date? ")
      update = input("enter the update: ")
      calender[date] = update
      print("Update was successful!")
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[-4:]) < int(strftime("%Y"))):
        print("Enter ageain in MM/DD/YYYY format")
        try_again = input("would you like to try again? Y for yes, N for no: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calender[date] = event
        print("The event was successfully added")
    elif user_choice == "D":
      if len(calender.keys()) < 1:
        print("The calender is already Empty")
      else:
        event = input("What event?")
        for date in calender.keys():
          if calender[date] == event:
            del calender[date]
          else:
            print("Incorrect event was specified")
    elif user_choice == "X":
      start = False
    else:
      print("An invalid command was entered")
      start = False
      
start_calender()
