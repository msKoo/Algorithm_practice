########## 입력
print('입력하세요')
N, M = map(int, input().split())
########## 

# ########## 내 답안
# cards = [list(map(int, input().split())) for _ in range(N)]

# candis = []

# for i in range(N):
#   candis.append(min(cards[i]))

# print(max(candis))
##########

########## 다른 답안

result = 0

for i in range(N):
  data = list(map(int, input().split()))

  min_value = min(data)

  result=max(result, min_value)

print(result)