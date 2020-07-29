
##문제 1.
# idx = 1
# my_sum = 0
# while idx < 1000:
#     if idx % 3 == 0:
#         my_sum += idx
#     elif idx % 5 == 0:
#         my_sum += idx
#
#     idx += 1
#
# print(my_sum)


## 문제 2.
##피보나치 수열의 각 항은 바로 앞의 항 두개를 더한 것입니다.
###짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까

# my_list = [1, 2]
# while my_list[-1] < 4000000:
#     my_var = my_list[-2] + my_list[-1]
#     my_list.append(my_var)
#
# my_list1 = [tmp for tmp in my_list if tmp % 2 == 0]
# a = 0
# for tmp1 in my_list1:
#     a += tmp1
# print(my_list1[-1])
# print(a)




## 문제 3.
##알파벳 대소문자로 된 문자열이 주어지면, 이 문자열에서 가장 많이 사용된 알파벳이 무엇인지 출력하는 프로그램을 작성하시오
##단 대소문자는 구별하디 않아요. 만약 동률이 존재하는 경우 알파벳 순으로 제일 앞에있는 문자를 출력하세요
##문자열) "This is a sample Program mississippi river" =>I
##문자열) "abcdabcdababccddcd" => c

# myStr = "This is a sample Program mississippi river"
#
# num = 0
# alph=[]
# for tmp in myStr:
#     a = 0
#     for tmp1 in myStr:
#          if tmp in tmp1:
#             a += 1
#
#     if num < a:
#         num = a
#         alph = tmp
#     elif num == a:
#         alph = tmp
#
#
#
#
#
# print(num)
# print(alph)















