class Document:

    def __init__(self, title: str, content: str, pages: int) -> None:
        self.__title = title
        self.__content = content
        self.__pages = pages

    def get_title(self) -> str:
        return self.__title

    def get_content(self) -> str:
        return self.__content

    def get_pages(self) -> int:
        return self.__pages

# printer class(depends on document class) - Dependency

class Printer:

    def __init__(self, printer_name: str, printer_type: str) -> None:
        self.__printer_name = printer_name
        self.__printer_type = printer_type


    def print_document(self, document: Document) -> None:

        print(f"\n {'='*50}")
        print(f"Printer : {self.__printer_name}, Type: {self.__printer_type}")
        print(f"\n {'='*50}")
        print(f"Printing Document: {document.get_title()}")
        print(f"total pages: {document.get_pages()}")
        print(f"Content: {document.get_content()}")
        print(f"\n {'='*50}")

    def get_printer_details(self) -> str:
        return f"Printer Name: {self.__printer_name}, Printer Type: {self.__printer_type}"


doc1 = Document("Python Basics", "This is a document about Python basics.", 10)
doc2 = Document("Advanced Python", "This is a document about advanced Python topics.", 15)

office_printer = Printer("HP LaserJet", "Laser")
office_printer.print_document(doc1)
office_printer.print_document(doc2)

print(f"doc1 title: {doc1.get_title()}, doc2 title: {doc2.get_title()}")