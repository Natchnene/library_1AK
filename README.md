Приложение "библиотека" сделано с использованием языка Python и фреймворка django.

Используемые технологии:
python = "^3.11"
django = "^4.2.4"
python-dotenv = "^1.0.0"

Базы данных - SQLite. 
Путь к базе данных: library_django -> db.sqlite3

Для запуска и тестирования приложения необходимо запустить веб-сервер, для этого из консоли находясь 
в корне проекта (папка library_django, в ней лежит управляющий файл manage.py) необходимо прописать команду
python manage.py runserver и перейти в браузере на стартовую страницу по адресу http://127.0.0.1:8000/reader/get_readers/

Стартовая страница представляет собой списком читателей. Пользователь может выбрать свою фамилию из списка, 
перейти на следующую страницу и выбрать одно действие: вывести весь список книг в библиотеке, для того, что бы взять новую 
книгу или вывести список книг у читателей, что бы сдать книгу. Если фамилии в списке нет, можно создать нового пользователя.

