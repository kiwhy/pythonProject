##전역변수선언##
coffee = 0
name = []

##함수선언##
def coffe_mach(order, button):
    print()

    print("%s 님의 주문 나옴" %order)
    if button == 1:
        print("아메리카노")
    elif button == 2:
        print("카페라떼")
    elif button == 3:
        print("카푸치노")
    elif button == 4:
        print("에스프레소")
    else:
        print("잘못된 버튼")
    print()

##메인코드##

while True:
    name = str(input("주문자명 입력"))
    coffee = int(input("1.아메리카노 2.카페라떼 3.카푸치노 4.에스프레소"))
    coffe_mach(name, coffee)
    print("커피나옴")