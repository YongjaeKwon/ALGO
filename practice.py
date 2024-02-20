'''
5 3
1 2 1 2 1
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
20 19 18 17 16
15 14 13 12 11
10 9 8 7 6
'''
import sys

N, K = 0, 0
MAX = 6
R = [[0] * MAX for _ in range(MAX)]
M = [[0] * MAX for _ in range(MAX)]
Answer = 0
A = [0]
def input_data():
    global N, K, A
    N, K = map(int, input().split())
    A += list(map(int,input().split()))
    for i in range(1, K + 1):
        R[i][1:N + 1] = map(int, input().split())
    for i in range(1, K + 1):
        M[i][1:N + 1] = map(int, input().split())

def DFS(Day, Rang, Mary):
    global Answer
    if Day == K+1:
        print(Day,Rang,Mary)
        Answer = max(Answer, Rang + Mary)
        return

    for i in range(1, N + 1):
        NewRang = Rang
        NewMary = Mary
        if A[i] > 0:
            A[i] -= 1
            NewRang += R[Day][i]
            for j in range(1, N + 1):
                if A[j] > 0:
                    A[j] -= 1
                    NewMary += M[Day][j]
                    DFS(Day + 1, NewRang, NewMary)
                    NewMary -= M[Day][j]
                    A[j] += 1
            NewRang -= R[Day][i]
            A[i] += 1

def settings():
    DFS(1, 0, 0)

def find_answer():
    print(Answer)

if __name__ == "__main__":
    input_data()
    settings()
    find_answer()