# interface_segregation.py
from abc import ABCMeta, abstractmethod

# --------------------------------------------------------
# インタフェース分離の原則
# --------------------------------------------------------

# アスリートインターフェース
class Athlate(metaclass=ABCMeta):
    pass

# スイムのアスリートインターフェース
# 継承：Athlate
class SwimAthlate(Athlate):

    # メソッドをインターフェースごとに分ける
    @abstractmethod
    def swim(self):
        pass

# ジャンプのアスリートインターフェース
# 継承:Athlate
class JumpAthlate(Athlate):

    # メソッドをインターフェースごとに分ける
    @abstractmethod
    def high_jump(self):
        pass

    # メソッドをインターフェースごとに分ける
    @abstractmethod
    def long_jump(self):
        pass

# アスリートクラス1
# 継承：スイムアスリートインターフェース
class Athlate1(SwimAthlate):
    
    # スイムインターフェースを継承すれば、
    # スイムで定義したメソッドのみメソッド定義可能となる
    def swim(self):
        print('I swim')

# アスリートクラス2
# 継承：スイムアスリートインターフェース,
#       ジャンプアスリートインターフェース
class Athlate2(SwimAthlate, JumpAthlate):
    
    # 両インターフェースを継承すれば、
    # 両インターフェースのメソッド定義が可能となる
    def swim(self):
        print('I swim')

    def high_jump(self):
        print('high jump')

    def long_jump(self):
        print('long jump')

# グローバル
john = Athlate1()
john.swim()

ken = Athlate2()
ken.swim()
ken.high_jump()
ken.long_jump()

# インタフェース分離の原則に適していない

# アスリートインターフェース
# class Athlate(metaclass=ABCMeta):
#     @abstractmethod
#     def swim(self):
#         pass
#
#     @abstractmethod
#     def high_jump(self):
#         pass
#
#     @abstractmethod
#     def long_jump(self):
#         pass

# # アスリートクラス1
# # 継承：スイムアスリートインターフェース
# class Athlate1(SwimAthlate):
#     全部のメソッドを継承しなければならなくなる    
#     def swim(self):
#         print('I swim')
#
#     def high_jump(self):
#         print('high jump')
#
#     def long_jump(self):
#         print('long jump')

# # グローバル
# john = Athlate1()
# john.swim()
