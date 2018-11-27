import math

class Fire:

    def __init__(self):
        pass

    def parabola(self, angle, power):
        x = 0
        y = 0
        t = 1
        g = 2

        pointlist = []

        while y >= 0:
            x = int((power * math.cos(angle * math.pi / 180)) * t)
            y = int(((power * math.sin(angle * math.pi / 180)) * t) - (0.5 * g * t * t))
            pointlist.append((x//20, y//20))
            t += 1
        del pointlist[-1]


        return pointlist

    def finished(self, point, target):
        if point == target:
            return True
        else:
            return False


if __name__ == '__main__':
    fire = Fire()
    print(fire.parabola(45,50))