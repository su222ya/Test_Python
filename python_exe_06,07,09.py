
## 문제 6.
## 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이
## 같은 수를 대칭수(palindrome)라고 부릅니다.

## 두 자리 수를 곱해 만들 수 있는 대칭수 중
## 가장 큰 수는 9009 (= 91 × 99) 입니다.

## 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수를 구하세요
################################################

# a = []
# for i in range(400,1000):
#     for k in range(400,1000):
#         list = str(i*k)
#         for j in range(len(list)):
#             if list[j] != list[-(j+1)]:
#                 break
#         else:
#
#             a.append(int(list))
# print(max(a))



## 문제 7.
## 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

## 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
################################################################

# n=0
#
# while n < 2544:
#     n += 1
#     a = []
#    # print("현재 n의 값은 : {}".format(n))
#     for i in range(1,11):
#         c = n % i
#         a.append(c)        #나머지 값
#    # print(a)
#     if sum(a) == 0:
#         print("나누어 떨어지는 수:{}".format(n))
#         break





## 문제 9.
## 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

## 이 때 10,001번째의 소수를 구하세요.

# num_prime=[2]   #소수 담을 리스트
# n=2
# while True:
#     count = 0
#
#     for i in num_prime:
#         if n % i == 0:
#             count = 1
#             break
#     if count == 0:
#         num_prime.append(n)
#     if len(num_prime) == 10001:
#         break
#     n += 1
#
# print(num_prime[10000])


























