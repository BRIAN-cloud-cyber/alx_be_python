class Book:
    books=[]
    def __init__(self,title:str,author:str):
        self.title=title
        self.author=author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
        
class Ebook(Book):
    def __init__(self,file_size:int,title:str,author:str):
        super().__init__(title,author)
        self.size=file_size
    def __str__(self):
        return f"{self.title} by {self.author},File Size: {self.file_size}KB"
    
class PrintBook(Book):
    def __init__(self,page_count:int,title:str,author:str):
        super().__init__(title,author)
        self.count=page_count
    def __str__(self):
        return f"{self.title} by {self.author},Page Count:{self.count}"
class Library:
    def add_books(self,book,books):
        self.books=books
        self.books=[]
        if isinstance(book,Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book,EBook,or PrintBook can be added")
        
    def List_books(self):
        for book in self.books:
            print(book)

def main():
    my_library=Library() #library instance
    classic_book=Book("Pride and Prejudice","Jane Austen")
    digital_book=Ebook("Snow Crash","Neal Stephenson",500)
    paper_novel=PrintBook("The Catcher in the Rye","J.D.Salinger",2024)

    # add books to the library

    my_library.add_books(classic_book)
    my_library.add_books(digital_book)
    my_library.add_books(paper_novel)

    #list books
    my_library.List_books()

if __name__=="__main__":
    main()
    