 def KeyCheck():
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
if key = "LEFT_KEY":
  #put the page here (the mario page)
  page_number = page_number+1
