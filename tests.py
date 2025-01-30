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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_limit_str_books(self):
        collector = BooksCollector()
        valid_book_name = 'Дартаньян и три мушкетера'
        collector.add_new_book(valid_book_name)
        assert len(valid_book_name) < 40

    def test_add_new_book_exist_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дартаньян и три мушкетера. Тридцать лет спустя')
        collector.add_new_book('Дартаньян и три мушкетера. Тридцать лет спустя')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Роман')
        assert collector.get_book_genre('Преступление и наказание') == 'Роман'

    def test_get_book_genre_genre_on_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Кубок огня')
        collector.set_book_genre('Гарри Поттер и Кубок огня', 'Фэнтези')
        assert collector.get_book_genre('Гарри Поттер и Кубок огня') == 'Фэнтези'



