'''
max(a,b,c) - min(a,b,c) 의 절대값
첫째 줄 a,b,c 가 각각 받은 카의 개수 (최대 1000)
2,3,4 줄에는 카드의 종류 (절대값이 최대 1억)
=> 가장 잘 만들 수 있는 점수 (벌점이 가장 작게)

완탐: 1000 * 1000 * 1000 = 10억
모든 카드를 대입해 보면서 최소 점수 갱신


'''
import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
arr_a = list(map(int,input().split()))
arr_b = list(map(int,input().split()))
arr_c = list(map(int,input().split()))