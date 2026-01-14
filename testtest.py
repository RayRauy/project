import matplotlib.pyplot as plt

def impossible(x):
    plt.ion()
    fig, ax = plt.subplots()

    xs = []
    ys = []

    step = 0
    xs.append(step)
    ys.append(x)

    line, = ax.plot(xs, ys, marker='.')  # NOTE the comma

    ax.set_xlabel("Step")
    ax.set_ylabel("Value")
    ax.margins(0)

    plt.pause(0.2)

    while x > 1:
        if x % 2 == 1:
            x = 3 * x + 1
        else:
            x = x // 2

        step += 1
        xs.append(step)
        ys.append(x)

        line.set_data(xs, ys)   # update line data
        ax.relim()              # recompute limits
        ax.autoscale_view()     # rescale axes
        plt.pause(0.3)          # redraw

    plt.ioff()
    plt.show()


inputs = int(input("Enter a number: "))
impossible(inputs)
