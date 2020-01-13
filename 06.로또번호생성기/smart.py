import numpy

def make_lotto_number(**kwargs):
    rand_number = numpy.random.choice(range(1,46), 6, replace=False)
    rand_number.sort()

    lotto = []

    if kwargs.get("include"):
        include = kwargs.get("include")
        lotto.extend(include)

        cnt_make = 6 - len(lotto)

        for _ in range(cnt_make):
            for j in range(rand_number):
                if lotto.count(j) == 0:
                    lotto.append(j)
                    break
    else:
        lotto.extend(rand_number)

    if kwargs.get("exclude"):
        exclude = kwargs.get("exclude")
        lotto = list(set(lotto) - set(exclude))

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = numpy.random.choice(range(1,46), 6, replace=False)
                rand_number.sort()

                for j in rand_number:
                    if lotto.count(j) == 0 and j not in exclude:
                        lotto.append(j)
                        break
    
    if kwargs.get("continuty"):
        continuty = kwargs.get("continuty")
        start_number = numpy.random.choice(lotto, 1)

        seq_num = []
        for i in range(start_number[0], start_number[0] + continuty):
            seq_num.append(i)
        seq_num.sort()
        cnt_make = 6 - len(seq_num)
        lotto = []
        lotto.extend(seq_num)

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = numpy.random.choice(range(1,46), 6, replace=False)
                rand_number.sort()
                
                for j in rand_number:
                    if lotto.count(j) == 0 and j not in seq_num:
                        lotto.append(j)
                        break
                
                lotto = list(set(lotto))

    return lotto


count = int(input("로또 번호를 몇개 생성할까요?"))
for j in range(count):
    print(make_lotto_number())



make_lotto_number(include=[1,2,3,4])