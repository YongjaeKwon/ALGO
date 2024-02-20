import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = [1,2,3]
arr = []
def check(cur,arr):
  for i in range(1,cur//2+1):
    if arr[-i:] == arr[-2*i:-i]:
      return False
  return True

def recur(cur):
  if not check(cur,arr):
    return
  if cur == n:
    temp = ''
    for i in range(n):
      temp += str(arr[i])
    print(int(temp))
    exit()
  for i in lst:
    arr.append(i)
    recur(cur+1)
    arr.pop()

recur(0)