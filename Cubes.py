import Utils

CUBE_SIDES = 6


def start():  # This is definitely wrong im stumped
    print(Utils.formatColor("Cube calculator!!1"))

    dimension = int(input("Enter the dimension of your cube: "))

    sides_per_face = dimension ** 2

    total_faces = sides_per_face * dimension * 6

    visible_faces = sides_per_face * CUBE_SIDES
    hidden_faces = total_faces - visible_faces
    # hidden_faces = visible_faces * (dimension - 1) # OLD WAY OF CALCULATING

    print(Utils.formatColor("Visible faces: %s", visible_faces))
    print(Utils.formatColor("Hidden faces: %s", hidden_faces))


if __name__ == "__main__":
    start()
