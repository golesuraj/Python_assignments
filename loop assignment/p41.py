for i in range(1, 101):
    root = round(i ** (1 / 3))
    if root ** 3 == i:
        print(i)
