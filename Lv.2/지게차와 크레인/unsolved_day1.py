# https://school.programmers.co.kr/learn/courses/30/lessons/388353

# param : storage   - 컨테이너
# param : requests  - 출고 요청

def solution(storage, requests):
    answer = 0

    # 왼쪽, 오른쪽, 위, 아래
    check_list = [(-1, 0), (1, 0), (0, 1), (0,-1)]

    for request in requests:
        for i in range(len(storage)):
            if len(request) == 1:
                storage_list = list(storage[i])

                find_index = [(i, index) for index, char in enumerate(storage_list) if char == request]

                print(find_index)

                # for index in find_index:
                #     for check in check_list:
                #         if 

            elif (len(request)) == 2: # 크레인으로 뽑을 때
                storage[i] = storage[i].replace(''.join(set(request)), '0')
        #     break
        # break

    print(storage)

    return answer

storage = ["AZWQY", "CAABX", "BBDDA", "ACACA"]
requests = ["A", "BB", "A"]
print(solution(storage, requests)) # 11

# storage = ["HAH", "HBH", "HHH", "HAH", "HBH"]
# requests = ["C", "B", "B", "B", "B", "H"]
# print(solution(storage, requests)) # 4