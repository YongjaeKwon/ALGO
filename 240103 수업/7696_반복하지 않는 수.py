'''
같은 숫자를 두번 쓰는 것을 못하게 해보자
ex) 11, 22, 33
그리고 n이 0으로 입력되면 프로그램을 종료한다.
'''

def find_number_at_position(position):
    current = 1

    while position > 0:
        current_str = str(current)
        position -= len(set(current_str))

        if position <= 0:
            return int(current_str[len(current_str) + position])

        current += 1

# 25번째 숫자 출력
result = find_number_at_position(25)
print(result)
