import sys

testCase = int(sys.stdin.readline())
queue = []
result = []
#출력 list로 받고 한번에 출력하기

for i in range (testCase):
  line = sys.stdin.readline().split()
  if line[0] == 'push':
    queue.append(line[1])
  
  if line[0] == 'pop':
    if len(queue) == 0:
      result.append(-1)
    else:
      result.append(queue.pop(0))
  
  if line[0] == 'size':
    result.append(len(queue))

  if line[0] == 'front':
    if len(queue) == 0:
      result.append(-1)
    else:
      result.append(queue[0])

  if line[0] == 'back':
    if len(queue) == 0:
      result.append(-1)
    else:
      result.append(queue[-1])

  if line[0] == 'empty':
    if len(queue) == 0:
      result.append(1)
    else:
      result.append(0)
  
for i in result:
  print(i)