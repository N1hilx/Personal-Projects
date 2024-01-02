import numpy as np

# Túto funkciu implementujte
def rm_edge(ft_arr: np.ndarray, n: int):
    ft_arr[:n] = 0  # First n rows set to 0
    ft_arr[-n:] = 0 # Last n rows set to 0
    ft_arr[::, :n] = 0 # For every row set first n elements to 0
    ft_arr[::, -n:] = 0  # For every row set last n elements to 0

    return ft_arr

# Testy:
arr = np.array([[1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]])

print(rm_edge(arr, 1))
# [[0 0 0 0 0]
#  [0 1 1 1 0]
#  [0 1 1 1 0]
#  [0 1 1 1 0]
#  [0 0 0 0 0]]

arr = np.array([[1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]])

print(rm_edge(arr, 3))
# [[0 0 0 0 0]
#  [0 0 0 0 0]
#  [0 0 0 0 0]
#  [0 0 0 0 0]
#  [0 0 0 0 0]]


print(rm_edge(arr, 0))