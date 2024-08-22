import sys
import math

''' python task2.py circle.txt points.txt '''


def read_circle(file_path):
    with open(file_path, 'r') as file:
        center_x, center_y = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return center_x, center_y, radius


def read_points(file_path):
    with open(file_path, 'r') as file:
        points = []
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points


def check_point(circle_x, circle_y, radius, point_x, point_y):
    distance_squared = (point_x - circle_x) ** 2 + (point_y - circle_y) ** 2
    radius_squared = radius ** 2

    if math.isclose(distance_squared, radius_squared, rel_tol=1e-9):
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2


def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py <файл с окружностью> <файл с точками>")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    circle_x, circle_y, radius = read_circle(circle_file)
    points = read_points(points_file)

    results = []
    for x, y in points:
        result = check_point(circle_x, circle_y, radius, x, y)
        results.append(str(result))

    print("\n".join(results))


if __name__ == "__main__":
    main()
