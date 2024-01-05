'''
원래 일곱 난쟁이 인데 9명이 있었음
일곱 난쟁이의 키의 합은 100

거짓부렁이 난쟁이를 걸러내고 일곱 난쟁이를 찾자

키는 전부 다르다
복수 정답일 경우 아무거나 출력

정답이 없는 경우는 없다.
'''
import sys
input = sys.stdin.readline

# 9명의 키가 차례대로 주어짐
height =[]
for i in range(9):
  nanjangyi = int(input())
  height.append(nanjangyi)

height.sort()
# 풀이1 7중 for문
# answer = False
# for a in range(3):
#   for b in range(a+1, 4):
#     for c in range(b+1, 5):
#       for d in range(c+1, 6):
#         for e in range(d+1, 7):
#           for f in range(e+1, 8):
#             for g in range(f+1, 9):
#               if height[a] + height[b] + height[c] + height[d] + height[e] + height[f] + height[g] == 100:
#                 print(height[a])
#                 print(height[b])
#                 print(height[c])
#                 print(height[d])
#                 print(height[e])
#                 print(height[f])
#                 print(height[g])
#                 # 답은 1개만 찾으면 되기 때문에 break
#                 answer = True
#                 if answer:
#                   break
#               if answer:
#                   break
#             if answer:
#                   break
#           if answer:
#                   break
#         if answer:
#                   break
#       if answer:
#                   break
#     if answer:
#                   break
#   if answer:
#                   break

# 풀이2 전체를 더해서 2명의 키를 뺏을 때 100
total = sum(height)

def false_nanjangyi():
  for i in range(8):
    for j in range(i + 1, 9):
      if total - height[i] - height[j] == 100:
        return i, j

i, j = false_nanjangyi()

for a in range(len(height)):
  if a != i and a != j:
    print(height[a])
