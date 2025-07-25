# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    answer = []
    
    players_dict = {name: i for i, name in enumerate(players)}
    
    for calling in callings:
        idx = players_dict[calling]
        
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        players_dict[players[idx]] = idx
        players_dict[players[idx-1]] = idx-1
    
    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
allings = ["kai", "kai", "mine", "mine"]
print(solution(players, allings))#["mumu", "kai", "mine", "soe", "poe"]