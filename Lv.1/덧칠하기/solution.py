# https://school.programmers.co.kr/learn/courses/30/lessons/161989

# param : n         - 벽의 길이
# param : m         - 롤러의 길이
# param : section   - 칠해야하는 구역 번호

def solution(n, m, section):
    answer = 0
    i = 0
    
    while i < len(section):
        # 현재 section[i]부터 시작해서 m칸 칠함
        start = section[i]
        end = start + m - 1
        answer += 1
        
        # 롤러가 칠할 수 있는 끝 지점까지 포함된 section들은 건너뜀
        while i < len(section) and section[i] <= end:
            i += 1
    
    return answer

n = 8 
m = 4
section = [2, 3, 6]
print(solution(n, m. section)) # 2

n = 5
m = 4
section = [1, 3]
print(solution(n, m. section)) # 1

n = 4
m = 1
section = [1, 2, 3, 4]
print(solution(n, m. section)) # 4