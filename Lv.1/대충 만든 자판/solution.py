# https://school.programmers.co.kr/learn/courses/30/lessons/160586

# param : keymap    - 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열
# param : tafgets   - 입력하려는 문자열들이 담긴 문자열 배열

def solution(keymap, targets):
    answer = []

    key_press_count = {}

    # 최소 key 눌리는 횟수 저장
    for key in keymap:
        for press_index, ch in enumerate(key):
            if ch not in key_press_count:
                key_press_count[ch] = press_index + 1
            else:
                key_press_count[ch] = min(key_press_count[ch], press_index + 1)

    for target in targets:
        cnt = 0
        for ch in target:
            if ch in key_press_count:
                cnt += key_press_count[ch]
            else:
                cnt = -1
                break
        answer.append(cnt)

    return answer

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]
print(solution(keymap, targets)) # [9, 4]

keymap = ["AA"]
targets = ["B"]
print(solution(keymap, targets)) # [-1]

keymap = ["AGZ", "BSSS"]
targets = ["ASA","BGZ"]
print(solution(keymap, targets)) # [4, 6]