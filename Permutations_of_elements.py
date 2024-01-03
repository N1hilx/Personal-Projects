from typing import List


def seat_permutations(friends: List[str]) -> List[List[str]]:
    if len(friends) == 0:
        return [[]]
    elif len(friends) == 1:
        return [friends]
    else:
        permutations = []
        for i in range(len(friends)):
            ele = [friends[i]]
            all_other_ele = friends[:i] + friends[i+1:]
            for elements in seat_permutations(all_other_ele):
                permutations.append(ele + elements)
        return permutations


