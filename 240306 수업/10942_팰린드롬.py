import sys
input = sys.stdin.readline

def recur(cur, total, is_palindrome):
  if cur == e:
    print(is_palindrome)
    return
  
  recur(cur+1, total + arr[cur+1])
  return

n = int(input())
arr = [0] + list(map(int,input().split()))
m = int(input())
for i in range(m):
  s, e = map(int,input().split())
  recur(s,'',1)