class Book:
    def __init__(self,title:str,author:str,year:int):
        self.title=title
        self.author=author
        self.year=year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author},published in {self.year}"

    def __repr__(self):
       return f"Book('{self.title}','{self.author}','{self.year}')"

book1=Book("River Between","Ngung'i Wa Thiong'o",1998)
print(book1)
del book1
print(repr(book1))