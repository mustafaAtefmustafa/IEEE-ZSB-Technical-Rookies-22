def cavityMap(grid):
    # Write your code here
    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            if i == 0 or j == 0 or i == (len(grid[0]) - 1) or j == (len(grid[0]) - 1):
                continue
            else:
                if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
                    grid[i][j] = "X"
                else:
                    continue
    return grid


if __name__ == '__main__':
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    result = cavityMap(grid)
    for row in result:
        print(''.join(map(str, row)))
