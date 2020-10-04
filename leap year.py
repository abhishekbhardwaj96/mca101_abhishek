def is_leap(n):
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False
