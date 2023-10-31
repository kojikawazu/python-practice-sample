from abc import ABC, abstractmethod
# visitor.py

# Elementインターフェース
class ItemElement(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass

# Bookクラス
# 継承：Element
class Book(ItemElement):

    def __init__(self, price, isbn):
        self.__price = price
        self.__isbn = isbn

    @property
    def price(self):
        return self.__price

    @property
    def isbn(self):
        return self.__isbn

    def accept(self, visitor):
        return visitor.visit(self)

# Fluitクラス
# 継承：Element
class Fluit(ItemElement):

    def __init__(self, price, weight, name):
        self.__price = price
        self.__weight = weight
        self.__name = name

    @property
    def price(self):
        return self.__price

    @property
    def weight(self):
        return self.__weight

    @property
    def name(self):
        return self.__name
    
    def accept(self, visitor):
        return visitor.visit(self)

# Visitorインターフェース
class Visitor(ABC):

    @abstractmethod
    def visit(self, item):
        pass

# ShoppingVisitorクラス
# 継承：Visitor
class ShoppingVisitor(Visitor):

    # itemの値段を返す
    def visit(self, item: ItemElement):
        if isinstance(item, Book):
            cost = item.price
            if cost >= 50:
                cost -= 10
            print(f"Book ISBN: {item.isbn}, cost = {cost}")
            return cost
        elif isinstance(item, Fluit):
            cost = item.price * item.weight
            cost = cost * 0.8
            print(f"{item.name} cost = {cost}")
            return cost

# グローバル

# 値段算出
def calcurate_price(items):
    visitor = ShoppingVisitor()
    sum = 0
    for item in items:
        sum += item.accept(visitor)
    return sum

items = [
    Book(20, '1111'),
    Book(100, '2222'),
    Fluit(8, 10, 'Banana'),
    Fluit(10, 5, 'Apple')
]

# Bookは50円以上の場合、10円引き
# Fluitは20%OFF
print(f"Total Cost = {calcurate_price(items)}")
