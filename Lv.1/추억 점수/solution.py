# https://school.programmers.co.kr/learn/courses/30/lessons/176963

# param : name      - 인물
# param : yearning  - 각 인물의 점수
# photo : photo     - 사진에 찍힌 인물

def solution(name, yearning, photo):
    answer = []
    
    yearning_dict = {i:j for i, j in zip(name, yearning)}
    
    for i in range(len(photo)):
        tmp = 0
        for j in photo[i]:
            if j in yearning_dict: # dict에 key가 있다면 tmp 값에 점수를 추가
                tmp += yearning_dict[j]
        answer.append(tmp)
    
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name, yearning, photo)) # [19, 15, 6]

name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
print(solution(name, yearning, photo)) #[67, 0, 55]

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may"],["kein", "deny", "may"], ["kon", "coni"]]
print(solution(name, yearning, photo)) # [5, 15, 0]