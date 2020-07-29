## 문제 14.
## 2**15 = 32768 의 각 자리수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.

## 2**1000의 각 자리수를 모두 더하면 얼마입니까?


# # 1)
# def sum_digit(number):
#     return sum([int(i) for i in str(number)])      # list comprehension
#
# print("결과 : {}".format(sum_digit(2**1000)))

# # 2)
#
# def sum_digit(number):
#     return sum(map(int,str(number)))
# print("결과 : {}".format(sum_digit(2**1000)))




## 문제 16.
## n! 이라는 표기법은 n × (n − 1) × ... × 3 × 2 × 1을 뜻합니다.

## 예를 들자면 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 이 되는데,
## 여기서 10!의 각 자리수를 더해 보면 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 입니다.

## 100! 의 자리수를 모두 더하면 얼마입니까?


def my_multi(num):
    tmp = 1
    my_list = list()
    while num > 0:
        my_list.append(num)
        num -= 1

    for i in range(1, len(my_list) + 1):
        tmp *= i

    return sum([int(j) for j in str(tmp)])


print(" 100!의 결과 : {}".format(my_multi(100)))


#################################################

# my_list = list()
# num=100
# tmp=1
#
# while num > 0:
#     my_list.append(num)
#     num -= 1
# print(len(my_list))
# for i in range(1,len(my_list)+1):
#      tmp *= i
#
# my_sum = sum([int(j) for j in str(tmp)])
# print(my_sum)
#








