class Document:
    def __init__(self, title, content):
        self.__title = title
        self.___content = content
    def getTitle(self):
        return self.__title
    def getContent(self):
        return self.___content 