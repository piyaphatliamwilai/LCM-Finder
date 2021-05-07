# import

import time

print("Hello, this is LCM checker, made by piyaphatliamwilai")

# debug

debug_mode = input("Do you want debug mode? (Y/N) -> ")

number1 = int(input("Give the first number -> "))
number2 = int(input("Give the second number -> "))

# check thingy

check = number1
check2 = number2

# main

while (check != check2):
    if (check < check2):
        check = check + number1

        if debug_mode == "Y":
            print(check ,"is lower adding ", check, "(", number1, ")")
    
    elif (check2 < check):
        check2 = check2 + number2

        if debug_mode == "Y":
            print(check2 ,"is lower adding", number2, "(", number2, ")")

if (check == check2):
  print(check)
  
 while 3 > 2:
  time.sleep(0.1)
