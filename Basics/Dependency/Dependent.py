from Document import Document
from Printer import Printer

class Dependent:
    def __init__(self):
        doc=Document("Dependency", "This is a document about dependency.")
        printer=Printer()
        printer.printDocument(doc)

if __name__=="__main__":
    dependent=Dependent()
    