# https://school.programmers.co.kr/learn/courses/30/lessons/172928

# param : park      - 공원
# param : routes    - 움직일 값

def index_check(park, s_index, route):
    direction, n = route.split(' ')
    n = int(n)

    w = len(park[0])
    h = len(park)

    if direction == 'N': # 북쪽
        if s_index[0] - n >= 0:
            for i in range(1, n + 1):
                if park[s_index[0] - i][s_index[1]] == 'X':
                    return False
            return True
        
    elif direction == 'S': # 남쪽
        if s_index[0] + n < h:
            for i in range(1, n + 1):
                if park[s_index[0] + i][s_index[1]] == 'X':
                    return False
            return True

    elif direction == 'W': # 서쪽
        if s_index[1] - n >= 0:
            for i in range(1, n + 1):
                if park[s_index[0]][s_index[1] - i] == 'X':
                    return False
            return True
        
    elif direction == 'E':  # 동쪽
        if s_index[1] + n < w:
            for i in range(1, n + 1):
                if park[s_index[0]][s_index[1] + i] == 'X':
                    return False
            return True
        
    return False

def solution(park, routes):
    park = [[j for j in i] for i in park]

    # S의 인덱스 찾기
    for i, row in enumerate(park):
        if 'S' in row:
            s_index = [i, row.index('S')]
            break

    for route in routes:
        if index_check(park, s_index, route):
            direction, n = route.split()
            n = int(n)

            # 이동 처리
            if direction == 'N':
                s_index[0] -= n
            elif direction == 'S':
                s_index[0] += n
            elif direction == 'W':
                s_index[1] -= n
            elif direction == 'E':
                s_index[1] += n

    return s_index