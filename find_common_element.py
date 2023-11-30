def list_intersection_3(l1, l2, l3):
    spies = []
    for spy in l1:
        if spy in l2 and spy in l3:
            spies += [spy]
    return spies


# ukázka zavolání funkce

def main():
    animals = ['kočka', 'pes']
    rhyme = ['pes', 'les', 'mez', 'ves', 'dnes']
    song = ['skákal', 'pes', 'přes', 'oves']

    for spy in list_intersection_3(animals, rhyme, song):
        print(spy)

if __name__ == '__main__':
    main()
