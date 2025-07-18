# https://school.programmers.co.kr/learn/courses/30/lessons/250121

# param : data      - code, date, maximum, remain 값이 저장되어 있는 배열
# param : ext       - 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열 ["code", "date", "maximum", "remain"] 문자열을 가짐
# param : val_ext   - 뽑아낼 정보의 기준값을 나타내는 정수
# param : sort_by   - 해당하는 값을 기준으로 오름차순으로 정렬 ["code", "date", "maximum", "remain"] 문자열을 가짐

def solution(data, ext, val_ext, sort_by):
    answer = []

    # 문자열을 미리 인덱스로 맵핑함
    ext_mapping = {
        'code':     0,
        'date':     1,
        'maximun':  2,
        'remain':   3
    }

    for i in range(len(data)):
        if data[i][ext_mapping[ext]] < val_ext:
            answer.append(data[i])

    answer = sorted(answer, key=lambda x: x[ext_mapping[sort_by]])

    return answer

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = 'date'
val_ext = 20300501
sort_by = 'remain'
print(solution(data, ext, val_ext, sort_by)) # [[3,20300401,10,8],[1,20300104,100,80]]