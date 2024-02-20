import sys
from copy import deepcopy
input = sys.stdin.readline

lst = [list(str(input().rstrip())) for _ in range(5)]
dict_alpha = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 
              'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 
              'K': 11, 'L': 12}
dict_num = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
            6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
            11: 'K', 12:'L'}

board = []
answer = []
visited = [False for _ in range(13)]

def check(a):
  if a[0] + a[2] + a[5] + a[7] != 26:
    return False
  if a[7] + a[8] + a[9] + a[10] != 26:
    return False
  if a[0] + a[3] + a[6] + a[10] != 26:
    return False
  if a[1] + a[2] + a[3] + a[4] != 26:
    return False
  if a[1] + a[5] + a[8] + a[11] != 26:
    return False
  if a[4] + a[6] + a[9] + a[11] != 26:
    return False
  return True

def recur(cur):
  global cnt
  board_temp = deepcopy(board)
  if cur == len(lst_dict):
    i = 0
    for j in range(12):
      if board_temp[j] == 'x':
        board_temp[j] = dict_alpha[arr[i]]
        i += 1
    if check(board_temp):
      answer.append(board_temp)
    return
  for i in range(len(lst_dict)):
    if visited[i]:
      continue
    visited[i] = True
    arr[cur] = lst_dict[i]
    recur(cur+1)
    visited[i] = False

for i in range(5):
  for j in range(9):
    if lst[i][j] in dict_alpha:
      board.append(dict_alpha[lst[i][j]])
      del dict_alpha[lst[i][j]]
    if lst[i][j] == 'x':
      board.append('x')

arr = [0 for _ in range(len(dict_alpha))]
lst_dict = list(dict_alpha)
recur(0)
answer.sort()
final = answer[0]
k = 0
final_lst = [['.', '.', '.', '.', 'x', '.', '.', '.', '.'], ['.', 'x', '.', 'x', '.', 'x', '.', 'x', '.'], ['.', '.', 'x', '.', '.', '.', 'x', '.', '.'], ['.', 'x', '.', 'x', '.', 'x', '.', 'x', '.'], ['.', '.', '.', '.', 'x', '.', '.', '.', '.']]
for i in range(5):
  for j in range(9):
    if final_lst[i][j] == 'x':
      final_lst[i][j] = dict_num[final[k]]
      k += 1
for i in range(5):
  print(*final_lst[i])
