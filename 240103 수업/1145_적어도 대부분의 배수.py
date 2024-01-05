'''

'''
import sys
input = sys.stdin.readline

arr = list(map(int,input().split()))

# # 풀이 1
# for i in range(1,100**4):
#   cnt = 0
#   for j in arr:
#     if i % j == 0:
#       cnt += 1
#   if cnt >= 3:
#     print(i)
#     break

# 풀이 2

min_baesu = sys.maxsize
for i in range(5):
  for j in range(i+1,5):
    for k in range(j+1,5):
      arr[i], arr[j], arr[k]
