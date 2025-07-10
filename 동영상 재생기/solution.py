# https://school.programmers.co.kr/learn/courses/30/lessons/340213

# param : video_len - 동영상 총 길이
# param : pos       - 현재 동영상 위치
# param : op_start  - 오프닝 시작 구간
# param : op_end    - 오프닝 마지막 구간
# param : commands  - 명령어(next, prev 각 10초 씩)

def solution(video_len, pos, op_start, op_end, commands):
    video_len = int(video_len.split(':')[0]) * 60 + int(video_len.split(':')[1])
    pos = int(pos.split(':')[0]) * 60 + int(pos.split(':')[1])
    op_start = int(op_start.split(':')[0]) * 60 + int(op_start.split(':')[1])
    op_end = int(op_end.split(':')[0]) * 60 + int(op_end.split(':')[1])

    # 오프닝 구간인지 확인
    def check_opening(pos, op_start, op_end):
        if pos >= op_start and pos <= op_end:
            pos = op_end

        return pos

    for command in commands:
        pos = check_opening(pos, op_start, op_end)
        # next 일 경우
        if command == 'next' :
            if video_len - pos < 10:
                pos = video_len
            else:
                pos += 10

        # prev 일 경우
        if command == 'prev' :
            if pos < 10:
                pos = 0
            else:
                pos -= 10
    
    pos = check_opening(pos, op_start, op_end)

    answer = f'{pos//60:02}:{pos%60:02}'
    
    return answer

video_len = "34:33"
pos = "13:00"
op_start = "00:55"
op_end = "02:55"
commands = ["next", "prev"]
print(solution(video_len, pos, op_start, op_end, commands)) # "13:00"

video_len = "10:55"
pos = "00:05"
op_start = "00:15"
op_end = "06:55"
commands = ["prev", "next", "next"]
print(solution(video_len, pos, op_start, op_end, commands)) # "06:55"

video_len = "07:22"
pos = "04:05"
op_start = "00:15"
op_end = "04:07"
commands = ["next"]
print(solution(video_len, pos, op_start, op_end, commands)) # "04:17"