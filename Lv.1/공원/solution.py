# https://school.programmers.co.kr/learn/courses/30/lessons/340198

# param : mats - 정사각형 돗자라
# param : park - 공원

def solution(mats, park):
    answer = 0
    answer_list = [-1]

    rows = len(park)
    cols = len(park[0])

    for mat in mats:
        windows = []

        # 슬라이딩 윈도우
        for i in range(rows - mat + 1):
            for j in range(cols - mat + 1):
                window = [row[j:j + mat] for row in park[i:i + mat]]
                windows.append(window)

        for window in windows:
            mats_flag = 0
            for i in window:
                if i.count('-1') == mat: # row에 -1 값이 mat 값 만큼 있을 때
                    mats_flag +=1
            if mats_flag == mat: # 총 row 갯수가 mats_flag 값과 같으면 돗자리 필 수 있음
                answer_list.append(mat)
    
    answer = max(answer_list)

    return answer