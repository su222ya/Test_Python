

# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.



class Car(object):
    def __init__(self, manufacturer,model,displ,year,cyl,trans,drv,cty,hwy,fl,car_class):
        self.manufacturer = manufacturer
        self.model = model
        self.displ = displ
        self.year = year
        self.cyl = cyl
        self.trans = trans
        self.drv = drv
        self.cty = cty
        self.hwy = hwy
        self.fl = fl
        self.car_class = car_class
      #  self.avg_hwy = round((kor+eng+math)/3,1)      #소수 첫번째자리까지 반올림


#파일 가져오기
file1 = open("C:/python_data_1/mpg.txt","rt",encoding='UTF8')
cars = list()

a = 1
tmp1 = 0
b=1
tmp2=0

while True:
    line = file1.readline()
    if not line:
        break

    car_data = line.split(",")   #list에 담겨서 리턴 ["홍길동","18","7","19"]
    cars.append(Car(car_data[0], car_data[1],float(car_data[2]),car_data[3],car_data[4],car_data[5],
                    car_data[6],car_data[7],float(car_data[8]),car_data[9],car_data[10]))

    if float(car_data[2]) <= 4:
        a += 1
        tmp1 += float(car_data[8])
    elif float(car_data[2]) >= 5:
        b += 1
        tmp2 += float(car_data[8])

if tmp1/a <= tmp2/b:
    print("{}".format(round(tmp2/b,1)))
    print("5 이상인 자동차가 더 높습니다!")
elif tmp1/a >= tmp2/b:
    print("{}".format(round(tmp1/a,1)))
    print("4 이하인 자동차가 더 높습니다!")






# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# 평균적으로 더 높은지 확인하세요.

# class Car(object):
#     def __init__(self, manufacturer,model,displ,year,cyl,trans,drv,cty,hwy,fl,car_class):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.displ = displ
#         self.year = year
#         self.cyl = cyl
#         self.trans = trans
#         self.drv = drv
#         self.cty = cty
#         self.hwy = hwy
#         self.fl = fl
#         self.car_class = car_class
#
#
#
#
# #파일 가져오기
# file1 = open("C:/python_data_1/mpg.txt","rt",encoding='UTF8')
# cars = list()
# a=1
# b=1
# tmp1= 0
# tmp2=0
#
# while True:
#     line = file1.readline()
#     if not line:
#         break
#
#     car_data = line.split(",")   #list에 담겨서 리턴 ["홍길동","18","7","19"]
#     cars.append(Car(car_data[0], car_data[1],float(car_data[2]),car_data[3],car_data[4],car_data[5],
#                     car_data[6],car_data[7],float(car_data[8]),car_data[9],car_data[10]))
#
#     if "audi" in car_data:
#         a += 1
#         tmp1 += float(car_data[7])
#
#     elif "toyota" in car_data:
#         b += 1
#         tmp2 += float(car_data[7])
#
# if tmp1/a <= tmp2/b:
#     print("{}".format(round(tmp2/b,1)))
#     print("toyota 자동차가 더 높습니다!")
# elif tmp1/a >= tmp2/b:
#     print("{}".format(round(tmp1/a,1)))
#     print("audi 자동차가 더 높습니다!")




# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.

# class Car(object):
#     def __init__(self, manufacturer,model,displ,year,cyl,trans,drv,cty,hwy,fl,car_class):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.displ = displ
#         self.year = year
#         self.cyl = cyl
#         self.trans = trans
#         self.drv = drv
#         self.cty = cty
#         self.hwy = hwy
#         self.fl = fl
#         self.car_class = car_class
#       #  self.avg_hwy = round((kor+eng+math)/3,1)      #소수 첫번째자리까지 반올림
#
#
#
# #파일 가져오기
# file1 = open("C:/python_data_1/mpg.txt","rt",encoding='UTF8')
# cars = list()
# a=1
# b=1
# c=1
# tmp1= 0
# tmp2=0
# tmp3 = 0
#
# while True:
#     line = file1.readline()
#     if not line:
#         break
#
#     car_data = line.split(",")   #list에 담겨서 리턴 ["홍길동","18","7","19"]
#     cars.append(Car(car_data[0], car_data[1],float(car_data[2]),car_data[3],car_data[4],car_data[5],
#                     car_data[6],car_data[7],float(car_data[8]),car_data[9],car_data[10]))
#
#     if "chevrolet" in car_data:
#         a += 1
#         tmp1 += float(car_data[8])
#
#     elif "ford" in car_data:
#         b += 1
#         tmp2 += float(car_data[8])
#
#     elif "honda" in car_data:
#         c += 1
#         tmp3 += float(car_data[8])
#
# print("chevrolet 평균 hwy(고속도로 연비) : {}".format(round(tmp1/a,1)))
# print("ford 평균 hwy(고속도로 연비) : {}".format(round(tmp2/b,1)))
# print("honda 평균 hwy(고속도로 연비) : {}".format(round(tmp3/c,1)))


# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.


# class Car(object):
#     def __init__(self, manufacturer,model,displ,year,cyl,trans,drv,cty,hwy,fl,car_class):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.displ = displ
#         self.year = year
#         self.cyl = cyl
#         self.trans = trans
#         self.drv = drv
#         self.cty = cty
#         self.hwy = hwy
#         self.fl = fl
#         self.car_class = car_class
#
#     def __repr__(self):
#         return "manufacturer: {}, model : {} , displ : {}, year : {}, cyl : {}, trans : {}, drv : {}, cty : {}, hwy : {}, fl : {}, car_class : {}"\
#             .format(self.manufacturer, self.model, self.displ, self.year, self.cyl, self.trans, self.drv, self.cty, self.hwy, self.fl, self.car_class)
#
#
#
# #파일 가져오기
# file1 = open("C:/python_data_1/mpg.txt","rt",encoding='UTF8')
# cars = list()
# audi_list=[]
# while True:
#     line = file1.readline()
#     if not line:
#         break
#
#     car_data = line.split(",")   #list에 담겨서 리턴 ["홍길동","18","7","19"]
#     tmp=Car(car_data[0], car_data[1],float(car_data[2]),car_data[3],car_data[4],car_data[5],
#                     car_data[6],car_data[7],float(car_data[8]),car_data[9],car_data[10])
#     cars.append(tmp)
#
#
# for i in cars:
#     if i.manufacturer == "audi":
#         audi_list.append(i)
#
# result= sorted(audi_list, key= lambda car : car.hwy ,reverse=True)   # car.hwy의 값을 car(변수)에 넣고 audi_list값을 내림차순한다.
#
# for k in range(5):
#     print(result[k])






# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다.
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.

class Car(object):
    def __init__(self, manufacturer,model,displ,year,cyl,trans,drv,cty,hwy,fl,car_class):
        self.manufacturer = manufacturer
        self.model = model
        self.displ = displ
        self.year = year
        self.cyl = cyl
        self.trans = trans
        self.drv = drv
        self.cty = cty
        self.hwy = hwy
        self.fl = fl
        self.car_class = car_class

    def __repr__(self):
        return "manufacturer: {}, model : {} , displ : {}, year : {}, cyl : {}, trans : {}, drv : {}, cty : {}, hwy : {}, fl : {}, car_class : {}"\
            .format(self.manufacturer, self.model, self.displ, self.year, self.cyl, self.trans, self.drv, self.cty, self.hwy, self.fl, self.car_class)



#파일 가져오기
file1 = open("C:/python_data_1/mpg.txt","rt",encoding='UTF8')
cars = list()
suv_list= list()
car_name = []
while True:
    line = file1.readline()
    if not line:
        break

    car_data = line.strip().split(",")   #strip(): 공백 없애줌, split(",") : ,별로 나눠줌
    tmp=Car(car_data[0], car_data[1],float(car_data[2]),car_data[3],car_data[4],car_data[5],
                    car_data[6],car_data[7],float(car_data[8]),car_data[9],car_data[10])
    cars.append(tmp)


# 회사이름만 꺼냄
for k in cars:
    car_name.append(k.manufacturer)

car_name = set(car_name)
print(car_name)


# suv 꺼냄
for i in cars:
    if i.car_class == "suv":
        suv_list.append(i)
print(suv_list)












# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.





# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.








# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.



