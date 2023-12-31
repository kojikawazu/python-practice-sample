from abc import ABC, abstractmethod
from datetime import datetime
# state.py

# Stateインターフェース
class State(ABC):

    @abstractmethod
    def begin(self):
        pass
    
    @abstractmethod
    def write_log(self):
        pass

    @abstractmethod
    def end(self):
        pass

class DayState(State):

    def begin(self):
        print('昼の処理を開始します')

    def write_log(self):
        with open('tmp.txt', mode='w', encoding='utf-8') as fh:
            fh.write('昼のログ')

    def end(self):
        print('昼の処理を終了します')

class NightState(State):

    def begin(self):
        print('夜の処理を開始します')

    def write_log(self):
        with open('tmp.txt', mode='w', encoding='utf-8') as fh:
            fh.write('夜のログ')

    def end(self):
        print('夜の処理を終了します')

class Context:

    def __init__(self):
        self.__state = DayState()

    def do(self):
        self.__state.begin() # stateで処理を実行して、stateの中に処理を入れる
        self.__state.write_log()
        self.__state.end()

    def change_state(self, state: State):
        self.__state = state

    def change_state_by_time(self):
        now = datetime.now()
        if (now.hour < 6) or (now.hour >= 19):
            self.__state = NightState()
        else:
            self.__state = DayState()

# グローバル
print('[1]')
context = Context()
context.do()
print('-' * 100)

print('[2]')
context.change_state(NightState())
context.do()
print('-' * 100)

print('[3]')
context.change_state_by_time()
context.do()
