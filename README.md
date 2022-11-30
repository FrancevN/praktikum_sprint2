# Реализованные тесты:

1. test_add_new_book_add_two_books - проверка добавления двух книг
2. test_add_new_book_add_book - проверка добавления книги
3. test_add_two_identical_books_add_one_book - проверка не возможности добавить две идентичные книги
4. test_not_rate_a_book_that_is_on_the_list_is_none - проверка невозможности выставить рейтинг книге, которой нет в списке
5. test_dont_rate_less_than_1_get_1 - проверка невозможности выставить рейтинг меньше 1
6. test_dont_rate_more_than_10_get_1 - проверка невозможности выставить рейтинг больше 10
7. test_book_not_added_has_no_rating_is_none - у не добавленной книги нет рейтинга
8. test_add_book_to_favorites_add_favorites - добавление книги в избранное
9. test_cannot_add_book_to_favorites_if_it_is_not_in_dictionary_books_rating_favorites_is_empty - нельзя добавить книгу в избранное, если её нет в словаре books_rating
10. test_book_remove_in_favorites_favorites_is_empty - Проверка удаления книги из избранного