import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        greg = BookLover("greg","greg@gmail.com","Sci-Fi")
        greg.add_book("Three Body Problem", 4)
        self.assertTrue("Three Body Problem" in greg.book_list['book_name'].values)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        greg = BookLover("greg","greg@gmail.com","Sci-Fi")
        greg.add_book("Three Body Problem", 4)
        greg.add_book("Three Body Problem", 4)
        self.assertTrue(greg.book_list.len()==1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        greg = BookLover("greg","greg@gmail.com","Sci-Fi")
        greg.add_book("Three Body Problem", 4)
        self.assertTrue(greg.has_read("Three Body Problem"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        greg = BookLover("greg","greg@gmail.com","Sci-Fi")
        greg.add_book("Three Body Problem", 4)
        self.assertFalse(greg.has_read("Cat in Hat"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        greg = BookLover("greg","greg@gmail.com","Sci-Fi")
        greg.add_book("Three Body Problem", 4)
        greg.add_book("book 2", 4)
        greg.add_book("book 3", 4)
        greg.add_book("book 4", 4)
        self.assertTrue(greg.num_books_read()==4)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        greg = BookLover("greg","greg@gmail.com","Sci-Fi")
        greg.add_book("Three Body Problem", 4)
        greg.add_book("book 2", 2)
        greg.add_book("book 3", 3)
        greg.add_book("book 4", 4)
        self.assertTrue((greg.fav_books()['book_rating'] > 3).all())
        
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)