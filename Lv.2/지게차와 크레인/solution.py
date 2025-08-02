# https://school.programmers.co.kr/learn/courses/30/lessons/388353

# param : storage   - 컨테이너
# param : requests  - 선택할 컨테이너

from collections import deque

def use_lift(storage, remove_item):
    n, m = len(storage), len(storage[0])
    visited = [[False] * m for _ in range(n)] # 한번 방문한 것은 다시 조회 하지 않기 위함
    q = deque()

    # 외곽 지점들 큐에 추가
    for r in range(n):
        for c in range(m):
            if r == 0 or r == n - 1 or c == 0 or c == m - 1:
                if not visited[r][c]:
                    if storage[r][c] == remove_item:
                        storage[r][c] = ""
                    elif storage[r][c] == "":
                        q.append((r, c))
                    visited[r][c] = True

    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    # q을 기준으로 상하좌우를 탐색하면서 점점 안쪽으로 조회함
    # visited 값을 통해 한번 탐색한 곳은 탐색하지 않음
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if storage[nr][nc] == "":
                    q.append((nr, nc))
                elif storage[nr][nc] == remove_item:
                    storage[nr][nc] = ""
                visited[nr][nc] = True
    return storage

def use_crane(storage, remove_item):
    n, m = len(storage), len(storage[0])

    for r in range(n):
        for c in range(m):
            if storage[r][c] == remove_item:
                storage[r][c] = ""
    return storage

def solution(storage, requests):
    answer = 0

    storage = [
        list(r)
        for r in storage
    ]

    for request in requests:
        remove_item = request[0]

        if len(request) == 1: # 지게차
            storage = use_lift(storage, remove_item)
        else: # 크레인
            storage = use_crane(storage, remove_item)

    answer = sum(col != '' for row in storage for col in row)

    return answer

storage = ["AZWQY", "CAABX", "BBDDA", "ACACA"]
requests = ["A", "BB", "A"]
print(solution(storage, requests)) # 11

# storage = ["HAH", "HBH", "HHH", "HAH", "HBH"]
# requests = ["C", "B", "B", "B", "B", "H"]
# print(solution(storage, requests)) # 4