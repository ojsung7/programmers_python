def solution(wallpaper):
    answer = []

    wallpaper = [[j for j in i] for i in wallpaper]

    tmp = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                tmp.append([i, j])

    lux, luy = min(row[0] for row in tmp), min(row[1] for row in tmp)
    rdx, rdy = max(row[0] for row in tmp) + 1, max(row[1] for row in tmp) + 1

    print(lux, luy, rdx, rdy)

    return answer

wallpaper = [".#...", "..#..", "...#."]	
print(solution(wallpaper)) # [0, 1, 3, 4]

wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
print(solution(wallpaper)) # [1, 3, 5, 8]