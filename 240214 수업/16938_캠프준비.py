import sys
input = sys.stdin.readline

n,l,r,x = map(int,input().split())
arr = list(map(int,input().split()))
min_ = sys.maxsize
max_ = 0

cnt = 0
def check(sum_,min_,max_,length):
  global l,r,x
  if sum_ < l:
    return False
  if sum_ > r:
    return False
  if max_ - min_ < x:
    return False
  if length < 2:
    return False
  return True
def recur(cur,sum_,min_,max_,length):
  global cnt
  if cur == n:
    if check(sum_,min_,max_,length):
      cnt +=1
    return
  # 추가하지 않은 거
  recur(cur+1,sum_,min_,max_,length)
  # 추가한거
  recur(cur+1,sum_ + arr[cur],min(min_,arr[cur]),max(max_,arr[cur]),length+1)

recur(0,0,min_,max_,0)
print(cnt)