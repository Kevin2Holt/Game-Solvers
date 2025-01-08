import pyautogui
count = 0
def load_grid(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def get_neighbors(x, y, grid):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                # if grid[nx][ny] != '*':
                #     continue
                neighbors.append((nx, ny))
    return neighbors

def find_combinations(grid, x, y, path, visited, combinations):
    if len(path) >= 4:# and len(path) <= 4:
        combinations.add(''.join(path))
        # word = ''.join(path)
        # print(str(len(word))+"\t"+word)
        # pyautogui.typewrite(word)
        # pyautogui.press('enter')
    # if len(path) >= 5:
    #     return
    for nx, ny in get_neighbors(x, y, grid):
        if grid[nx][ny] == '*':
            # print("---")
            continue
        if (nx, ny) not in visited and grid[nx][ny] != '':
            # print(".")
            visited.add((nx, ny))
            find_combinations(grid, nx, ny, path + [grid[nx][ny]], visited, combinations)
            visited.remove((nx, ny))

def generate_combinations(grid):
    combinations = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '*':
                visited = {(i, j)}
                find_combinations(grid, i, j, [grid[i][j]], visited, combinations)
    return sorted(combinations, key=len)

# Load the grid from the file
grid = load_grid('C:/Users/kevin/OneDrive/Desktop/Scripts/input.txt')

for line in grid:
    for char in line:
        if char == '*':
            print('·', end=' ')
        else:
            print(char, end=' ')
    print()
# Generate combinations
combinations = generate_combinations(grid)
count = 0
# Simulate typing each combination
for word in combinations:
    if word == "aphotic":
        continue
    count += 1
    print(str(count) + "\t" + word)
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    # time.sleep(1)