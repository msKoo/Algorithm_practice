########## 입력
print('입력하세요')
Num = int(input())
########## 


########## 내 답안
# 00시 00분 00초 ~ N시 59분 59초

# result = 0
# hour =  [0, 0, 0, 0, 0, 0]
# result_list = []

# for n in range(0, Num+1):
#   hour[0] = n // 10
#   hour[1] = n % 10
#   if hour[0] == 3:
#     result += (3600*10)
#     continue
#   elif hour[1] == 3:
#     result += (3600)
#     continue
#   else:
#     for minute in range(0,60):
#       hour[2] = minute // 10
#       hour[3] = minute % 10
#       if hour[2] == 3 or hour[3] == 3:
#         result += 60
#         continue
#       else:
#         for second in range(0,60):
#           hour[4] = second // 10
#           hour[5] = second % 10
#           if hour[4] == 3 or hour[5] == 3:
#             result += 1
# print(result)

########## 


########## 다른 답안
count = 0

for i in range(Num+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        count += 1

print(count)