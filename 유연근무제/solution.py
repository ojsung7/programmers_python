# https://school.programmers.co.kr/learn/courses/30/lessons/388351

# param : schedules - 출근 희망 시각
# param : timelogs  - 실제 출근 시각
# param : startday  - 시작 일자

# 직원들은 매일 한 번씩만 어플로 출근하고, 
# 모든 시각은 시에 100을 곱하고 분을 더한 정수로 표현됩니다. 
# 예를 들어 10시 13분은 1013이 되고 9시 58분은 958이 됩니다.

def solution(schedules, timelogs, startday):

    # days를 정렬
    days = [1, 2, 3, 4, 5, 6, 7]
    days_idx = days.index(startday)

    days = days[days_idx:] + days[:days_idx]

    answer = 0

    # 시간을 분 단위로 변경
    def change_time_pattern(time):
        hour = time // 100
        minute = time % 100

        return hour * 60 + minute
    
    schedules = [change_time_pattern(x) for x in schedules]
    timelogs = [
        [change_time_pattern(x) for x in timelog]
        for timelog in timelogs
    ]

    for idx1, schedule in enumerate(schedules):
        answer_tmp = 0
        for idx2, timelog in enumerate(timelogs[idx1]):
            # 주말(토요일, 일요일)은 출근 체크를 하지 않음
            if days[idx2] in [6, 7]:  # 6 = 토요일, 7 = 일요일
                continue

            # 출근 희망 시각에 10분을 더한 시간까지 도착했으면 정상 출근
            if timelog <= schedule + 10:
                answer_tmp += 1

        if answer_tmp == 5:
            answer += 1

    return answer

schedules = [700, 800, 1100]
timelogs = [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]]
startday = 5
print(solution(schedules, timelogs, startday)) # 3

schedules = [730, 855, 700, 720]
timelogs = [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]]
startday = 1
print(solution(schedules, timelogs, startday)) # 2