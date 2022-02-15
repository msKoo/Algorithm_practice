########## 입력
print('입력하세요')
n, k = map(int, input().split())
########## 

# ########## 내 답안
# result = 0

# while n != 1:
#   if n % k == 0:
#     n = n/k
#   else:
#     n = n - 1
#   result += 1

# print(result)

##########

########## 다른 답안
result = 0

while True:
  # (N==K로 나누어떨어지는 수 target)가 될 때까지 1씩 빼기
  # target에 도달할때까지 필요한 -1 연산 => result에 더하기
  target = (n//k)*k
  print('target :', target, end=' ')
  result += (n-target)
  print('result + %d-%d => %d'%(n, target, result), end=' ')
  n = target

  if n<k:
    break
  
  result += 1
  n //= k
  print('n :', n)

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)