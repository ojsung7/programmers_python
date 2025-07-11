# https://school.programmers.co.kr/learn/courses/30/lessons/389478

# param : n     - 총 숫자
# param : w     - row 수
# param : num   - 꺼내야하는 상자 번호

def solution(n, w, num):
    # 1. 총 층 수 구하기
    # (1 if n % w != 0 else 0) -> 14 13 나머지가 있기 때문에 n % w 하면 2가 나머지로 나오고 따라서 층이 하나 더 있음
    #      14 13
    # 9 10 11 12
    # 8 7 6 5
    # 1 2 3 4
    total_row = (n//w) + 1
    
    # 2. num의 층 구하기
    # num - 1 하는 이유가 나눴을 때 딱 떨어질 수 있기 때문
    num_row = (num - 1) // w + 1

    # 3. num의 위치 찾기
    if num_row % 2 == 1: # 왼쪽에서 오른쪽으로 쌓일 때
        # num - (num_row*(w-1)) + 1 -> 처음 생각한 코드, 틀렸음
        # (num_row - 1) * w + 1 -> 맨 처음 숫자를 구한 후 num의 위치값을 구함
        # 11을 구할려고 할때 11 - 9 + 1 = 3 으로 계산
        num_position_index = num - ((num_row - 1) * w + 1)
    else: # 오른쪽에서 왼쪽으로 쌓일 때
        num_position_index = (num_row * w) - num

    answer = 0
    
    for current_row in range(num_row, total_row + 1):
        start = (current_row - 1) * w + 1
        end = start + w - 1

        # 해당 열의 숫자를 배열로 집어 넣음
        # 앞에서 계산한 num_position_index 값으로 해당 위치에 모든 층을 검사
        if current_row % 2 == 1: # 왼쪽에서 오른쪽으로 쌓일 때
            num_list = list(range(start, end + 1))
        else: # 오른쪽에서 왼쪽으로 쌓일 때
            num_list = list(range(end, start - 1, -1))

        if num_list[num_position_index] <= n:
            answer += 1

    return answer

n = 22
w = 6
num = 8
print(solution(n, w, num)) # 3

n = 13
w = 3
num = 6
print(solution(n, w, num)) # 4