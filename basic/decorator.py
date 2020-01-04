# def outer_function(msg):
#     def inner_function():
#         return "난 내부함수인데 {}메세지를 받았어".format(msg)
#     return inner_function


# c = outer_function("헬로")

# print(dir(c))
# print(type(c.__closure__))


import time


# def test() :
#     start_time = time.time()
#     for i in range(5):
#         time.sleep(0.1)
#     end_time = time.time() - start_time
#     print("함수 동작 시간 : {}".format(end_time))

def time_checker(func) :
    def inner_function(*args, **kwargs) :
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("함수 {} 동작 시간 : {}".format(func.__name__, end_time-start_time))
        return result
    return inner_function

@time_checker
def test1():
    for i in range(5) :
        time.sleep(0.1)

@time_checker
def test2():
    for i in range(5) :
        time.sleep(0.3)

test1()
test2()

from functools import wraps

def login_required(func):
    @wraps(func)
    def inner_function(*args, **kwargs):
        if not kwargs.get("is_login"):
            print("로그인이 필요합니다.")
            return "로그인이 필요한 페이지입니다."
        return func(*args, **kwargs)
    return inner_function

@login_required
def login():
    print("안녕")

login()


def add_tag(new_args):
    def decorator(func):
        def wrapper(name):
            return "<{}><{}></{}>".format(new_args, func(name), new_args)
        return wrapper
    return decorator

@add_tag("html")
def test(msg):
    return msg

print(test("홍길동"))





