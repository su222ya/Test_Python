
# first class
# first-class citizen(1급 시민)

# 프로그램의 구성요소(개체- 값, 객체, 함수)가 다음의 조건을 만족하면
# first-class citizen이라고 불러요!!


# 1. 구성요소가 변수나 데이터 구조의 속성으로 저장될 수 있어요!
# 2. 함수의 인자로 전달될 수 있어요!
# 3. 함수의 결과로 리턴될 수 있어요!

# 아주 쉽게 생각하면
# 우리가 사용하는 일반 숫자 타입의 데이터 => 변수에 저장도 가능하고
# 함수의 인자로 넘겨줄 수 있고 함수의 결과로 리턴될 수 있어요!
# 일반 숫자는 일급시민입니다.

# 우리가 사용하는 객체(class로부터 파생된 instance)
# python에서 사용되는 객체는 1급시민의 조건을 만족해요 => 1급 객체

# python의 함수는 어떻게 될까요??
# 만약 1급시민의 조건을 만족한다면 일급 함수(first class function)라고 불러요!!
# python은 일급함수를 지원하는 언어에요!
# => 함수를 runtime으로 생성할 수 있어요!


# 1. 함수를 변수에 저장할 수 있어요!

# def my_add(x, y):
#     return x+y
#
# print(my_add)
#
# f = my_add       #f는 my_add라는 함수와 주소값이 같다!
# print(f(100,200))

# 2. 함수를 다른 함수의 인자로 전달할 수 있어요!


# def my_add(x,y):
#     return x+y
#
# def my_sub(x,y):
#     return x-y
#
# def my_operation(func, arg_list):       #진짜 일을 하는 함수(func)와 데이터(arg_list)를 둘 다 받는다!
#     result = []
#
#     for (tmp1, tmp2) in arg_list:
#         result.append(func(tmp1, tmp2))
#
#     return result
#
# data = [(1,2), (3,4), (5,6)]
#
# print(my_operation(my_sub,data))

# 3. 함수를 다른 함수의 리턴값으로 사용할 수 있어요!
#     =>closure라는 개념도 같이 이해해야 해요!

# def addMaker():
#
#     def my_add_maker():
#         return 100
#
#     return my_add_maker     #return 100이라는 코드 자체를 리턴해라!
#
# print(addMaker()())       #addMaker()() 함수의 리턴으로 함수를 사용하여서 리턴된 함수를 실행시키기 위해 ()를 또 사용한다!


# tmp1 = 100
#
# def my_func(x):
#
#     tmp2 =300      # 매개변수도 지역변수에요!
#     return x
#
# print(tmp1)    # 100
# my_func(1000)
#
# # print(tmp2)   # XX 함수가 호출되는 시점에 만들어 지고 함수가 리턴되는 시점에 해당 메모리가 날라간다
# print(x)


# def addMaker(x):    # x는 지역변수로 함수가 호출되면 생성되고 종료되면 없어져요!
#
#     def my_add_maker(y):
#         return x + y
#
#     return my_add_maker
#
# add_5 = addMaker(5)
# add_10 = addMaker(10)   #내가 인자를 어떻게 넣느냐에 따라서 필요한 함수를 만들어낼 수 있다!( 동적으로 함수를 만들어낼 수 있다!)
#
# print(add_5(100))
# print(add_10(100))

##########################################################

# Closure  (지역변수 저장공간, 함수가 다른함수를 리턴할 때 작동)
# first class function(일급함수)의 개념을 이용하여
# 스코프에 묶인 변수를 바인딩 하기 위한 기술을 의미해요!   # 예) def addMaker(x)의 지역변수 x를 나중에 사용하기 위한 기술
# 클로저는 데이터를 저장한 레코드에요. 스코프안의 변수가      # x가 저장된 공간을 레코드라 한다
# 소멸되어도 그에 대한 접근을 클로저를 통해서 할 수 있어요!

# 클로저의 도움을 받아 런타임시에 내가 필요한 함수를
# 만들어 낼 수 있어요!!

# def addMaker(x):    # x는 지역변수로 함수가 호출되면 생성되고 종료되면 없어져요!
#
#     def my_add_maker(y):
#         return x + y
#
#     return my_add_maker
#
# add_5 = addMaker(5)       #add_5에 addMaker(5)데이터를 저장한 주소값이 저장된다! 따라서 x값이 소멸되지 않고 접근할 수 있다
# add_10 = addMaker(10)   #내가 인자를 어떻게 넣느냐에 따라서 필요한 함수를 만들어낼 수 있다!( 동적으로 함수를 만들어낼 수 있다!)
#
# print(add_5(100))
# print(add_10(100))










































