import sys
input = sys.stdin.readline

lst = [list(map(int,list(input().rstrip()))) for _ in range(8)]
print(lst)