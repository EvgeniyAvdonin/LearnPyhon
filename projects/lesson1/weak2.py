def take_figures(one,two):
    if (one != str(one) and two != str(two)):
        return 0
    elif one == two:
        return 1
    elif len(one) > len(two):
        return 2
    elif (one != two and two == 'learn'):
        return 3
print(take_figures(2,4))


