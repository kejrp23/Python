"""
Created on 3/26/27
Created for Codeacademy Training exersize.
Written by: Jason R. Pittman
Note: All comments are my own for information purpose and future building ideas.
Note: They reflect my ideas and my ideas alone
This is a calendar program for Command Line. 

The program should behave in the following way:

Print a welcome message to the user
Prompt the user to view, add, update, or delete an event on the calendar
Depending on the user's input: view, add, update, or delete an event on the calendar
The program should never terminate unless the user decides to exit
"""
#This is the main structural requirements for the Calendar
from time import sleep,strftime #save time and import both at once
MY_FIRST_NAME = "Jason" #at some point let the user do this through raw_input()
calendar = {} #dictionaries use values and pairs so we will use Dates and events
#Above here we have the time elements a Consant name to work with and a dictionary
#ok from here on is the Calendar
def welcome():#This is the Splash screen or Welcome area for getting started.
  #This is a possible line for adding a raw_input for the users name
  #MY_FIRST_NAME = raw_input("Lets Get Started\n Please enter your first name: ")
  print "Welcome " + MY_FIRST_NAME + "."
  print "Opening your Calendar one moment please"
  sleep(2)
  print "Today's date is: " + strftime("%A %B %d,%Y") 
  print "the Current time is " + strftime("%I:%M:%S")
  print "What would you like to do? "
#time to set how the calendar runs until exit  
def start_calendar():
  welcome()
  start = True
  #The Calendar is below here
  while start:#keeps the program running unless exited by choice
    user_choice = raw_input('A to add, U to Update, V to View, D to Delete, X to Exit: ')
    user_choice = user_choice.upper()
    
    
    #Adding the Choices they should all be similiar
    if user_choice == 'V':
      if len(calendar.keys()) < 1: # this checks to see if anything is on the calendar by searching the calendar dictionary keys to see if anything is on them
        print "Calendar Empty"
      else:
        print calendar
        
        
        
    # Choice two - update
    elif user_choice == 'U':
      date = int(raw_input('Enter Date (MM/DD/YYYY): '))
      update = raw_input('Enter the update: ')
      #add the inputed changes
      calendar[date] = update
      print 'Calendar Successfully Updated'
      print calendar
      
      
    # Choice three - Add
    elif user_choice == 'A':
      event = raw_input('Enter Event: ')
      date = int(raw_input('Enter Date (MM/DD/YYYY): '))
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):#check the date to make sure it's 10 characters long and to make sure that it isn't older than the current year. (len(date[6:]) splices the date looking for the current year and compares it to the %Y in strftime
      	print 'Invalid Date!' #executes if date isn't long enough or is in the past.
        try_again = raw_input("Try Again? Y for yes, N for No: ")
        try_again.upper()
        if try_again == 'Y':
          continue #Starts the loop over
        else:
          start = False #ends the program if the user doesn't want to continue
      else:
        calendar[date] = event
        print 'Event Added Successfully!'
        print calendar
        continue
    
    
    #the last choice Delete
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print 'Calendar is empty'
        
      else:
        event = raw_input("What Event")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print 'The Event Was Successfully Deleted'
          else:
            print 'No Event was found!'
    
    
    #Time to exit the program        
		elif user_choice == 'X':
      start = False
            
    else:
      print 'That command was not recognized'
      start = False
        

        
        
        
        
        
start_calendar() #launcher for debuggi
