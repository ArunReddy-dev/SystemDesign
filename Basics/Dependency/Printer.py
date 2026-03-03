class Printer:
    def printDocument(self, document):
        print("Title: " + document.getTitle())
        print("Content: " + document.getContent())