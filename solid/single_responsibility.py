# single_responsibility.py

# --------------------------------------------------------
# 単一責任の原則
# --------------------------------------------------------

# ユーザー情報格納クラス
class UserInfo:
    # ユーザー情報を保持する役割
    
    # --------------------------------------------
    # [GOOD] 単一責任の原則を満たしている場合
    # --------------------------------------------

    # --------------------------------------------
    # コンストラクタ
    # --------------------------------------------
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number
    
    def __str__(self):
        return "{}, {}, {}".format(
            self.name, self.age, self.phone_number
        )
    
    # --------------------------------------------
    # [BAD] 単一責任の原則を満たしていない場合
    # --------------------------------------------
    #def write_str_to_file(self, filename):
    #    with open(filename, mode='w') as fh:
    #        fh.write(str(self))

# ファイルマネージャークラス
class FileManager:
    # ファイル操作の役割

    @staticmethod
    def write_str_to_file(obj, filename):
        with open(filename, mode='w') as fh:
            fh.write(str(obj))

# グローバル
user_info = UserInfo('Taro', 21, '000-0000-000')
print(str(user_info))
FileManager.write_str_to_file(user_info, 'tmp.txt')