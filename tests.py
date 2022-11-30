from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('ДРАКОНЫ')
        assert len(collector.get_books_rating()) == 1

    def test_add_two_identical_books_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('ДРАКОНЫ')
        collector.add_new_book('ДРАКОНЫ')
        assert len(collector.get_books_rating()) == 1

    def test_not_rate_a_book_that_is_on_the_list_is_none(self):
        collector = BooksCollector()
        collector.add_new_book('ДРАКОНЫ')
        assert collector.set_book_rating('Гордость и предубеждение и зомби', 5) is None

    def test_dont_rate_less_than_1_get_1(self):
        collector = BooksCollector()
        collector.add_new_book('ДРАКОНЫ')
        collector.set_book_rating('ДРАКОНЫ', 0)
        assert collector.get_book_rating('ДРАКОНЫ') == 1

    def test_dont_rate_more_than_10_get_1(self):
        collector = BooksCollector()
        collector.add_new_book('ДРАКОНЫ')
        collector.set_book_rating('ДРАКОНЫ', 11)
        assert collector.get_book_rating('ДРАКОНЫ') == 1

    def test_book_not_added_has_no_rating_is_none(self):
        collector = BooksCollector()
        assert collector.get_book_rating('ДРАКОНЫ') is None

    def test_add_book_to_favorites_add_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('ДРАКОНЫ')
        collector.add_book_in_favorites('ДРАКОНЫ')
        assert collector.favorites == ['ДРАКОНЫ']

    def test_cannot_add_book_to_favorites_if_it_is_not_in_dictionary_books_rating_favorites_is_empty(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('ДРАКОНЫ')
        assert collector.favorites == []

    def test_book_remove_in_favorites_favorites_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('ДРАКОНЫ')
        collector.add_book_in_favorites('ДРАКОНЫ')
        collector.delete_book_from_favorites('ДРАКОНЫ')
        assert collector.favorites == []
