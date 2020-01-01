# 시간이 남을때 공부해보는 파이썬

- 인프런 남박사의 파이썬 실전100%강의를 보면서 공부중인 프로젝트
- 시간이 있을때마다 하나씩 듣는중입니다.

1. 파이썬은 세미콜론을 쓰지않는다. 물론 붙여도 에러는 나지않는다.

```
result = [num + 5 for num in range(1, 10) if num % 2 == 0]
```

- 위와 같은 구문을 컴프리헨션이라고 한다. 위의 문장을 풀어서 쓰면

```
result = []
for num in range(1, 10):
    if num % 2 == 0:
        result.append(num + 5)
print(result)
```

- 파일 입출력시 with문을 사용하면 자원반납 즉 .close를 명시하지 않아도 된다.

```
with open("./sampleLong.txt", mode="r", encoding="utf-8") as s, open("sample2.txt", mode="w", encoding="utf-8") as t :
```

- 위와 같은 구문에서 코드를 깨끗하게 한다고

```
with open("./sampleLong.txt", mode="r", encoding="utf-8") as s,
open("sample2.txt", mode="w", encoding="utf-8") as t :
```

- 위와같이 한줄을 내려버리면 파이썬은 인식을 하기못하기때문에 다음과 역슬러쉬를 추가해준다.

```
with open("./sampleLong.txt", mode="r", encoding="utf-8") as s, \
open("sample2.txt", mode="w", encoding="utf-8") as t :
```

- 파이썬의 예외처리는 try catch가 아닌 try except이다.

- 함수 매개변수가 아래와같을시

```
    save_winner(*args)
```

- 앞에 아스트릭(\*)이 한개 붙어있으면 매개변수 개수가 정해져있지않고 print를 찍어보면 튜플로 반환하는걸 알수있다.

```
    save_winner2(**args)
```

- 앞에 아스트릭(\*)이 2개 붙어있으면 키와 값을 쌍으로 넘겨주어야한다 ex)

```
    save_winner2(name="홍길동", name2="가가멜")
```

```
    def hi():
        print("hello")
```

- 다음과 같은 변수가 존재시 기존에 호출은 hi()이지만 변수에 담을경우에는 ()생략

```
    hi()
    hello = hi

```
