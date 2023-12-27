from calendar import day_name, weekday

if __name__ == "__main__":
    days = day_name
    m, d, y = list(map(int, input().split()))
    day_num = weekday(y, m, d)
    print(days[day_num].upper())
