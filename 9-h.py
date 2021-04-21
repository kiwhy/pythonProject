##전역변수##
import random

want = 0
num = set()

##함수정의##
def random_numb_gen(ea):
    for i in range(0, ea):
        while len(num) < 6:
            num.add(random.randrange(1,45))
        print(num)
        num.clear()

##메인함수##
want = int(input("뽑을횟수"))
random_numb_gen(want)