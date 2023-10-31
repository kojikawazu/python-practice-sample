# singleton2.py

# constractorをprivateにするが、pythonは出来ないのでその対策
class Database2:

    # インスタンス
    __instance = None

    def __init__(self):
        raise RuntimeError('このクラスのコンストラクタは使用不可')

    @classmethod
    def get_instance(cls, database_url=None):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
        if database_url:
            cls.__instance.__database_url = database_url
        return cls.__instance
    
    @property
    def database_url(self):
        return self.__database_url
    
    @database_url.setter
    def database_url(self, database_url):
        self.__database_url = database_url

    # databaseに接続
    def connect(self):
        pass

# グローバル
a = Database2.get_instance('127.0.0.1')
b = Database2.get_instance()

print(a==b)
print(id(a), id(b))
print(a.database_url, b.database_url)