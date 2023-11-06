import numpy as np

def numpy_array_to_obj(vertices, filename):
    """
    Convert a NumPy array of vertices to a .obj file.

    Args:
        vertices (np.ndarray): A 2D NumPy array of shape (n_vertices, 3) containing the x, y, and z coordinates of each vertex.
        filename (str): The name of the output .obj file.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        for v in vertices:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")



# vertices = np.array([
#     [0.0, 0.0, 0.0],
#     [1.0, 0.0, 0.0],
#     [0.0, 1.0, 0.0],
#     [0.0, 0.0, 1.0],
# ])
#
# numpy_array_to_obj(vertices, "example.obj")