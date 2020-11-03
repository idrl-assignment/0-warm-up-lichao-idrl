import numpy as np
from PIL import Image# TODO: import ...


def generate_random_matrix(m, n):
    matrix=np.random.randint(0,2,(m,n))
    return matrix


def save_matrix(matrix, file_name):
    im=Image.fromarray(matrix)
    im.save("example.png")
    return


if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.png")
