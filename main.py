def felszin(a: float) -> float:
    return 6 * a ** 2


def terfogat(a: float) -> float:
    return a ** 3


def Main() -> None:
    print('Kocka A és V:')
    a: float = float(input("a:"))
    if a <= 0:
        print('Nincs ilyen kocka!')
    else:
        print(f'Kocka felszíne: {felszin(a)}')
        print(f'Kocka térfogata: {terfogat(a)}')


if __name__ == "__main__":
    Main()
