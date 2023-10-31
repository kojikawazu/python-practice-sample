from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import pickle
# memento.py

# Originatorクラス
class Originator:

    def __init__(self, state, name):
        self._state = state
        self._name = name
    
    def change_state(self, state):
        print(f'Change state 実行: {state}')
        self._state = state

    def change_name(self, name):
        print(f'Change name 実行: {name}')
        self._name = name

    def __str__(self):
        return f'State: {self._state} name: {self._name}'

    def save(self):
        return ConcreteMemento(self._state, self._name)

    def restore(self, memento):
        self._state = memento.state
        self._name = memento.name
        print(f"Originator: State change to: {self._state}")

# Mementoインターフェース
class Memento(ABC):
    
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractproperty
    def date(self):
        pass

# ConcreteMementoクラス
# 継承：Memento
class ConcreteMemento(Memento):
    
    def __init__(self, state, name):
        self._state = state
        self._name = name
        self._date = datetime.now()

    @property
    def state(self):
        return self._state

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    def get_name(self):
        return f"{self.date} / ({self.state})"

# CareTakerクラス
class CareTaker:

    def __init__(self):
        self._mementos = []

    def backup(self, memento: Memento):
        print(f'Originalの状態を保存: {memento.get_name()}')
        self._mementos.append(memento)

    def undo(self):
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        return memento
    
    def show_history(self):
        print(f'変更履歴')
        for memento in self._mementos:
            print(memento.get_name())

# OriginatorBackupクラス
class OriginatorBackup:

    @staticmethod
    def dump_file(originator, file_name):
        with open(file_name, mode='wb') as fh:
            pickle.dump(originator, fh)

    @staticmethod
    def load_file(file_name):
        with open(file_name, mode='rb') as fh:
            return pickle.load(fh)

# グローバル
print('[1]')
originator = Originator('FirstState', 'Originator 1')
care_taker = CareTaker()

# バックアップ保存
backup_instance = originator.save()
care_taker.backup(backup_instance)
print(f'{originator}\n')

print('[2]')
originator.change_state('SecondState')

# バックアップ保存
backup_instance = originator.save()
care_taker.backup(backup_instance)
print(f'{originator}\n')

print('[3]')
originator.change_state('ThirdState')
originator.change_name('New Originator 2')
print(f'{originator}\n')

print('[4]')
undo_instance = care_taker.undo()
originator.restore(undo_instance)
print(f'{originator}\n')

care_taker.show_history()
print('')

print('[5]')
#OriginatorBackup.dump_file(originator, 'tmp.dump')
originator_2 = OriginatorBackup.load_file('tmp.dump')
print(originator_2)
print(type(originator_2))