import sys
input = sys.stdin.readline

n = int(input())

arr = [500,100,50,10,5,1]

money = 1000 - n

cnt = 0
for i in range(len(arr)):
  div, mod = divmod(money,arr[i])
  cnt += div
  money = mod

print(cnt)