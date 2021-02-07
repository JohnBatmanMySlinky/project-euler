# grid = [
#     [131, 673, 234, 103,  18],
#     [201,  96, 342, 965, 150],
#     [630, 803, 746, 422, 111],
#     [537, 699, 497, 121, 956],
#     [805, 732, 524,  37, 331]
# ]

import sys
grid = [x.split(',') for x in sys.stdin.read().split('\n')]
for x in range(len(grid)-1):
    for y in range(len(grid)-1):
        grid[x][y] = int(grid[x][y])
grid.pop(len(grid)-1)

# min path sum
# top left --> bottom right
# only right and down

# diagonal matrix traversal was harder than i thought....

x = 0; y = 0
answer = grid.copy()
for idx in range(1,(len(grid)-1)*2+1):
    for x in range(0,len(grid)):
        for y in range(0, len(grid)):
            if x + y - idx == 0:
                if x-1<0:
                    answer[x][y] += answer[x][y-1]
                elif y-1<0:
                    answer[x][y] += answer[x-1][y]
                else:
                    answer[x][y] += min(answer[x-1][y], answer[x][y-1])
            if y > idx: break
        if x > idx: break
print(answer[len(answer)-1][len(answer)-1])

