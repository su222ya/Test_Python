# 1. 주석
# python의 주석: 1줄 주석은 => #
# 여러줄 주석은 """ """
"""
여기는 몽땅 주석이에요!
"""


# 2. python의 keyword
#import keyword

# print(keyword.kwlist)
# 어떤 키워드를 사용할 수 있는지 확인해보아요!!


#3. 변수의 생성과 삭제
#my_var= 100
#print(my_var)
#데이터 타입 없이 변수명만 입력하면됨.


#4. 변수를 삭제할 수 있어요!
#del my_var
#print(my_var)


#5. python의 데이터 타입
# python의 built-in data type(이미 정의되있는 데이터 타입)
# -Numeric(숫자)
# -Text Sequence(문자열)
# -Sequence(순서가 있는것)
# -Set
# -Mapping
# -Bool

##########################################################################
# 1. Numeric Data Type(숫자형)
# int(정수)
# float(실수)
# complex(복소수)

# a= 100 #정수
# b=3.141592 #실수
# c=1+2j  #복소수
# d=0o34 #8진수 34 int
# e=0xAB #16진수 int

#데이터 타입을 알고싶어요!
# print(type(a)) #type =>해당 변수에 대한 데이터 타입을 나타냄 class int
# print(type(b)) #class float
# print(type(c)) #class complex

# my_result = 3/4     #0이 아니라 0.75
# print(my_result)
#
# my_result = 10%3    #나머지 연산자
# print(my_result)
#
# my_result = 10//3   #몫 연산자


###################################################################

#2. Text Sequence type(str)

#다른 언어는 문자와 문자열을 구분
#문자는 한글자, 문자열 두글자 이상으로 구성
#문자를 표현할 때 다른 언어는 ''
#문자열을 표현할 때 다른 언어는 ""
#python은 문자열을 표현할 때 ('', "")
# a= "Hello"
# b= "k"
# c= 'python'


# 문자열 연산
# first = "haha"
# second = "hoho"
#
# #print(first+second)  #hahahoho
# print(first+str(10))  #haha10
# print(first*3)  #hahahahahaha


# indexing  (indexing은 지정한 위치에 있는것을 뽑아냄(단순히 요소만 갖고오는거라 그 안의 요소의 타입에 따라 바뀐다))
# my_var = "HELLO"
# print(my_var[-1])  #뒤에서부터 숫자를 셀 때 -를 쓰면된다


# slicing   (slicing은 지정한 범위만큼 잘라내서 리스트 형태로 나온다)
# my_var = "HELLO"
# print(my_var[0:3])   #HEL(0~2까지만 나옴)
# my_var = "이것은소리없는아우성!!"
# print(my_var[0:3])   #이것은
# print(my_var[0:])    #처음부터 끝까지


# in, not in 연산자
# myStr = "This is a sample Text"
# print("sample" in myStr)  #sample이 myStr문자열 안에 있어?
# print("sample" not in myStr)   #sample이 myStr문자열 안에 없니?


# formatting
# num_of_apple = 10
# myStr = "나는 사과를 %d개 가지고 있어요!" % num_of_apple
# print(myStr)

# 문자열 formatting은 아래의 표현을 주로 사용해요!
# num_of_apple = 10
# myStr = "나는 사과를 {}개, 바나나 {}개 가지고 있어요!" .format(num_of_apple,20)
# format이라는 method를 써서 문자열을 나타냄
# print(myStr)


# 문자열 method를 이용하여 문자열 처리를 할 수 있어요!!
# myStr = "cocacola"

# 문자열의 길이를알고 싶으면?
# print(len(myStr))    #len() 함수를 이용, myStr의 길이
#
# print(myStr.count('c'))  #str의 method인 count()를 이용, 문자열에서 c의 개수
#
# print(myStr.find('o'))   #1, 문자열에서 o를 찾아서 처음 발견한 위치를 알려줌
# myStr = "   my Hobby"
# print(myStr.upper())   #소문자를 대문자로
# print(myStr.lower())   #대문자를 소문자로
# print(myStr.strip())   #공백을 날린다

##################################################################################

# 3. Sequence type (list, tuple, range)

# list
# 임의의 객체(데이터)를 순서대로 저장하는 집합 자료형
# C의 array와 유사...
# list는 코드(literal)로 표현할 때 [] (대괄호로 표현)
# my_list = []
# print(type(my_list))
# my_list = list()   #함수를 이용해서 list 만듦
# my_list = [1, 2, 3]
# my_list = [1, 2, 3.14, "Hello", [5, 6, 7],100]  #다양한 타입을 안에 넣을수 있다

