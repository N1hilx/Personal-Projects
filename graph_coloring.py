from typing import List, Dict


COLORING = Dict[str, str]
COUNTRIES = List['Country']


class Country:
    name: str
    neighbors: List[str]

    def __init__(self, name: str, neighbors: List[str]):
        self.name = name
        self.neighbors = neighbors


def is_ok(coloring: COLORING, countries: COUNTRIES) -> bool:
    for c in countries:
        for n in c.neighbors:
            if c.name in coloring and n in coloring and coloring[c.name] == coloring[n]:
                return False

    return True

def is_final(
    coloring: COLORING,
    countries: COUNTRIES,
    country_index: int
) -> bool:
    return country_index == len(countries)


def solve_coloring(
    coloring: COLORING,
    countries: COUNTRIES,
    colors: List[str],
    country_index: int = 0
) -> bool:
    if not is_ok(coloring, countries):
        return False

    if is_final(coloring, countries, country_index):
        print(coloring)
        return True

    for color in colors:
        coloring[countries[country_index].name] = color
        if solve_coloring(coloring, countries, colors, country_index+1):
            return True

    return False


# Testy:
coloring: COLORING = {}
countries = [
    Country('El Sobov', ['La Losov']),
    Country('La Losov', ['El Sobov']),
]
print(solve_coloring(coloring, countries, ['RED', 'GREEN']))
