"""Module providing a function printing python version."""


def is_leap(year: int):
    """Function printing python version."""
    leap = False
    if year / 4 == year // 4 and year / 100 != year // 100 or year / 400 == year // 400:
        leap = True
    print(leap)
    return leap


# year = int(input())
# print(is_leap(year))

is_leap(1800)
is_leap(1900)
is_leap(1900)
is_leap(2100)
is_leap(2200)
is_leap(2300)
is_leap(2500)
is_leap(2000)
is_leap(2400)
is_leap(1990)
is_leap(1904)
is_leap(1908)
is_leap(1912)
is_leap(1916)
is_leap(1920)
is_leap(1924)
is_leap(1928)
is_leap(1932)
is_leap(1936)
is_leap(1940)
is_leap(1944)
is_leap(1948)
is_leap(1952)
is_leap(1956)
is_leap(1960)
is_leap(1964)
is_leap(1968)
is_leap(1972)
is_leap(1976)
is_leap(1980)
is_leap(1984)
is_leap(1988)
is_leap(1992)
is_leap(1996)
