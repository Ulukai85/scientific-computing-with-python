# Build a polygon area calculator project

class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def __str__(self):
        return f'Rectangle(width={self.w}, height={self.h})'

    def set_width(self, width):
        self.w = width

    def set_height(self, height):
        self.h = height

    def get_area(self):
        return self.w * self.h

    def get_perimeter(self):
        return 2 * self.w + 2 * self.h

    def get_diagonal(self):
        return (self.w ** 2 + self.h ** 2) ** .5

    def get_picture(self):
        if self.w > 50 or self.h > 50:
            return 'Too big for picture.'
        return ''.join(self.w * '*' + '\n' for i in range(self.h))

    def get_amount_inside(self, other):
        return (self.w // other.w) * (self.h // other.h)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.w})'

    def set_side(self, side):
        self.w = side
        self.h = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
