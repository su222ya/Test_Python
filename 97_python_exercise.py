# 각 사람에 대한 데이터를 읽어서 성적순으로 출력하면 되요! 출력양식은 다음과 같습니다.
#예시)
# 1등 아이유 95.6
# 2등 홍길동 89.3

# class Student(object):
#     def __init__(self,name,grade1,grade2,grade3):
#         self.name = name
#         self.grade1 = grade1
#         self.grade2 = grade2
#         self.grade3 = grade3
#
# file1 = open("C:/python_data/student_score.txt","r")      #파일 가져오기
# my_list= []
# stu_list = []
# while True:
#     line = file1.readline().rstrip()  #file1의 데이터를 라인별로 읽는다
#     if not line:
#         break
#     my_list= line.split(",")
#     stu = Student(my_list[0],my_list[1],my_list[2],my_list[3])
#     stu_list.append(stu)
#
#
#
# print(stu_list[0].name)
#
# file1.close()            #파일 닫기
#


##########################################################################

#풀이)
#class 디자인
class Student(object):
    def __init__(self, name, kor, eng, math):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__math = math
        self.avg = round((kor+eng+math)/3,1)      #소수 첫번째자리까지 반올림

    def __repr__(self):
        return "이름:{} ,수학:{}".format(self.__name,self.avg)


#파일 가져오기
file1 = open("C:/python_data/student_score.txt","r")
students = list()

while True:
    line = file1.readline()  # 홍길동,18,7,19
    if not line:
        break

    stu_data = line.split(",")   #list에 담겨서 리턴 ["홍길동","18","7","19"]
    students.append(Student(stu_data[0],int(stu_data[1]),int(stu_data[2]),int(stu_data[3])))



result = reversed(sorted(students, key = lambda stu : stu.avg))


for tmp in result:
    print(tmp)






# my_list = [10,6,8,3,7,2]
#
# #리스트를 오름차순으로 정렬하고 싶어요
# result = sorted(my_list)