# indexing과 slicing을 할 수 있어요!
# print(my_list[1])   #2
# print(my_list[-2])   #[5, 6, 7]  ,indexing은 위치에 있는것을 뽑아냄(단순히 요소만 갖고오는거라 그 안의 요소의 타입에 따라 바뀐다)
# print(my_list[4:5])   #[[5, 6, 7]] ,slicing은 범위만큼 잘라내서 리스트 형태로 나온다
# print(my_list[4][1])   #6
# print(my_list[0:2])   #[1, 2]

# list 연산
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)  #[1, 2, 3, 4, 5, 6]
# print(a * 3)

# a = [1, 2, 3]
# a[0] = [7, 8, 9]
# print(a)   #[[7, 8, 9], 2, 3] , [0]요소에 넣은것 (indexing)
# a[0:1] = [7, 8, 9]
# print(a)    #[7, 8, 9, 2, 3] , 리스트를 리스트로 바꾼것 (slicing)

# a = [1, 2, 3]
# a.append(4)   #리스트의 끝에 마지막 요소로 4를 추가 , [1, 2, 3, 4]
# a.append([5, 6, 7])   #리스트의 끝에 마지막 요소로 [5, 6, 7]를 추가 , [1, 2, 3, [5, 6, 7]]
# print(a)

# my_list = ["홍길동", "아이유", "강감찬", "신사임당"]
# my_list.sort()   # 리스트를 오름차순으로 정렬, sort는 자기자신의 값을 바꾼다(처리한 결과값을 넘기지 않음, return값이 없음)
# print(my_list)

# my_list = ["홍길동", "아이유", "강감찬", "Kin"]
# my_list.sort()   # 리스트를 오름차순으로 정렬, 유니코드 순서라 영어가 한글보다 먼저나옴
# print(my_list)


#  tuple
# list는 []로 표현, tuple은 ()로 표현
# a = (1, 2, 3)    #tuple
# tuple은 일단 만들어지면 내용 변경이 안돼요!!, 원본 데이터 변경을 안되게 하고싶을때 사용
# a[0] = 100   #에러, 값 변경 안됨
# a = (3,)    #요소가 1개만 존재하는 tuple
# a = (1, 2, 3)    #일반적인 Tuple
# a = 1, 2, 3   #tuple 괄호 생략 가능
# print(type(a))
# a = (1, 2, 3)
# b = (5, 6, 7)
# print(a+b)       #(1, 2, 3, 5, 6, 7)

# a = (1, 2, 3)     #튜플을 리스트로 바꾸고 싶을 때
# my_list= list(a)
# print(my_list)

# my_tuple = tuple(my_list)    #리스트를 튜플로 바꾸고 싶을 때
# print(my_tuple)


# range
# 주로 for문에서 사용
# 같은 데이터를 적은 양의 데이터로 표현이 가능 (실제로 값을 다가지고 있는것이 아니라 range(1,100,2) 이렇게 의미를 나타내줌)
# my_range = range(10)   # range(시작, 끝, 증감치) ,range(10) = range(0,10,1)
# print(type(my_range))
# print(my_range)    # range(0, 10)
# print(7 in my_range)  # True
# print(my_range[5])    # 5 ,indexing
# print(my_range[1:4])   # range(1, 4) ,slicing
# print(list(my_range[1:4]))   # [1, 2, 3]
# print(list(my_range))     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

###############################################################

# 4. Mapping( dict )
# dictionary는 key와 value로 데이터를 저장하는 구조
# { }로 표현해요!!
# a = { "name" : "홍길동", "age": 40}   # key=name, value=홍길동
# #print(type(a))
# print(a["name"])
# a["address"] = "서울"   #추가
# print(a)       #{'name': '홍길동', 'age': 40, 'address': '서울'}
# print(a.get("age"))   #get이라는 매서드를 이용해서 값을 가져온다

# dict에서 많이 사용하는 대표적인 method 3개
# a = {'name': '홍길동', 'age': 40, 'address': '서울'}
# print(a.keys())     # a에서 key들만 뽑아라, dict_keys(['name', 'age', 'address'])=>리스트처럼 생겼지만 실제 리스트는 아니다
# print(a.values())
# print(list(a.keys()))   #dict를 list로 바꿈
# print(a.items())    # dict_items([('name', '홍길동'), ('age', 40), ('address', '서울')])
#값을 튜플로 빼내서 리스트 형태로 뽑아냄, 이렇게 해서 뽑아야 값을 for문을 통해 반복해서 처리 가능

