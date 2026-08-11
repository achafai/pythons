import math


def get_player_pos() -> tuple:
    while True:
        try:
            inputs = input("Enter coordinates as floats in format 'x, y, z': ")
            inputs_list = str.split(inputs, ",")
            coordinates = tuple(float(num) for num in inputs_list)
            break
        except ValueError:
            print("Invalid syntax")
    return coordinates


if __name__ == "__main__":
    a = get_player_pos()
    print(f"Got a first tupel: {a}")
    print(f"It includes: X={float(a[0])}, Y={float(a[1])}, Z={float(a[2])}")
    distance = round(math.sqrt(a[0]**2 + a[1]**2 + a[2]**2), 4)
    print(f"Distance to centre: {distance}")
    print("Get a second set of coordinates")
    b = get_player_pos()
    dst = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)
    dst = round(dst, 4)
    print(f"Distance between the 2 sets of coordinates: {dst}")
