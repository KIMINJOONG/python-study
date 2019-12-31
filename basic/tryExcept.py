try:
    val = "10.5"
    n = int(val)
    
except ValueError as e:
    print("오류 발생 {}".format(e))


try:
    idx = []
    idx[0] = 100
except IndexError as e:
    print("오류 발생 {}".format(e))

try:
    idx = []
    idx[0] = 100
except Exception as e:
    print("오류 발생{}".format(e))


try:
    idx = []
    idx[0] = 100
except:
    pass


print("OK")


try:
    n = "10.5"
    v = int(n)
except:
    print("오류 발생")
else:
    print("정상 동작 확인")


try:
    file = open("sample.txt", "r")
    n = "10.5"
    v = int(n)
except:
    print("오류 발생")
finally:
    file.close()
    print("파이널리 호출")