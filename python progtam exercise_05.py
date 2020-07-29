## 문제 5.
## 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고,
## 이 소수들을 그 수의 소인수라고 합니다.
## 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

## 600851475143의 소인수 중에서 가장 큰 수를 구하세요.

num_prime=[2]   #소수 담을 리스트
n=2
while n < 600851475144:
    count = 0

    for i in num_prime:
        if n % i == 0:
            count = 1
            break
    if count == 0:
        num_prime.append(n)

    n += 1



my_input = 600851475143
result=[]
for tmp in num_prime:
    # count = 0
    while my_input % tmp == 0:
        result.append(tmp)
        my_input = int(my_input // tmp)

        if my_input // tmp == 1:
            break

my_set = set(result)
print(my_set)
print(max(my_set))


