import collections

lines = []
with open("input.txt") as f:
    for line in f.read().splitlines():
        lines.append(list(map(int, line)))

print(lines)

width = len(lines[0])
height = len(lines)

def get_val(node):
    return lines[node[1]][node[0]]


def get_length(came_from, node):
    total_dist = get_val(node)
    while node in came_from:
        print(node)

        node = came_from[node]
        total_dist += get_val(node)
    return total_dist


def h(node, goal):
    return (abs(node[0] - goal[0]) + abs(node[1] - goal[1])) * 1.33


def on_grid(node):
    x, y = node
    return x >= 0 and x < width and y >= 0 and y < height


def get_neighbors(node, came_from):
    x, y = node
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    neighbors = list(filter(on_grid, neighbors))
    if node in came_from:
        prev1 = came_from[node]
        neighbors.remove(came_from[node])
        if prev1 in came_from:
            prev2 = came_from[prev1]
            if prev2 in came_from:
                prev3 = came_from[prev2]
                if node[0] == prev1[0] == prev2[0] == prev3[0]:
                    neighbors = [n for n in neighbors if n[0] != node[0]]
                elif node[1] == prev1[1] == prev2[1] == prev3[1]:
                    neighbors = [n for n in neighbors if n[1] != node[1]]
    return neighbors


def a_star(start, goal):
    open = {start}

    came_from = {}
    g_score = collections.defaultdict(lambda: float("inf"))
    g_score[start] = get_val(start)

    f_score = collections.defaultdict(lambda: float("inf"))
    f_score[start] = h(start, goal)

    while open:
        current = min(open, key=lambda x: f_score[x])
        if current == goal:
            return get_length(came_from, goal)
        
        open.remove(current)
        for neighbor in get_neighbors(current, came_from):

            temp_g_score = g_score[current] + get_val(neighbor)
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor, goal)
                

                open.add(neighbor)


length = a_star((0, 0), (width-1, height-1))
print(length)
