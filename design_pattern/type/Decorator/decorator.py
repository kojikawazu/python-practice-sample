from abc import ABC, abstractmethod
# decorator.py

# Componentインターフェース
class Component(ABC):

    @abstractmethod
    def oparation(self):
        pass

# ShowCharComponentクラス
# 継承：Component
class ShowCharComponent(Component):

    def __init__(self, char):
        self.__char = char

    def oparation(self):
        print(self.__char * 20)

# ShowDecoratorクラス
# 継承：Component
class ShowDecorator(Component):

    def __init__(self, component: Component):
        self._component = component

# ShowMessageクラス
# ShowDecorator
class ShowMessage(ShowDecorator):

    def __init__(self, component: Component, msg):
        super().__init__(component)
        self.__msg = msg

    def oparation(self):
        self._component.oparation()    # Componentのメソッド
        print(self.__msg)              # ShowMessageクラスのメソッド    
        self._component.oparation()

class WriteDecorator(Component):

    def __init__(self, component: Component, file_name, msg):
        self._component = component
        self._file_name = file_name
        self._msg = msg

class WriteMessage(WriteDecorator):

    def oparation(self):
        self._component.oparation()
        with open(self._file_name, mode='w') as fh:
            fh.write(self._msg)

# グローバル
print('[1]')
show_component = ShowCharComponent('-')
show_component.oparation()

print('[2]')
show_message = ShowMessage(show_component, 'Hello World')
show_message.oparation()

print('[3]')
write_message = WriteMessage(show_message, 'tmp.txt', 'Write Message')
write_message.oparation()

