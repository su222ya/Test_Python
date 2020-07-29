
# python에서 module은 함수나 변수 또는 클래스를 모아놓은 파일을 지칭
# 다른 python파일에서 불러와서 사용할 수 있어요!

# module을 사용하는 이유는 코드의 재사용성과 관리목적

# python모듈은 크게 2가지가 있어요!
# - C언어로 구성된 binary module
# - python언어로 구현된 일반 module

# module을 사용하기 위해서 사용하는 keyword : import
# module도 파이썬 입장에서는 객체로 관리되요!!

# import sys
#
# print(sys.path)       #list
# #
# sys.path.append("c:/python_data")    # module을 저장할 폴더를 지정
# #
# print(sys.path)

# module을 하나 만들어 보아요!!(python 파일을 하나 생성)

# module을 만들었으니 가져다가 사용해보아요!

# import module1
#
# print(module1.my_pi)
# print(module1.my_adder(10,20))
#
#
# import module1 as m1     # mobule1을 m1으로 부르겠다!
#
# print(m1.my_pi)
# print(m1.my_adder(10,20))


# from module1 import my_adder           #이 모듈로부터 my_adder라는 함수를 나는 땡길거야
# print(my_adder(10,20))

# from module1 import *           #이 모듈로부터 그 안에 있는 모든걸 다 땡겨올거야
# print(my_pi)

# c:/python_data안에 module1.py를 저장해 놨어요!
# c:/python_data/test_module/module1.py 로 다시 저장해요!

# import test_module.module1 as my_module
#
# print(my_module.my_pi)




