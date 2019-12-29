# 반복문 while

guest = 1
while guest < 10 :
    guest = guest + 1
    print("손님이 {}명입니다.".format(guest))
    if guest == 10:
        print("손님이 꽉 찼습니다.")

num = 1
jjak = 0
hol = 0
while num <= 10:
    if num % 2 == 0:
        print("짝{}".format(num))
        jjak += num
    else :
        print("홀{}".format(num))
        hol += num
    num = num + 1

print("홀 합 {}".format(hol))
print("짝 합 {}".format(jjak))

num = 1
hap = 0
while num <= 100:
    hap += num
    num += 1
print(hap)