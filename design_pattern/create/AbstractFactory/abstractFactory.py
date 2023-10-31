from abc import ABC, abstractmethod
# abstractFactory.py

# アイテムインターフェース
class AbcItem(ABC):

    def __init__(self, caption):
        self.caption = caption
    
    @abstractmethod
    def make_html(self):
        pass

# ページアイテムインターフェース
# 継承：AbcItem
class PageItem(AbcItem):

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = []

    def add(self, item):
        self.content.append(item)

    def write_html(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as fh:
            fh.write(self.make_html())

# リンクアイテムインターフェース
# 継承：AbcItem
class LinkItem(AbcItem):
# <a></a>

    def __init__(self, caption, url):
        super().__init__(caption)
        self.url = url

# リストアイテムインターフェース
# 継承：AbcItem
class ListItem(AbcItem):
# <li></li>
    def __init__(self, caption):
        super().__init__(caption)
        self.items = []

    def add(self, item):
        self.items.append(item)

# Factoryインターフェース
class Factory(ABC):

    @abstractmethod
    def create_page_item(self, title, author):
        pass

    @abstractmethod
    def create_link_item(self, caption, url):
        pass

    @abstractmethod
    def create_list_item(self, caption):
        pass
