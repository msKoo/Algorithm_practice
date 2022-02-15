########## 입력
print('입력하세요')
n = int(input())
plan = input().split()
########## 


########## 내 답안
# x = 1
# y = 1
# for p in plan:
#   if p == 'l' and x > 1:
#     x -= 1
#   elif p == 'r' and x < n:
#     x += 1
#   elif p == 'u' and y > 1:
#     y -= 1
#   elif p == 'd' and y < n:
#     y += 1

# print(y,x)
########## 


########## 다른 답안
x = 1
y = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types=['l', 'r', 'u', 'd']

for p in plan:
  for i in range(len(move_types)):
    if p == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(x, y)