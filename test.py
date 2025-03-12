from audioop import reverse


def square_sum(square_sum):
    lst = square_sum.split()
    lst2 = []
    for word in lst:
        if len(word) >= 5:
            lst.append(word[::-1])
        print(lst2)


square_sum("Hey fellow warriors")