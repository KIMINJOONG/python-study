a = "abcdefg"

for i in a :
    print(i)


a = ["python", "java", "c/c++", "c#"]

for i in a :
    print(i)

# 0부터 시작
for i in range(100) :
    print(i)

# ragne시작 범위도 설정가능
for i in range(1, 100) :
    print(i)

for i in range(1, 5 + 1) :
    print(i)


# 1부터 10까지 2씩 찍혀라
for i in range(1, 10, 2) :
    print(i)

a = [(1,2), (3,4), (5,6)]
for i in a:
    for j in i :
        print(j)


a = [[[1,2,3,4,5], ['a', 'b', 'c'], [11, 12, 13, 14]]]
for i in a :
    for j in i:
        for x in j:
            print(x)

student = [{"홍길동": 100}, {"가제트": 200}, {"가가멜": 300}]

for s,i in enumerate(student, start=1):
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("{} 이름: {} 점수: {}".format(s,name, value))


# result = []
# for num in range(1, 6) :
#     result.append(num + 5)

result = [num + 5 for num in range(1, 6)]
print(result)

result = [num + 5 for num in range(1, 10) if num % 2 == 0]
print(result)

result = []
for num in range(1, 10):
    if num % 2 == 0:
        result.append(num + 5)
print(result)

result = [num * 3 for num in range(1, 99) if num % 2 == 0]
print(result)

for i in range(2, 10) :
    for j in range(1, 10):
        result = i * j
        print("{} x {} = {}".format(i, j, result))

gugudan = [ "{} x {} = {}".format(i, j, i*j) for i in range(2, 10) for j in range(1, 10)]
print(gugudan)