# 자료구조를 얼마나 잘 활용하느냐가 중요합니다~!!!!!!!!

###############################################################

# Bool data type => Boolean(True, False)
# 사용하는 연산자 => and, or, not 연산자를 사용할 수 있어요

# 다음의 경우는 Python에서 False로 간주
# 1. 빈 문자열은 False로 간주 => "", ''
# 2. 빈 리스트는 False로 간주 => []
# 3. 빈 tuple도 False로 간주 => ()
# 4. 빈 dict도 False로 간주 => {}
# 5. 숫자 0은 False로 간주
# 6. None은 당연히 False로 간주


# a = 5
# b = 0
#
# print(a and b)    #false
# print(a & b)      # & : bitwise 연산
#                   # 0101 & 0000 => 0000
#
# print(a | b)      # | : bitwise 연산
#                   # 0101 & 0000 => 0101


############################################

# Set data type
# 집합 자료형이고 중복을 허용하지 않아요!
# 순서가 존재하지 않는 자료형

# {} => dict => { "key': "value" }
# {} => set => {1, 2, 3}
# my_set = {1, 2, 3, 4, 1, 2}
#
# print(my_set)     #자동적으로 중복을 제거

# my_list = [1, 2, 3, 4, 1, 2]
# my_set = set(my_list)
# print(my_set)
# # list를 set으로

# my_str = "Hello"
# my_set = set(my_str)
# print(my_set)
# # 문자열을 set으로

# set에서 사용하는 연산자
# 합집합(|), 교집합(&), 차집합(-)

# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# print(s1 | s2)      #union
# print(s1 & s2)      #intersection
# print(s1 - s2)      #difference



#######################################################################


# 추가적으로 날짜관련 사항도 알아보아요!!
# date와 datetime에 대해서 알아보아요!

# from datetime import date, datetime     #date 날짜, datetime 시간
#
# today = date.today()
# print(today)   #2020-07-15
# # 오는 날짜는 : 2020년 07월 15일 입니다.
#
# my_str = "오는 날짜는 : {}년 {}월 {}일 입니다."
# my_str = my_str.format(today.year,today.month,today.day)
# print(my_str)
#
# my_datetime = datetime.today()
# print(my_datetime)
#
# print("현재 시간은 : {}시 입니다.".format(my_datetime.hour))

# 오늘이 07월 15일이에요.
# 내일의 날짜는 07월 16일이에요.     => 이건 쉬움

# 오늘이 01월 31일이에요.
# 내일의 날짜는 02월 01일이에요.    => 그래도 할만함

# 오늘이 03월 01일이에요.
# 내일의 날짜는 02월 28? 29?일이에요.     => 어려움

## 결론은 날짜연산은 처리하기가 너무 힘들어서 계산을 통해 처리하는게 아니라 delta를 이용해서 처리해요!

# from datetime import date, timedelta
#
# today = date.today()        #오늘날짜를 구해요
# days = timedelta(days=30)    #들어가는 숫자만큼 날짜를 계산  ,timedelta는 날짜를 알아서 계산
#
# print(today + days)

# from datetime import date, datetime, timedelta
# today = datetime.today()
# hours = timedelta(hours=-5)    #다섯시간전 시간 구하기
# 
# print(today + hours)

#1달전 날짜를 알아보아요!
# 예) 오늘 날짜가 3월 31일 => 1달전 날짜는?
# 연도와 월에 대한 timedelta는 존재하지 않아요!
# 그래서 새로운 외부 module을 또 사용해야 해요!

# from datetime import date
# from dateutil.relativedelta import relativedelta
# dateutil는 외부 모듈이라 다운로드 받아야함 (setting-> project_폴더명->+클릭->dateutil 검색,설치)

# today = date.today()
# months = relativedelta(months=-1)
#
# print(today + months)

# 현재 날짜와 시간만 하고 있어요!!
# 문자열로 되어있는 날짜를 진짜 날짜로 변환해서 연산을 하고 싶어요!

# from datetime import datetime
# from dateutil.parser import parse
# my_date = parse("2019-01-30")      #문자열일 경우 parse
# print(my_date)
# my_date = datetime(2019,1,30)      #숫자형일경우 datetime
# print(my_date)


#####################################################################################


# python의 data type은 여기까지 정리해보아요!!


















































