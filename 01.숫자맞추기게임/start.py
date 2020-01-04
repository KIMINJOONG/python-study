import random 
import os

def input_check(msg, casting=int):
    while True:
        try: 
            user_input = casting(input(msg))
            return user_input
        except:
            continue

chance = 10
count = 0
number = random.randint(0, 99)
os.system("clear")
print("1부터 99까지의 숫자를 10번안에 맞춰보시오")

while count < chance :
    count += 1
    user_input = input_check("몇 일까요? ")
    if user_input ==  number:
        break
    elif user_input < number:
        print("{} 보다 큰 숫자입니다.".format(user_input))
    elif user_input > number:
        print("{} 보다 작은 숫자입니다.".format(user_input))
    else:
        print("아닙니다.")

if user_input == number:
    print("성공! {} 맞습니다".format(number))
else:
    print("실패! 정답은 {} 입니다.".format(number))