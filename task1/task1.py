import sys
''' python task1.py 5 4
    python task1.py 4 3 '''


def circular_array_path(n, m):
    circular_array = list(range(1, n + 1))
    path = []
    current_index = 0

    while True:
        path.append(circular_array[current_index])
        current_index = (current_index + m - 1) % n
        if current_index == 0:
            break
    return ''.join(map(str, path))


if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    print(circular_array_path(n, m))
