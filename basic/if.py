# 현재 시간이 12부터 1시이전이면 점심을 먹고 
# 3시부터 4시이거나 아프면 휴식을 하고
# 아니면 일을 한다.

time = 12
sick = True

if 12 <= time < 1 and not sick:
    print("점심먹으러감")
elif 3<= time <= 4 or sick:
    print("휴식 시간")
else:
    print("일하는중..")


name = "abcdef"

if "a" in name:
    print("있음")
else:
    print("없음")



