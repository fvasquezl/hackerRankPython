import re

fun = lambda x: re.fullmatch(r"\b[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{3}\b", x)

# def fun(s):
#     # return True if s is a valid email, else return False
#     r = r"\b[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{3}\b"
#     return re.fullmatch(r, s)


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
