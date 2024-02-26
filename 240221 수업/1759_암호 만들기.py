import sys
input = sys.stdin.readline

l, c = map(int,input().split())
lst = input().split()

arr = ['' for _ in range(l)]
lst.sort()

def add_value(x):
  if x in 'aeiou':
    return 1,0
  else:
    return 0,1

def recur(cur, cnt, vowel, non_vowel):
  if cnt == l:
    if vowel < 1 or non_vowel < 2:
      return
    
    print(''.join(arr))
    return

  if cur == c:
    return
  
  a, b = add_value(lst[cur])
  arr[cnt] = lst[cur]

  recur(cur+1, cnt+1, vowel + a, non_vowel + b)
  recur(cur+1, cnt, vowel, non_vowel)

recur(0, 0, 0, 0)