# liskov_substitution.py

# --------------------------------------------------------
# リスコフの置換原則
# --------------------------------------------------------

# 長方形
class Rectangle():

    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return _height

    @height.setter
    def height(self, height):
        self._height = height

    def culcurate_area(self):
        return self._width * self._height

# 四角クラス
class Square(Rectangle):

    def __init__(self, size):
        self._width = self._height = size

    @Rectangle.width.setter
    def width(self, size):
        self._width = self._height = size

    @Rectangle.height.setter
    def height(self, size):
        self._width = self._height = size

# エリアメソッド
def print_area(obj):
    change_to_width = 10
    change_to_height = 20
    obj.width = change_to_width
    obj.height = change_to_height

    if isinstance(obj, Square):
        change_to_width = change_to_height

    print('予想 = {}, 実際 = {}'.format(
        change_to_height * change_to_width,
        obj.culcurate_area()
    ))

# グローバル
rc = Rectangle(2,3)
print_area(rc)

sq = Square(5)
print_area(sq)

# リスコフの置換原則に適していない

# class Rectangle():
#
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#   
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, width):
#         self._width = width
#
#     @property
#     def height(self):
#         return _height
#
#     @height.setter
#     def height(self, height):
#         self._height = height
#
#     def culcurate_area(self):
#         return self._width * self._height


# # 四角クラス
# class Square(Rectangle):
#
#     def __init__(self, size):
#         self._width = self._height = size
#
#     @Rectangle.width.setter
#     def width(self, size):
#         self._width = self._height = size
#
#     @Rectangle.height.setter
#     def height(self, size):
#         self._width = self._height = size

# # エリアメソッド
# def print_area(obj):
#     change_to_width = 10
#     change_to_height = 20
#     obj.width = change_to_width
#     obj.height = change_to_height
#
#     print('予想 = {}, 実際 = {}'.format(
#         change_to_height * change_to_width,
#         obj.culcurate_area()
#     ))

# # グローバル
# rc = Rectangle(2,3)
# print_area(rc)
#
# sq = Square(5)
# print_area(sq)