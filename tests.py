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

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == 'Оно'

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец. Братство кольца')
        collector.set_book_genre('Властелин колец. Братство кольца', 'Фэнтези')
        collector.add_new_book('Властелин колец. Две крепости')
        collector.set_book_genre('Властелин колец. Две крепости', 'Фэнтези')
        collector.add_new_book('Властелин колец. Возвращение короля')
        collector.set_book_genre('Властелин колец. Возвращение короля', 'Фэнтези')
        expect={'Властелин колец. Братство кольца':'Фэнтези',
                'Властелин колец. Две крепости':'Фэнтези',
                'Властелин колец. Возвращение короля':'Фэнтези'}
        assert collector.get_books_genre() == expect

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гремлины')
        collector.set_book_genre('Гремлины', 'Ужасы')
        collector.add_new_book('Морозко')
        collector.set_book_genre('Морозко', 'Сказка')
        collector.add_new_book('Простоквашино')
        collector.set_book_genre('Простоквашино', 'Детские приключения')
        books_for_children = collector.get_books_for_children()
        expect=['Морозко', "Простоквашино"]
        assert books_for_children == expect

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Темная башня')
        collector.set_book_genre('Темная башня', 'Фэнтези')
        collector.add_book_in_favorites('Темная башня')
        assert 'Темная башня' in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Луна 84')
        collector.set_book_genre('Луна 84', 'Фантастика')
        collector.add_book_in_favorites('Луна 84')
        collector.delete_book_from_favorites('Луна 84')
        assert 'Луна 84' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Добрый предзнаменовения')
        collector.set_book_genre('Добрый предзнаменовения', 'Фэнтези')
        collector.add_book_in_favorites('Луна 84')
        assert'Добрый предзнаменовения' in collector.get_list_of_favorites_books()










