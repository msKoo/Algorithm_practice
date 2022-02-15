########## 입력
print('입력하세요')
N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
########## 

########## 내 답안
# nums.sort(reverse=True)

# result = 0
# plus = 0
# count = 0

# while (plus < M):
#   if count == K:
#     count = 0
#     result += nums[1] 
#   else:
#     result += nums[0] 
#   plus += 1 # 더하기 연산 있을 때마다 count + 1
#   count += 1

# print(result)
########## 


########## 다른 답안

nums.sort()
first = nums[N-1]
second = nums[N-2]

count = int(M / (K+1))* K
count += int(M%(K+1)) # 가장 큰 수가 더해지는 횟수

result = 0

result += (count) * first
result += (M - count) * second

print(result)