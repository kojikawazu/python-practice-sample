# open_closed.py
from abc import ABCMeta, abstractmethod

# --------------------------------------------------------
# 開放閉鎖の原則
# --------------------------------------------------------

# ユーザー情報クラス
class UserInfo:

    # コンストラクタ
    def __init__(self, user_name, job_name, nationality):
        self.user_name = user_name
        self.job_name = job_name
        self.nationality = nationality
    
    def __str__(self):
        return '{} {} {}'.format(
            self.user_name, self.job_name, self.nationality
        )

# 比較クラス(親)
class Comparation(metaclass=ABCMeta):

    @abstractmethod
    def is_equal(self, other):
        pass
    
    def __and__(self, other):
        return AndCompration(self, other)
    
    def __or__(self, other):
        return OrComparation(self, other)

# And比較クラス
class AndCompration(Comparation):

    def __init__(self, *args):
        self.comparations = args

    def is_equal(self, other):
        return all(
            map(
                lambda comparation: comparation.is_equal(other),
                self.comparations
            )
        )

# or比較クラス
class OrComparation(Comparation):

    def __init__(self, *args):
        self.comparations = args

    def is_equal(self, other):
        return any(
            map(
                lambda comparation: comparation.is_equal(other),
                self.comparations
            )
        )

# フィルタークラス(親)
class Filter(metaclass=ABCMeta):

    @abstractmethod
    def filter(self , comparation, items):
        pass

# ジョブ名比較クラス
class JobNameComparation(Comparation):

    def __init__(self, job_name):
        self.job_name = job_name
    
    def is_equal(self, other):
        return self.job_name == other.job_name

# 国籍比較クラス
class NationalityComparation(Comparation):

    def __init__(self, nationality):
        self.nationality = nationality

    def is_equal(self, other):
        return self.nationality == other.nationality

# ユーザー情報フィルタークラス
class UserInfoFilter(Filter):

    def filter(self, comparation, items):
        for item in items:
            if comparation.is_equal(item):
                yield item

# グローバル
taro = UserInfo('taro', 'salary man', 'Japan')
jiro = UserInfo('jiro', 'police man', 'Japan')
john = UserInfo('john', 'salary man', 'USA')
user_list = [taro, jiro, john]

# ジョブ比較
print('[1]')
salary_man_comparation = JobNameComparation('salary man')
user_info_filter = UserInfoFilter()
for user in user_info_filter.filter(salary_man_comparation, user_list):
    print(user)

# 国籍比較
print('[2]')
japan_comparation = NationalityComparation('Japan')
for user in user_info_filter.filter(japan_comparation, user_list):
    print(user)

# and比較
print('[3]')
salary_man_and_japan = salary_man_comparation & japan_comparation
for user in  user_info_filter.filter(salary_man_and_japan, user_list):
    print(user)

# or比較
print('[4]')
salary_man_or_japan = salary_man_comparation | japan_comparation
for user in  user_info_filter.filter(salary_man_or_japan, user_list):
    print(user)

# [誤り]
# ユーザー情報フィルタークラス
# class UserInfoFilter:

#     @staticmethod
#     def filter_users_job(users, job_name):
#         for user in users:
#             if user.job_name == job_name:
#                 yield user

#     @staticmethod
#     def filter_users_nationality(users, nationality):
#         for user in users:
#             if user.nationality == nationality:
#                 yield user

# for man in UserInfoFilter.filter_users_job(user_list, 'police man'):
#     print(man)

# for man in UserInfoFilter.filter_users_nationality(user_list, 'Japan'):
#     print(man)