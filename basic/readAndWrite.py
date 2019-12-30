#파이썬에서 파일 읽고 쓰기

# file = open("sample.txt", mode="w")
# file.write("hello python")
# file.close()

# readfile = open("./sample.txt", mode="r")
# content = readfile.read()
# readfile.close()
# print(content)

# file = open("sample.txt", mode="w", encoding="utf-8")
# file.write("안녕 파이썬")
# file.close()

# readfile = open("./sample.txt", mode="r", encoding="utf-8")
# content = readfile.read()
# readfile.close()
# print(content)

# readfile = open("./sampleLong.txt", mode="r", encoding="utf-8")

# for l in readfile:
#     print(l)

# readfile.close()

#close를 사용하지않아줘도 된다.
with open("./sampleLong.txt", mode="r", encoding="utf-8") as file :
    print(file.read())

with open("./sampleLong.txt", mode="r", encoding="utf-8") as s, open("sample2.txt", mode="w", encoding="utf-8") as t :
    t.write(s.read().replace("파이썬", "Python"))