def solution(mats, park):
    answer = 0

    mats_list = []

    for park_list in park:
        print(park_list)

    # for i in range(len(park[0]) - 2):
    #     print(park[0][i:i+3])

    # 윈도우 슬라이싱 방법
    for mat in mats:
        print(f'mat -> {mat}')
        for r_start in range(len(park) - mat):
            for c_start in range(len(park[0]) - mat):
                mats_flag = 0
                for i in range(mat):
                    row_element = []
                    for j in range(mat):
                        row_element.append(park[r_start + i][c_start + j])
                    if row_element.count('-1') == 3:
                        mats_flag +=1
                if mats_flag == mat:
                    mats_list.append(mat)
                    break
    
    answer = max(mats_list)

    return answer

# 채점 결과 런타임 오류 많이 발생함...
mats = [5,3,2]
park = [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]
print(solution(mats, park)) # 3