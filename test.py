from audioop import reverse


def square_sum(square_sum):
    lst = square_sum.split()
    lst2 = []
    for word in lst:
        if len(word) >= 5:
            lst2.append(word[::-1])
        else:
            lst2.append(word)
    str = ' '.join(lst2)

    print(str)


square_sum("Hey fellow warriors")