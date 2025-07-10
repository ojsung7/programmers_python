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