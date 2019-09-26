 import tkinter as tk
 #the page that u need to be on
page_number = 1
def KeyCheck():
 while repeat =="go":
    print(page_number)
    #says what page is selected
    global Break_KeyCheck
    Break_KeyCheck = False
     
    while Break_KeyCheck:
     base = getch()
     if base == '\xe0':
      sub = getch()

      if sub == 'H':
       key = 'UP_KEY'
      elif sub == 'M':
       key = 'RIGHT_KEY'
      elif sub == 'P':
       key = 'DOWN_KEY'
      elif sub == 'K':
       key = 'LEFT_KEY'

 Thread(target = KeyCheck).start()
 if key == "LEFT_KEY":
   page_number = page_number-1
   #changes the page number value down one
   repeat = go
   #repeats the code for the arrows with the changed value
 if key == "RIGHT_KEY": 
  page_number = page_number+1
  #changes the page number value up one
  repeat = go
  #repeats the code for the arrows with the changed value
 else:
  #gives an error if you hit a key that is not recognized and goes back to arrows with same value
  print("that is not a recognized control")
  repeat = go
