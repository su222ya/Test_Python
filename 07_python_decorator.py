
# Decorator
# python에서 Decorator는 기존의 코드에 여러가지 기능을 추가하는
# python구문이라고 이해하면 편해요!

# # Closure
# first class에 대해서 알아보앗어요!
# first class function(일급함수) : 파이썬은 일급함수를 지원하는 언어
# 1. 파이썬의 함수는 변수에 저장할 수 있어요!
# 2. 함수의 인자로 함수를 이용할 수 있어요! ==> Decorator
# 3. 함수의 결과값(리턴값)으로 함수를 이용할 수 있어요! ==> Closure


# def my_outer_func(func):
#     def my_inner_func():
#         func()
#     return my_inner_func       #해당 함수 코드를 리턴하라
#
# def my_func():      #인자로 전달될 함수
#     print("my_func() 함수가 호출되었어요!")
#
# decorated_my_func = my_outer_func(my_func)
#
# decorated_my_func()
# my_func()

#원래의 my_func함수를 수정하지 않고 다른 함수를 이용해서 my_func함수 기능을 확장시키고 싶을때!! ==> Decorator
# import time
# def my_outer_func(func):
#
#     def my_inner_func():
#         print("{} 함수 수행 시간을 계산합니다.".format(func.__name__))
#         start = time.time()     # 1970년 1월1일 0시 0분 0초 - 0(기준값)
#         func()
#         end = time.time()  # start와 end의 차를 이용해 함수의 실행시간을 구할 수있다!
#         print("함수 수행 시간은 {}입니다.".format(start-end))
#
#     return my_inner_func       #해당 함수 코드를 리턴하라, 기존함수에 새로운 기능을 추가해서 새로운 함수를 리턴받으려고 decorator를 사용한다.
#
# @my_outer_func      #my_func 실행할 때 my_outer_func인자에 넣어서 실행하라!
# def my_func():      #인자로 전달될 함수
#     print("my_func() 함수가 호출되었어요!")
#
# my_func()

###################################################################################

# def print_user_name(*args):    #인자로 들어온 사람의 이름을 출력
#  # args는 tuple로 받아요!
#     for name in args:
#         print(name)
#
# # print_user_name("홍길동","신사임당")   # 이렇게도 가능
# print_user_name("홍길동","신사임당","유관순")   # 이렇게도 가능


# def print_user_name(**kwargs):       #인자의 개수와 상관없이 함수를 호출할 수 있다
#  # kwargs는 dict로 받아요!
#     for key in kwargs.keys():
#         print(kwargs.get(key))
#
# print_user_name(name1="홍길동",name2="신사임당")
# print_user_name(name1="홍길동",name2="신사임당")

# Decorator에 대해서 한가지 더 알아보아요!

# def my_outer(func):
#
#     def my_inner(*args,**kwargs):        #모든 형태의 인자를 다 받아들이겠다!!
#         print("데코레이터!! 시작")
#         func(*args,**kwargs)
#         print("데코레이터!! 끝!!")
#     return my_inner
#
# @my_outer
# def my_func():     #함수생성
#     print("이것은 소리없는 아우성!!")
#
# @my_outer
# def my_add(x,y):
#     print("두 수의 합은 : {}".format(x+y))
#
# # my_func()
# my_add(10,20)
#









