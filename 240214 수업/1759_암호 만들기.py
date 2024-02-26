import sys
input = sys.stdin.readline

l,c = map(int,input().split())
lst = list(input().split())
visited = [0 for _ in range(c)]
arr = [0 for _ in range(l)]
vowel = ['a','e','i','o','u']
# 정렬 해야 순차적으로 나옴.
lst.sort()
def check(cur):
  ja = 0
  mo = 0
  for i in range(cur):
    if arr[i] in vowel:
      mo += 1
    else:
      ja += 1
    if ja >= 2 and mo >= 1:
      return True
  return False
# 3번 템플릿
def recur(cur,start):
  if cur == l:
    if check(cur):
      print(*arr, sep='')
    return
  for i in range(start,c):
    arr[cur] = lst[i]
    recur(cur+1,i+1)

recur(0,0)