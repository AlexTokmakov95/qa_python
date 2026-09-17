from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books_books_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2
    
    def test_set_book_genre_set_know_genre_book_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы'}

    def test_get_book_genre_know_book_get_genre_done(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.get_book_genre('Гордость и предубеждение и зомби')

        assert collector.books_genre.get('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_know_genre_get_book_done(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        books_with_genre = collector.get_books_with_specific_genre('Ужасы')
        assert 'Гордость и предубеждение и зомби' in books_with_genre

    def test_get_books_for_children_add_two_books_one_book_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')

        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 1 and 'Что делать, если ваш кот хочет вас убить' in books_for_children

    def test_add_book_in_favorites_add_one_book_book_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')  
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_one_book_book_deleted(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')  
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert collector.get_list_of_favorites_books() == []

    def test_get_books_genre_get_list_books_genre_list_geted(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы'}



    @pytest.mark.parametrize('name', ['Я','Он','Дети завтрашнего дня','Дети завтрашнего дняПиксельпутеводитель','Компания с ограниченной ответственностью']) 
    def test_add_new_book_positive_input_name_with_different_number_characters(self, collector, name):
        collector.add_new_book(name)
        
        assert len(collector.get_books_genre()) == 1

