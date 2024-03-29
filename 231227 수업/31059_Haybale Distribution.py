'''
예제의 X값들을 전부 입력하니
정답이 하나의 지점으로 고정되는 것이 아닌, 각 a,b에 따라 골라야할 y가 전부 다르다는 것을 알 수 있다.

1. 완전탐색
x의 갯수가 10^6개 이기 떄문에 100만 * 100만의 연산을 해야한다 (시간 초과)

2. 규칙 찾기
a,b 의 크기에 따라서 규칙이 있을거라고 생각하게 됨. (내가 문제를 보고 판단할 수 있는 단서가 이거밖에 없다고 생각함)
a,b 가 같을 경우에는 X를 정렬하고 홀수 일때 가운데, 짝수일때 가운데 두개
a,b 가 서로 다를 때? (여기서부터 문제 발생.)
한쪽이 크면 클수록 멀리 있는 점이 정답이 되는 것 같은 패턴을 보인다. (복수의 곳간이 정답이 될 수 있음.)
(b가 크다면 중앙에서 오른쪽으로 멀어지는 곳간이 답이 되고/ a가 크다면 중앙에서 왼쪽으로 멀어지는 곳간이 답이 된다.)

=> 하지만 우리가 구하고 있는 정답은 곳간의 위치를 찾는 것이 아닌, 최소 비용을 찾는 것이다.

일단 한번 a,b의 대소 비교를 통한 알고리즘 부터 작성한다.
a,b 에 따라서 곳간의 위치를 한칸씩 이동하는 형식으로 해보자. 비용의 최소값이 갱신된다면 계속해서 index를 한칸씩 이동해준다.


3. 2번의 방식 실패.. 하지만 시간을 더 줄여보기 위해 탐색 방법을 달리하자.
=> index의 범위가 생각보다 크기 때문에, 모든걸 탐색해서는 시간초과가 난다.
=> 탐색의 시간을 줄이기 위해서 index의 시작과 끝 지점을 두고, 가운데값과 비교하며 탐색의 횟수를 줄이기로 한다. (이진 탐색)
=> 이진 탐색의 경우 반드시 정렬이 되어있어야 한다. 그러나 값이 중간에 커졌다 작아졌다 커졌다 할 수 있기 때문에 옳지 못한 방법인 것 같다.
=> 조금 보완을 해서 보자...
=> index를 조금 크게 크게 건너 뛰어볼까...
=> 점점 건너 뛰는 양을 줄여가면서 한다
=> change_index에 문제가 있는걸까... 훔.....


Test Case
6
1 8 2 3 6 10
9
1 1
2 2
3 3
1 2
1 3
1 7
7 1
3 1
2 1
'''
import sys
input = sys.stdin.readline

N = int(input())
barn = list(map(int,input().split()))
Q = int(input())

barn.sort()