# Experimenting a bit with the logistic map

ITERATIONS = 70

def logistic_map(x, r):
    return r * x * (1 - x)

def get_population(x_init, r):
    result = [x_init]
    x_next = x_init
    for i in range(ITERATIONS):
        x_next = logistic_map(x_next, r)
        result.append(x_next)
    return result

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    pop_list1 = get_population(0.5, 2.7) # normal
    pop_list2 = get_population(0.5, 3.2) # bifurcation
    pop_list3 = get_population(0.5, 3.7) # chaos
    xlist = range(ITERATIONS + 1)

    plt.plot(xlist, pop_list1)
    plt.plot(xlist, pop_list2)
    plt.plot(xlist, pop_list3)
    plt.ylim(0.0, 1.0)
    plt.show()
