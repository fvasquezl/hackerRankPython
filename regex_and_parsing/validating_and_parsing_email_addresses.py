import email.utils

if __name__ == "__main__":
    # regex_pattern = r"(?<=\d+)(?:[\.]|[\,])(?=\d+)"
    # print("\n".join(re.split(regex_pattern, input())))

    for _ in range(int(input())):
        n, e = list(map(str, input().split()))
        print("-")
        print(email.utils.parseaddr(f"{n} {e}"))
        # print(email.utils.formataddr((n, e)))
