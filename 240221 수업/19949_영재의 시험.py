import sys
input = sys.stdin.readline

lst = list(map(int,input().split()))

arr = [0 for _ in range(10)]
answer = 0

def check():
  score = 0 
  for i in range(10):
    if arr[i] == lst[i]:
      score += 1

  if score < 5:
    return False

  return True

def is_valid(cnt):
  if arr[cnt-1] == arr[cnt-2] and arr[cnt-1] == arr[cnt-3]:
    return False
  
  return True

def recur(cur, cnt):
  global answer

  if cnt > 2:
    if not is_valid(cnt):
      return

  if cur == 10:
    if check():
      answer += 1
    return

  for i in range(1,6):
    arr[cur] = i
    recur(cur+1, cnt+1)

recur(0,0)
print(answer)