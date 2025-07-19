# https://school.programmers.co.kr/learn/courses/30/lessons/389479

# param : players   - 시간 별 사용자 수
# param : m         - 서버 한 대로 이용할 수 있는 최대 사용자 수 
# param : k         - 서버 운영 시간

def solution(players, m, k):
    answer = 0
    active_server = [0] * len(players) # 활성화 된 서버 초기화

    for t in range(len(players)):
        needed = players[t] // m # 해당 시간에 총 필요한 서버 갯수

        current_running = active_server[t] # 현재 활성화 된 서버 갯수

        shortage = needed - current_running
        if  shortage > 0:
            answer += shortage

            for i in range(k): # k 시간 동안 서버 활성화 되어 있는 것을 미리 계산
                if t + i < 24:
                    active_server[t+i] += shortage

    return answer

players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
m = 3
k = 5
print(solution(players, m, k)) # 7

players = [0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0]
m = 5
k = 1
print(solution(players, m, k)) # 11

players = [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
m = 1
k = 1
print(solution(players, m, k)) # 12