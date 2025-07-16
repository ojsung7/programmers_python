# https://school.programmers.co.kr/learn/courses/30/lessons/250137

# param : bandage(list) - 붕대 [연속 성공 횟수, 초당 회복 체력, 보너스 회복 체력]
# param : health(int)   - 초기 체력
# param : attacks(list) - [[공격한 초, 데미지]]

def solution(bandage, health, attacks):
    asnwer = 0
    max_health = health
    total_time = attacks[-1][0] # 전체 초 시간
    health_success = -1 # 연속 성공
    attacks_index = 0  # 공격(인덱스)

    # 체력 추가하기
    def add_health(max_health, health, addition):
        return health + addition if health + addition <= max_health else max_health

    for time in range(total_time+1):
        # 해당 초에 공격인지 아닌지 판단
        if attacks[attacks_index][0] == time:
            print(f'{time}초 공격o')
            health = health - attacks[attacks_index][1]
            attacks_index += 1
            health_success = 0
        else:
            print(f'{time}초 공격x')
            health_success += 1
            health = add_health(max_health, health, bandage[1])
        print(f'연속 성공 -> {health_success}')
        if health_success == bandage[0]: # 연속으로 성공했다면
            print('추가 목숨')
            health = add_health(max_health, health, bandage[2])
            health_success = 0
        
        print('-'*10)

        if health <= 0:
            health = -1
            break
    
    return health

# bandage, health, attacks = [5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]
# print(solution(bandage, health, attacks)) # 5

bandage, health, attacks = [3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]
print(solution(bandage, health, attacks)) # -1

# bandage, health, attacks = [4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]
# print(solution(bandage, health, attacks)) # -1

# bandage, health, attacks = [1, 1, 1], 5, [[1, 2], [3, 2]]
# print(solution(bandage, health, attacks)) # 3