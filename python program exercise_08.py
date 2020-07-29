## 문제 8.
## 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다 (제곱의 합).
## 1**2 + 2**2 + ... + 10**2 = 385

## 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
## (1 + 2 + ... + 10)**2 = 552 = 3025

## 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의
## 차이는 3025 - 385 = 2640 이 됩니다.

## 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는
## 얼마입니까?


square_sum = 0
tmp_num = 0
for num in range(1,101):

    tmp_square = num**2
    square_sum += tmp_square

    tmp_num += num

tmp_num_sum = tmp_num**2

print(square_sum)
print(tmp_num_sum)

print("1부터 100까지 자연수에 대해 합의 제곱과 제곱의 합의 차이: {}".format(tmp_num_sum-square_sum))
