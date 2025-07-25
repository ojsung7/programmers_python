# https://school.programmers.co.kr/learn/courses/30/lessons/388352

# param : n     - 최대 숫자
# param : q     - 입력한 정수 배열
# param : ans   - 시스템 응답 

from itertools import combinations

# n 값을 통해 후보값을 미리 생성함
def set_candidates(n) -> list:
    return list(combinations([x for x in range(1, n+1)], 5))

# 후보값과 입력받은 정수 배열을 비교해서 몇개가 맞는지 반환
def checked_candidates(c, a):
    cnt = 0
    for i in c:
        if i in a:
            cnt +=1
    return cnt

def solution(n, q, ans):
    answer = 0
    
    candidates = set_candidates(n)

    for c in candidates:
        flag = True
        for a, b in zip(q, ans):
            num = checked_candidates(c, a)
            if num != b: # return 받은 값과 시스템 응답값을 비교해서 맞는지 확인
                flag = False
                break
        if flag:
            answer += 1

    return answer

n = 10
q = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]]
ans = [2, 3, 4, 3, 3]
print(solution(n,q,ans)) # 3

n = 15
q = [2, 3, 4, 3, 3]
ans = [2, 1, 3, 0, 1]
print(solution(n,q,ans)) # 5