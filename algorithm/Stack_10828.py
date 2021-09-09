# https://www.acmicpc.net/problem/10828
import sys
cor = []
command = []
N = int(input())
for i in range (N):
  command.append(sys.stdin.readline())
for cmd in command:
  if 'push' in cmd:
    cor.append(cmd[5:])
  elif 'pop' in cmd:
    print('-1') if len(cor) == 0 else print(cor.pop(), end ='')
  elif 'size' in cmd:
     print(len(cor))
  elif 'empty' in cmd:
    print(1) if len(cor) == 0 else print(0)
  elif 'top' in cmd:
    print(-1) if len(cor) == 0 else print(cor[-1], end='')