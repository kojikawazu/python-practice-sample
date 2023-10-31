from abc import ABC, abstractmethod, abstractproperty
# FactoryMethodパターン

# Factoryインターフェース
class IFactory(ABC):

    def __init__(self):
        self.registered_owners = []

    def create(self, owner):
        self._owner = owner
        product = self._create_product()
        self._register_product(product)
        return product

    @abstractmethod
    def _create_product(self):
        pass

    @abstractmethod
    def _register_product(self, product):
        pass

# 車Factoryクラス
class CarFactory(IFactory):

    def _create_product(self):
        return Car(self._owner)
    
    def _register_product(self, product):
        self.registered_owners.append(product.owner)

class ShipFactory(IFactory):

    def _create_product(self):
        return Ship(self._owner)

    def _register_product(self, product):
        self.registered_owners.append(product.owner)

class IProduct(ABC):

    def __init__(self, owner):
        self._owner = owner

    @abstractmethod
    def use(self):
        pass

    @abstractmethod
    def owner(self):
        pass

class Car(IProduct):

    def use(self):
        print(f'{self.owner}: 車を運転する')

    @property
    def owner(self):
        return self._owner

class Ship(IProduct):

    def use(self):
        print(f'{self.owner}: 船を運転する')
    
    @property
    def owner(self):
        return self._owner

print('[1]')
car_fatory = CarFactory()
yamada_car = car_fatory.create('山田')
sato_car = car_fatory.create('佐藤')

yamada_car.use()
sato_car.use()
print(car_fatory.registered_owners)

print('[2]')
ship_fatory = ShipFactory()
john_ship = ship_fatory.create('John')
ken_ship = ship_fatory.create('Ken')

john_ship.use()
ken_ship.use()
print(ship_fatory.registered_owners)