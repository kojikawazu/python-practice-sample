# singleton.py

class Database():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def database_url(self):
        return self.__database_url
    
    @database_url.setter
    def database_url(self, database_url):
        self.__database_url = database_url

    def connect(self):
        # Databaseに接続する
        pass

# グローバル
a = Database()
b = Database()

print(a==b)