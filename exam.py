import matplotlib.pyplot as plt

def paint(x_a, x_b, x_c, y_a, y_b, y_c, x_max, y_max):
    t = []
    for y in range(1, y_max + 1):
        for x in range(1, x_max + 1):
            s1 = (x_a - x) * (y_b - y_a) - (x_b - x_a) * (y_a - y)
            s2 = (x_b - x) * (y_c - y_b) - (x_c - x_b) * (y_b - y)
            s3 = (x_c - x) * (y_a - y_c) - (x_a - x_c) * (y_c - y)
            if (s1 <= 0 and s2 <= 0 and s3 <= 0) or (s1 >= 0 and s2 >= 0 and s3 >= 0):
                t.append([x, y])
    return t


pars = input()
pars = pars.split()
x_max = max(int(pars[0]), int(pars[2]), int(pars[4]))
y_max = max(int(pars[1]), int(pars[3]), int(pars[5]))
t = paint(int(pars[0]), int(pars[2]), int(pars[4]), int(pars[1]), int(pars[3]), int(pars[5]), x_max, y_max)
for i in t:
    plt.plot(i[0], i[1], 'ro')
plt.show()
