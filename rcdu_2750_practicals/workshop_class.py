


class Volume:

    def __init__(self):
        pass

    def volume(self, l , w, h):
        print("volume = {}".format(l*w*h))

class Surface_area:
    first_number = 2
    second_number = 3

    def __init__(self, fn, sn):
        self.first_number = fn
        self.second_number = sn

    def surface(self, c):
        print(self.first_number * self.second_number + c)
        return

if __name__ == "__main__":
    s = Surface_area(5, 5)
    s.surface(10)

    v = Volume()
    v.volume(3, 5, 6)