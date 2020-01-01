# def 함수명():
#     print("함수호출")
#     return True

# def add(a, b) :
#     c = a + b
#     return c

# b = add(1,3)
# print(b)

# def get_input_user(msg, casting=int) :
#     while True :
#         try:
#             user = casting(input(msg))
#             return user
#         except:
#             continue

# user = get_input_user("사용자 이름을 입력하세요.>", str)
# age = get_input_user("사용자 나이를 입력하세요.>")

# print(user, age)


# def save_winner(*args):
#     print(args);


# save_winner("홍길동", "김")

# def hi():
#     print("Hello")

# hello = hi

def outer_function(func):
    def inner_function(*args, **kwargs):
        print("함수명: {}".format(func.__name__))
        print("args: {}".format(args))
        print("kwargs: {}".format(kwargs))
        result = func(*args, **kwargs)
        print("result: {}".format(result))
        return result
    return inner_function

def add(a,b) :
    return a + b

f = outer_function(add)

f(10,20)

