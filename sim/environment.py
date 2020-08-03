import numpy as np
import matplotlib.pyplot as plt

class Boundry:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        plt.plot([self.p1[0], self.p2[0]],
                 [self.p1[1], self.p2[1]],
                 'k')

class Object:
    def __init__(self):
        pass

class Environment:
    def __init__(self):
        self.bounds = []

    def add_bound(self, bound : Boundry):
        self.bounds.append(bound)

    def draw(self):
        for b in self.bounds:
            b.draw()

    def show(self):
        plt.axis('equal')
        plt.show()


def procedural_environment():
    np.random.seed(190)

    env = Environment()

    scale = 500.
    width  = 60
    height = 40

    def get_state(a, b, c, d):
        return a*1+b*2+c*4+d*8

    def plt_line(p1, p2):
        #plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k')
        env.add_bound(Boundry(p1, p2))

    canvas = np.random.rand(width+1, height+1)
    new_canvas = np.zeros([width+1, height+1])
    for i in range(2, width):
        for j in range(2, height):
            new_canvas[i,j] = 0.5 * canvas[i, j] + 0.125 * canvas[i+1, j] + 0.125 * canvas[i-1, j] + 0.125 * canvas[i, j+1] + 0.125 * canvas[i, j-1]

    canvas = new_canvas > 0.25
    for i in range(width):
        for j in range(height):
            a = [scale * (i+0.5), scale * j]
            b = [scale * (i+1), scale * (j+0.5)]
            c = [scale * (i+0.5), scale * (j+1)]
            d = [scale * i, scale * (j+0.5)]
            s = get_state(canvas[i,j], canvas[i+1,j], canvas[i+1,j+1], canvas[i,j+1])
            if s == 1:
                plt_line(a, d)
            elif s == 2:
                plt_line(a, b)
            elif s == 3:
                plt_line(d, b)
            elif s == 4:
                plt_line(b, c)
            elif s == 5:
                plt_line(c, d)
                plt_line(a, b)
            elif s == 6:
                plt_line(a, c)
            elif s == 7:
                plt_line(c, d)
            elif s == 8:
                plt_line(c, d)
            elif s == 9:
                plt_line(a, c)
            elif s == 10:
                plt_line(a, d)
                plt_line(b, c)
            elif s == 11:
                plt_line(b, c)
            elif s == 12:
                plt_line(b, d)
            elif s == 13:
                plt_line(a, b)
            elif s == 14:
                plt_line(a, d)
            

            """
            if canvas[i,j]:
                plt.plot(i, j, 'or')
            else:
                plt.plot(i, j, 'og')
            """


    #env.draw()
    #env.show()
    
    return env

if __name__ == "__main__":
    procedural_environment()
