import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=None, book_list=None):
        #init method with 3 req, and 2 optional attributes
        self.name = name
        self.email = email
        self.num_books = num_books if num_books is not None else 0
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name': [], 'book_rating': []})
        
    def add_book(self, book_name, book_rating):
        if self.book_list is None:
            self.book_list = pd.DataFrame(columns=['book_name', 'book_rating'])
    
        if (self.book_list['book_name'] == book_name).any():
            print(f"'{book_name}' is already added to the list")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
            })
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        self.num_books += 1
            
    def has_read(self, book_name):
        #compares given book name to names in book list
        if (self.book_list['book_name'].str.lower() == book_name.lower()).any():
            return True
        else:
            return False
        
    def num_books_read(self):
        return len(self.book_list)

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]