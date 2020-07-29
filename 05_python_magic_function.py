
# Magic function

# -1. method의 이름 앞뒤에 더블 언더스코어(__)가 붙어있는
#     method를 지칭해요!
#     대표적인 Magic function => __init__(생성자)
# -2. class안에 정의되어 있는 특수한 형태의 method
# -3. 특수한 상황에서 그에 맞는  Magic function이 호출됩니다!

# class Student(object):
#
#     def __init__(self,name,dept):   #생성자
#         self.name = name
#         self.dept = dept
#         print("{} 학과 {} 학생이 생성되었습니다.".format(self.dept,self.name))
#
#
#     def __del__(self):         #소멸자
#         print("소멸자가 호출되었어요!")
#
# stu1 = Student("홍길동","심리학과")
#
# del stu1             #객체를 메모리에서 삭제해요! __del__ 호출되요!

###################################################

# a= 100
#
# print(type(a))    #class int가 존재해요!

# class MyInt(int):
#     pass
#
# my_num = MyInt(100)
# print(my_num + 200)    # = print(my_num.__add__(200)) , +는 자동적으로 __add__라는 magic function을 호출
# print(my_num.__add__(200))

###################################################

# class Student(object):
#
#     def __init__(self,name,dept):
#         self.name = name
#         self.dept = dept
#         print("{} 학과 {} 학생이 생성되었습니다.".format(self.dept,self.name))
#
#     def __repr__(self):          #출력을 하기 위해 repr이라는 magic function을 오버라이딩해서 이렇게 사용한다
#         return self.name
#
#
# stu1 = Student("홍길동","심리학과")       #stu1은 해당 인스턴스의 주소를 가르킴(reference)
#
# print(stu1)      #instance의 class정보와 저장되어 있는 메모리 주소가 출력

#####################################################

# class Car(object):
#
#     def __init__(self,model,price):
#         self.model = model
#         self.price = price
#
#     def __lt__(self, other):     #내가 새롭게 __li__연산을 재정의!!(오버라이딩)
#                                  # self는 car1, other는 car2
#         if self.price < other.price:
#             return "{} 가격이 더 낮아요!!".format(self.model)
#         else:
#             return "{} 가격이 더 높아요!!".format(self.model)
#
#
# car1 = Car("G70",5000)
# car2 = Car("sonata",3000)
#
#
# print(car1.price < car2.price)   #False
# print(car1 < car2)   #__lt__호출

################################################################


















