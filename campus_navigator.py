campus = {
    "Hostel": {
        "Cafeteria": 150,
        "Admin Block": 300
    },
    "Cafeteria": {
        "Academic Block": 200
    },
    "Admin Block": {
        "Academic Block": 120
    },
    "Academic Block": {
        "Library": 100
    },
    "Library": {}
}

heuristic = {
    "Hostel": 350,
    "Cafeteria": 260,
    "Admin Block": 150,
    "Academic Block": 90,
    "Library": 0
}


def get_h(path):
    node = path[-1]
    return heuristic[node]


def get_cost(path):
    total = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]
        total = total + campus[current][next_node]

    return total


def gbfs(start, goal):
    frontier = [[start]]
    count = 0

    while len(frontier) > 0:
        frontier.sort(key=get_h)

        path = frontier.pop(0)
        node = path[-1]

        count = count + 1

        print("Exploring:", node,
              "h =", get_h(path))

        if node == goal:
            print("Total nodes explored:", count)
            return path

        for neighbour in campus[node]:
            new_path = path + [neighbour]
            frontier.append(new_path)

    return None


answer = gbfs("Hostel", "Library")

print()
print("Path found by GBFS:", answer)
print("Total cost of this path:", get_cost(answer))