import time
def digital_clock():
    for hour in range(24): 
        for minute in range(60): 
            for second in range(60): 
                print(f"{hour:02}:{minute:02}:{second:02}", end="\r") 
                time.sleep(1) 
digital_clock()
