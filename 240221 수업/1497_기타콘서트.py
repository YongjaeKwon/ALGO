import sys
input = sys.stdin.readline

def check(x,y):
  temp = ''
  for i in range(m):
    if x[i] == 'Y' or y[i] == 'Y':
      temp += 'Y'
    else:
      temp += 'N'
  return temp

def recur(cur, cnt, song):
  global min_, m, target

  if song == target:
    min_ = min(min_,cnt)
    return

  if cnt > min_:
    return

  if cur == n:
    return
  
  guitar, available = lst[cur]
  # print('available',available)
  add_value = check(song,available)

  recur(cur+1, cnt, song)
  recur(cur+1, cnt + 1, add_value)

n, m = map(int,input().split())
lst = [list(input().split()) for _ in range(n)]

arr = [False for _ in range(m)]
ans = [True for _ in range(m)]
answer = -1
min_ = sys.maxsize
target = 'N' * m

for i in range(n):
  temp = ''
  guitar, available = lst[i]
  for j in range(m):
    if target[j] == 'Y' or available[j] == 'Y':
      temp += 'Y'
    else:
      temp += 'N'

  target = temp

if target == 'N' * m:
  print(-1)
  exit()

recur(0,0,'N'*m)
print(min_)