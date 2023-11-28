from typing import List

def is_face_on_photo(photo: List[List[str]]) -> bool:
    rows = len(photo)
    columns = len(photo[0]) if rows > 0 else 0

    for i in range(rows - 1):
        for j in range(columns - 1):
            # Check for face patterns horizontally
            if photo[i][j] + photo[i][j + 1] + photo[i + 1][j] + photo[i + 1][j + 1] in ["face", "afce", "cefa", "ecaf"]:
                return True

            # Check for face patterns vertically
            if photo[i][j] + photo[i + 1][j] + photo[i][j + 1] + photo[i + 1][j + 1] in ["face", "afce", "cefa", "ecaf"]:
                return True

    return False        
    

print(is_face_on_photo([['f', 'a'], ['c', 'e']]))  # True
print(is_face_on_photo([['f', 'a', 'c', 'e']]))  # False
print(is_face_on_photo([['e', 'c', 'x'], ['a', 'f', 'x'], ['x', 'x', 'x']]))  # True
print(is_face_on_photo([['f', 'f', 'x'], ['a', 'a', 'x'], ['x', 'x', 'x']]))  # False
print(is_face_on_photo([['x', 'x', 'x'], ['a', 'f', 'x'], ['c', 'e', 'x']]))  # True
