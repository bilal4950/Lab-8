warehouse = {
    "Receiving": {
        "Aisle1": 40,
        "Aisle2": 70
    },

    "Aisle1": {
        "Aisle2": 30,
        "Packing Station": 90
    },

    "Aisle2": {
        "Packing Station": 35
    },

    "Packing Station": {}
}


heuristic = {
    "Receiving": 100,
    "Aisle1": 70,
    "Aisle2": 35,
    "Packing Station": 0
}


def get_g(path):
    total = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]

        total = total + warehouse[current][next_node]

    return total


def get_h(path):
    node = path[-1]
    return heuristic[node]


def get_f(path):
    return get_g(path) + get_h(path)


def a_star(start, goal):
    frontier = [[start]]

    count = 0

    while len(frontier) > 0:

        frontier.sort(key=get_f)

        path = frontier.pop(0)

        node = path[-1]

        count = count + 1

        print(
            "Exploring:",
            node,
            "g =",
            get_g(path),
            "h =",
            get_h(path),
            "f =",
            get_f(path)
        )

        if node == goal:
            print("Total nodes explored:", count)
            return path

        for neighbour in warehouse[node]:

            new_path = path + [neighbour]

            frontier.append(new_path)

    return None


answer = a_star("Receiving", "Packing Station")

print()

print("Path found by A*:", answer)

print("Total cost of this path:", get_g(answer))
