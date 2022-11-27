### Лабораторна робота "Фрагментарна реалізація систем управління табличними базами даних"
# Зміст

- [Умова лабораторної роботи](#desc)
- [0 етап](#0stage)
- [1 етап](#1stage)
- [2-3 етап](#2-3stage)
- [10 етап](#10stage)
- [11 етап](#11stage)
- [12 етап](#12stage)
- [13 етап](#13stage)
- [14 етап](#14stage)
- [20 етап](#20stage)
- [24 етап](#24stage)
- [27 етап](#27stage)


<a name = "desc"></a>
## Умова лабораторної роботи

І. Загальні вимоги

Основні вимоги щодо структури бази:

- кількість таблиць принципово не обмежена (реляції між таблицями не враховувати);
- кількість полів та кількість записів у кожній таблиці також принципово не обмежені.

У кожній роботі треба забезпечити підтримку (для полів у таблицях) наступних (загальних для всіх варіантів!) типів:

- integer
- real
- char
- string

Також у кожній роботі треба реалізувати функціональну підтримку для:

- створення бази
- створення (із валідацією даних) та знищення таблиці з бази
- перегляду та редагування рядків таблиці
- збереження табличної бази на диску та, навпаки, зчитування її з диску

ІІ. Варіанти додаткових типів

- color (RGB код кольору); colorInvl (інтервальний тип)

ІІІ. Варіанти додаткових операцiй над таблицями

- вилучення повторюваних рядкiв у таблиці

<a name = "0stage"></a>
## 0 етап 

[**_UseCase.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%200/UseCase.png)  - UML діаграма прецедентів, яка призначена для проектування та специфікації програмних систем.

<a name = "1stage"></a>
## 1 етап

12 UML діаграм до лабораторної роботи призначені для проектування та специфікації програмних систем:

- [**_Class diagram.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/Class%20diagram.png) містить діаграму класів. Містить класи "Table", "Database", "Column",  також "AbstractRestController" та його видозміни ("TableManagementRestController", "ReadWriteTableRestController", "DataManagementRestController").
- [**_Components.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/Components.png) містить діаграму компонентів для розподіленої системи.
- [**_Sequence_Сreate_from_file.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/Sequence_Create_from_file.png) - діаграма послідовностей для створення бази даних з файлу.
- [**_Sequence_Edit_Value.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/Sequence_Edit_Value.png) - діаграма послідовностей для редагування значень в таблиці.
- [**_Sequence_deduplicate.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/Sequence_deduplicate.png) - діаграма послідовностей для видалення повторюваних рядків.
- [**_Sequence_diagr_fetch.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/Sequence_diagr_fetch.png) - діаграма послідовностей для витягування всіх таблиць.
- [**_Sequence_save_to_drive.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/Sequence_save_to_drive.png) - діаграма послідовностей для збереження бази даних у файл.
- [**_Sequence_table_create.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/Sequence_table_create.png) - діаграма послідовностей для створення таблиці у базі даних. 
- [**_UseCase.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/UseCase.png) - діаграма прецедентів. 
- [**_VOPC_Class.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/VOPC_Class.png) - VOPC-діаграма для створення таблиці. 
- [**_VOPC_deduplication.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/%20VOPC_dediplication.png) - VOPC-діаграма для видалення повторюваних рядків у таблиці.
- [**_Deployment_diagram.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/Deployment_diagram.png) - діаграма розгортання. 
- [**_Flow_of_events.txt_**](https://github.com/krispycrem/IT/blob/main/img/Stage%201/Flow_of_events.txt) - до трьох прецедентів (створення бази даних, вилучення повторюваних рядків, створення бази даних з файлу) описано потоки подій.

<a name = "2-3stage"></a>
## 2-3 етап

Було розроблено класи "Table", "Database" та "TableColumn" для понять "Таблиця", "База даних" та "Колонка таблиці" (папка models в структурі проєкту).
Також було додано UML-діаграму класів _Class_diagram.png_. У папці test_dedup знаходяться три Unit-тести, для вилучення повторюваних рядків таблиці, 
зокрема для перевірки рядків на рівність та знаходження повторюваних рядків за ідентифікатором. 
Інтерфейс користувача забезпечується за допомогою реалізованої фронтенд-частини. 
Операції, реалізовані у фронтенд частині:
- [Створення БД](https://github.com/krispycrem/IT/blob/main/img/Stage%202-3/createdb.png)
- [Створення таблиці](https://github.com/krispycrem/IT/blob/main/img/Stage%202-3/createtable.png)
- [Додавання рядка](https://github.com/krispycrem/IT/blob/main/img/Stage%202-3/addrow.png)
- [Дедуплікація рядків](https://github.com/krispycrem/IT/blob/main/img/Stage%202-3/deduptable.png)
- [Перегляд та редагування таблиці](https://github.com/krispycrem/IT/blob/main/img/Stage%202-3/view_and_edit_table.png)
- [Отримання даних з БД](https://github.com/krispycrem/IT/blob/main/img/Stage%202-3/getdump.png)
- [Відтворення БД з даних](https://github.com/krispycrem/IT/blob/main/img/Stage%202-3/create_from_dump.png)

HTTP-запити протестовані у [Postman](https://github.com/krispycrem/IT/blob/main/img/Stage%202-3/Postman.png). 

<a name = "10stage"></a>
## 10 етап

#### REST web-сервіси. 

REST web-сервіси реалізовані на фреймворку FastAPI. Ієрархічна структура має наступний вигляд: /database/{databaseId}/table/{tableId}. Реалізований REST API сервер, HTTP-запити протестовані у Postman.

<a name = "11stage"></a>
## 11 етап

#### REST web-сервіси + HATEOAS

REST web-сервіси реалізовані на фреймворку FastAPI. Ієрархічна структура має наступний вигляд: /database/{databaseId}/table/{tableId}. Реалізований REST API сервер, HTTP-запити протестовані у Postman.

Архітектурні обмеження для REST-додатків реалізовані за допомогою методу [**_hateoas_links()_**](https://github.com/krispycrem/IT/blob/main/img/Stage%2011/hateoas.png), який повертає дозволені операції для бази даних та таблиці залежно від того, чи існують вони. 

<a name = "12stage"></a>
## 12 етап

#### REST web-сервіси. Розробка OpenAPI Specification для взаємодії з ієрархічними даними (база, таблиця, ...).

REST web-сервіси реалізовані на фреймворку FastAPI. Ієрархічна структура має наступний вигляд: /database/{databaseId}/table/{tableId}. Реалізований REST API сервер, HTTP-запити протестовані у Postman.

Файл openapispec.yaml був створений для генерації стабу серверної частини додатка. 

<a name = "13stage"></a>
## 13 етап

#### REST web-сервіси. Реалізація серверного проєкту, використовуючи кодогенерацію стабу за OpenAPI Specification.

REST web-сервіси реалізовані на фреймворку FastAPI. Ієрархічна структура має наступний вигляд: /database/{databaseId}/table/{tableId}. Реалізований REST API сервер, HTTP-запити протестовані у Postman. 

Використовуючи інтерфейс OpenAPI, було згенеровано [загальну структуру проекту](https://github.com/krispycrem/IT/blob/main/img/Stage%2013/openapi_spec.png). 

<a name = "14stage"></a>
## 14 етап

#### REST web-сервіси. Реалізація клієнтського проєкту за OpenAPI Specification.

REST web-сервіси реалізовані на фреймворку FastAPI. Ієрархічна структура має наступний вигляд: /database/{databaseId}/table/{tableId}. Клієнтський проект був написаний за допомогою swagger документації серверної частини додатку. Для написання клієнтської частини був використаний фреймворк React. 

<a name = "20stage"></a>
## 20 етап

#### Web-проект із використанням AJAX. Щонайменше повинно забезпечуватись часткове перезавантаження web-сторінки.

В основі підходу до побудови користувацьких інтерфейсів AJAX покладена ідея надсилання веб-сторінкою запитів на сервер у фоновому режимі і довантажування користувачу необхідних даних. 

<a name = "24stage"></a>
## 24 етап

#### Варіант проєкту із використанням реляційної СУБД (замість використання серіалізації об'єктів для збереження даних).

Проєкт реалізований з використанням класів "Таблиця" (table.py), "Колонка" (table_columns.py), "База даних" (database.py), з відношенням "один до багатьох". Уси три файли розташовані у папці проєкту *models*. Функціонал був реалізований на сонові попередньо створених Use-Case діаграм.

<a name = "27stage"></a>
## 27 етап 

#### Інтегроване (Mock-) тестування у проєктах, що використовують реальні СУБД (реляційні чи ні) для збереження даних.

Реалізовані інтеграційні тестування:
- додавання рядка (_test_add_row()_)
- створення бази даних (_test_database_create_post()_)
- створення однакової бази даних (_test_same_database_creation()_)
- створення таблиці (_test_create_table_for_existing_db()_)
- видалення повторюваних рядків таблиці (_test_dedup()_)
- видалення таблиці (_test_delete_table()_)
- редагування рядка таблиці (_test_edit_value())
- редагування інтервалу інтервалу кольорів (test_edit_value_range())
- редагування значення кольору (test_edit_value_color())

За успішного реалізації повертається код 201.
