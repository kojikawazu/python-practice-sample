# dependency_inversion.py
from abc import ABCMeta, abstractmethod, abstractproperty

# --------------------------------------------------------
# 依存性逆転の原則
# --------------------------------------------------------

# Bookインターフェース
class IBook(metaclass=ABCMeta):

    @abstractproperty
    def content(self):
        pass

# Bookクラス
# IBookを継承する
class Book(IBook):

    def __init__(self, content):
        self._content = content
    
    @property
    def content(self):
        return self._content

# EBookクラス
# IBookを継承する
class EBook(IBook):

    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return 'E' + self._content

# フォーマッターインターフェース
class IFormatter(metaclass=ABCMeta):

    @abstractmethod
    def format(self, i_book: IBook):
        pass

# HTMLフォーマッター
# IFormatterを継承する
class HtmlFommater(IFormatter):

    # IBookとすれば、メソッドの追加が不要となる
    def format(self, i_book: IBook):
        return '<h1>' + i_book.content + '</h1>'

# XMLフォーマッター
# IFormatterを継承する
class XmlFommater(IFormatter):

    # IBookとすれば、メソッドの追加が不要となる
    def format(self, i_book: IBook):
        return '<xml>' + i_book.content + '</xml>'

# Printerクラス
class Printer:

    # IFormatterとすれば、メソッドの追加が不要となる
    def __init__(self, i_formatter: IFormatter):
        self._i_fomatter = i_formatter
    
    # IBookとすれば、メソッドの追加が不要となる
    def print(self, i_book: IBook):
        formatted_book = self._i_fomatter.format(i_book)
        print(formatted_book)

# グローバル
book = Book('My Book')
html_formatter = HtmlFommater()
html_printer = Printer(html_formatter)
html_printer.print(book)

# xmlフォーマッターを実装しやすくなった
xml_fommater = XmlFommater()
xml_printer = Printer(xml_fommater)
xml_printer.print(book)

# EBookクラスを実装しやすくなった
ebook = EBook('My Book')
html_printer.print(ebook)

# [依存性逆転の原則に適していない]
#
# class Book:
#     def __init__(self, content):
#         self.content = content

# class Formatter:
#     def format(self, book: Book):
#         return book.content

# # AformatterをPrinterで使用できない
# # 拡張性しにくい
# class AFomatter:
#     def format(self, book: Book):
#         return book.content + 'A'

# class Printer:
#     def print(self, book: Book):
#         formatter = Formatter()
#         Formatted_book = formatter.format(book)
#         print(Formatted_book)

# book = Book('My Book')
# printer = Printer()
# printer.print(book)