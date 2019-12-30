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
