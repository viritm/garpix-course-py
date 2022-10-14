
class Parallelepiped:

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_volume(self):
        return self.length * self.width * self.height

    def get_base_square(self):
        return self.width * self.length

    def get_first_side_square(self):
        return self.width * self.height

    def get_second_side_square(self):
        return self.length * self.height

    @staticmethod
    def info():
        print(list(filter(lambda x: not x.startswith('__'), dir(Parallelepiped))))


a = Parallelepiped(2, 4, 6)
print(a.get_volume())
print(a.get_base_square())
print(a.get_first_side_square())
print(a.get_second_side_square())
Parallelepiped.info()
