'''

'''
import sys
input = sys.stdin.readline

def get_gcd(a,b):
  if b == 0:
    return a
  while a%b != 0:
    a,b = b,a%b
  return b
N = int(input())
for i in range(N):
  arr = list(map(int,input().split()))
  max_gcd = 0
  for j in range(len(arr)-1):
    for k in range(j+1,len(arr)):
      max_gcd = max(get_gcd(arr[j],arr[k]), max_gcd)

  print(max_gcd)

