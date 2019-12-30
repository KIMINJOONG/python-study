#사용자입력받기

# user = input("사용자 이름을 입력하세요.>")
# print(user)

# num1 = int(input("숫자1"))
# num2 = int(input("숫자2"))
# print(num1 + num2)

# langs = ["한국어", "English"]
# for i, l in enumerate(langs, start=1):
#     print("{}. {}".format(i, l))

# while True:
#     sel = input("언어를 선택하세요.>")
#     if not sel.isnumeric() :
#         continue

#     sel = int(sel)
#     if 0 < sel < 3 :
#         break;
# print("사용자가 선택한 언어는 {} 입니다.".format(langs[sel - 1]))

#입력한 숫자가 소수인지
# while True :
#     num = input("2 이상의 숫자를 입려하세요.>")
#     if not num.isnumeric() :
#         continue
#     num = int(num)
#     if num < 2 :
#         continue
#     break

# isPrime = True
# for n in range(2, num) :
#     if num % 2 == 0 :
#         isPrime = False
#         break

# if isPrime : 
#     print("소수입니다.")
# else :
#     print("소수가 아닙니다.")

while True:
    num = input("2 이상의 숫자를 입려하세요.>")
    if not num.isnumeric() :
        continue
    num = int(num)
    if num < 2 :
        continue
    break

prime_list = [False, False] + [True] * (num - 1)
primes = []

for i in range(2, num + 1) :
    if prime_list[i]:
        for j in range(2 * i, num + 1, i) :
            prime_list[j] = False

primes = [i for i in range(2, num + 1) if prime_list[i] == True]
print(primes)

if num in primes :
    print("소수입니다.")
else :
    print("소수가 아닙니다")
