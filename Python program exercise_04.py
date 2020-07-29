## 문제 4.
## 로또 프로그램 작성
## 5000원으로 로또복권을 5장 자동으로 구매합니다.
## 이번 주 로또 당첨번호를 생성하여 로또 당첨을 확인하세요!
## 쉬운버전으로 먼저 작성합니다.
## 6숫자가 다 맞으면 1등, 5개 맞으면 2등으로 처리합니다.
## 즉, 쉬운버전은 보너스 숫자는 없는 것으로 간주합니다.
## 쉬운버전을 해결했다면
## 보너스 숫자를 이용하여 로또 당첨을 확인합니다.
## 보너스 숫자를 제외한 모든 숫자가 다 맞으면 1등,
## 보너스 숫자를 포함하여 6개의 숫자가 맞으면 2등,
## 보너스를 제외하고 5개의 숫자가 맞으면 3등으로 처리합니다.

## 쉬운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개,
## 4등 몇개, 꽝 몇개로 출력
## 어려운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개, 
## 4등 몇개, 5등 몇개, 꽝 몇개로 출력

## 랜덤값을 도출하기 위해서는 다음의 코드를 이용한다.
import random

i = random.randint(1, 100)  # 1부터 100 사이의 임의의 정수
f = random.random()  # 0부터 1 사이의 임의의 float
i = random.randrange(1, 101, 2)  # 1부터 100 사이의 임의의 짝수
i = random.randrange(10)  # 0부터 9 사이의 임의의 정수

##### 추가문제
##### 1등에 당첨될려면 평균적으로 얼마만큼의 돈을 투자해야 할까요?
##### 로또 1게임은 1000원입니다.