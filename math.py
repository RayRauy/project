import matplotlib.pyplot as plt
import numpy as np

def impossible(x):
    counter = 0
    s = []
    s.append(x)
    while x > 1:
        if x % 2 == 1:
            x = 3*x+1
            s.append(x)
            counter += 1
        else:
            x = x // 2
            s.append(x)
            counter += 1
    return s, counter

inputs = int(input("Enter a number: "))
result = impossible(inputs)
x = np.array(result[0])
y = np.array(range(len(result[0])))
print(result)
plt.plot(y, x, marker='.')  # Example plot point
plt.show()
