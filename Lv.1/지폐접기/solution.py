# https://school.programmers.co.kr/learn/courses/30/lessons/340199

# param : wallet    - 지갑 크기
# param : bill      - 지폐 크기

def solution(wallet, bill):
    answer = 0

    # 지폐가 지갑에 들어가는지 확인
    def check_fit(wallet, bill):
        # 지폐 크기가 지갑 크기에 맞을 때
        if bill[0] <= wallet[0] and bill[1] <= wallet[1] :
            return True
        # 지폐 크기가 지갑 크기에 맞지 않을 때
        else:
            return False

    check_fit_flag = check_fit(wallet, bill)

    while not check_fit_flag:
        bill.reverse() # 지폐 90도 돌리기
        check_fit_flag =  check_fit(wallet, bill)

        if check_fit_flag: # 지폐가 지갑에 들어가면 끝
            pass
        else: # 지폐가 지갑에 들어가지 않으면 긴 쪽 반 접음
            bill = [x // 2 if x == max(bill) else x for x in bill]
            check_fit_flag =  check_fit(wallet, bill)

            answer += 1

    return answer

wallet = [30, 15]	
bill = [26, 17]
print(solution(wallet, bill)) # 1

wallet = [50, 50]
bill = [100, 241]
print(solution(wallet, bill)) # 4