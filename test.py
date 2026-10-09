import pytest
from main import BooksCollector

class TestBooksCollector:
    
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_books_genre()

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])        
    def test_set_book_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', genre)
        assert collector.get_book_genre('Гарри Поттер') == genre 
    
    
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        
        genre = collector.get_book_genre('Гарри Поттер')
        assert genre == 'Фантастика'
        
    @pytest.mark.parametrize('name', ['Приключения Шерлока Холмса', 'Лунный камень'])
    def test_get_books_with_specific_genre(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Детективы')
        
        book = collector.get_books_with_specific_genre('Детективы')
        assert book == [name]
            
        
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        
        collector.get_books_genre()
        assert collector.get_books_genre != None 
        
    @pytest.mark.parametrize('name, genre', [['Том и Джери', 'Мультфильмы'], ['Друзья', 'Комедии']] )
    def test_get_books_for_children(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        
        book = collector.get_books_for_children()
        assert book == [name]
        assert genre != ['Ужасы', 'Детективы']
        
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        
        collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in collector.favorites
        
    @pytest.mark.parametrize('name', ['Гарри Поттер', 'Игра Престолов', 'Приключения Шерлока Холмса', 'Лунный камень'])
    def test_delete_book_from_favorites(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites
        
        
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.add_book_in_favorites('Приключения Шерлока Холмса')
        
        collector.get_list_of_favorites_books()
        assert 'Приключения Шерлока Холмса' in collector.favorites