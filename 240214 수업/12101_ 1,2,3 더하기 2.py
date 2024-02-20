import sys
input = sys.stdin.readline

n, k = map(int,input().split())
lst = [1,2,3]

visited = []
answer = []
temp = []
def check(arr):
  sum_ = sum(arr)
  if sum_ == n:
    return True
  return False

def recur(cur,end):
  global answer
  if cur == end:
    if check(arr):
      answer.append(arr.copy())
    return
  for i in lst:
    arr[cur] = i
    recur(cur+1,end)

for i in range(1,n+1):
  arr = [0 for _ in range(i)]
  recur(0,i)

answer.sort()
length = len(answer)
if k-1 < len(answer):
  str_ = ''
  for i in range(len(answer[k-1])):
    str_ += str(answer[k-1][i])
    str_ += '+'
  print(str_[0:-1])
else:
  print(-1)