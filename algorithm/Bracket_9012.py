import sys

N = int(input())
testData = []
# ())(() : no
for i in range(N):
  testData.append(sys.stdin.readline())

for data in testData:
  trans = []
  left = 0
  right = 0
  if data[0] == ')' or data[-2] == '(':
      print("NO")
  else:
    for i in range(0, len(data)-1):
      if data[i] == '(':
        left += 1
      else :
        right += 1
    if left != right:
      print("NO")
    else:
      print("YES")