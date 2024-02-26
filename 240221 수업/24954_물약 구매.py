import sys
input = sys.stdin.readline

n = int(input())
cost = [0] + list(map(int,input().split()))

discount = [[] for _ in range(n+1)]
for i in range(1,n+1):
  k = int(input())
  for j in range(k):
    discount[i].append(list(map(int,input().split())))

arr = [0 for _ in range(n)]
visited = [False for _ in range(n+1)] 
min_ = sys.maxsize

def check(cost):
  price = 0

  for i in range(n):
    price += cost[arr[i]]
    for j in range(len(discount[arr[i]])):
      cost[discount[arr[i]][j][0]] -= discount[arr[i]][j][1]
      if cost[discount[arr[i]][j][0]] <= 0:
        cost[discount[arr[i]][j][0]] = 1
        
  return price
    

def recur(cur):
  global min_

  if cur == n:
    lst = cost.copy()
    price = check(lst)
    min_ = min(min_,price)
    return

  for i in range(1,n+1):
    if visited[i]:
      continue
    visited[i] = True
    arr[cur] = i
    recur(cur + 1)
    visited[i] = False

recur(0)
print(min_)