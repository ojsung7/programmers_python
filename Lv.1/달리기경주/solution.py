# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# param : players - 선수 배열
# param : callings - 불리는 선수 배열(앞 사람을 추월함)
def solution(players, callings):
    answer = []
    
    # list로 해서 index를 검색하는 것은 시간복잡도가 너무 큼
    # dict로 해서 key값을 찾는 형식으로 변경
    players_dict = {name: i for i, name in enumerate(players)}
    
    for calling in callings:
        idx = players_dict[calling]
        
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        players_dict[players[idx]] = idx
        players_dict[players[idx-1]] = idx-1
    
    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))#["mumu", "kai", "mine", "soe", "poe"]