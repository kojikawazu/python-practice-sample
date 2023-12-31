from abc import ABC, abstractmethod
# bridge.py

# 図形インターフェース
class Shape(ABC):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @abstractmethod
    def create_shape_str(self):
        pass

# 四角クラス
# 継承: Shape
class RectangleShape(Shape):

    def __init__(self, width, height):
        super().__init__(width, height)

    def create_shape_str(self):
        rectangle = '*' * self._width + '\n'
        for _ in range(self._height - 2):
            rectangle += '*' + ' ' * (self._width - 2) + '*' + '\n'
        rectangle += '*' * self._width + '\n'
        return rectangle

# 真四角クラス
# 継承: Shape
class SquareShape(Shape):

    def __init__(self, width, height=None):
        super().__init__(width, width)

    def create_shape_str(self):
        square = '*' * self._width + '\n'
        for _ in range(self._width - 2):
            square += '*' + ' ' * (self._width - 2) + '*' + '\n'
        square += '*' * self._width + '\n'
        return square 

# ライターAbstractionインターフェース
class WriteAbstraction(ABC):

    def __init__(self, shape: Shape):
        self._shape = shape

    def read_shape(self):
        return self._shape.create_shape_str()

    @abstractmethod
    def write_to_text(self, file_name):
        pass

# ライターShapeクラス
# 継承：WriteAbstraction
class WriteShape(WriteAbstraction):

    def write_to_text(self, file_name):
        with open(file_name, mode='w', encoding='utf-8') as fh:
            fh.write(self.read_shape())

# グローバル
print('[1]')
rectangle = RectangleShape(10, 5)
#print(rectangle.create_shape_str())

print('[2]')
square = SquareShape(10)
#print(square.create_shape_str())

print('[3]')
write_shape = WriteShape(rectangle)
write_shape.write_to_text('tmp.txt')