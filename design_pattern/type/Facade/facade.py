# facade.py

# Knifeクラス
class Knife:

    def __init__(self, name):
        self.__name = name

    def cut_vegetables(self):
        print(f'野菜を{self.__name}をカットします')

# Boilerクラス
class Boiler:

    def __init__(self, name):
        self.__name = name

    def boil_vegetables(self):
        print(f'野菜を{self.__name}をボイルします')

# Flierクラス
class Flier:

    def __init__(self, name):
        self.__name = name

    def fry_vegetables(self):
        print(f'野菜を{self.__name}でフライします')

# Cookクラス
class Cook:

    def __init__(self, knife: Knife, flier: Flier, boiler: Boiler):
        self.__knife = knife
        self.__flier = flier
        self.__boiler = boiler

    def cook_dish(self):
        self.__knife.cut_vegetables()
        self.__flier.fry_vegetables()
        self.__boiler.boil_vegetables()

# グローバル
knife = Knife('My knife')
boiler = Boiler('My boiler')
flier = Flier('My flier')

cook = Cook(knife, flier, boiler)
cook.cook_dish()
