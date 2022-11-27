### Лабораторна робота "Фрагментарна реалізація систем управління табличними базами даних"

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

V. Завдання лабораторного практикуму

- [0 Етап](https://github.com/krispycrem/IT/blob/main/docs/Stage%200/report_stage_0.md)
- [1 Етап](https://github.com/krispycrem/IT/blob/main/docs/Stage%201/report_stage_1.md)
- [2-3 Етап](https://github.com/krispycrem/IT/tree/main/docs/Stage%202-3)
- [10 Етап](https://github.com/krispycrem/IT/tree/main/docs/Stage%2010)
- [11 Етап](https://github.com/krispycrem/IT/tree/main/docs/Stage%2011)
- [12 Етап](https://github.com/krispycrem/IT/tree/main/docs/Stage%2012)
- [13 Етап](https://github.com/krispycrem/IT/tree/main/docs/Stage%2013)
- [14 Етап](https://github.com/krispycrem/IT/tree/main/docs/Stage%2014)
- [20 Етап](https://github.com/krispycrem/IT/tree/main/docs/Stage%2020)
- [24 Етап](https://github.com/krispycrem/IT/tree/main/docs/Stage%2024)
- [27 Етап](https://github.com/krispycrem/IT/tree/main/docs/Stage%2027)

## Звіт до 0 етапу 

[**_UseCase.png_**](https://github.com/krispycrem/IT/blob/main/img/Stage%200/UseCase.png)  - UML діаграма прецедентів, яка призначена для проектування та специфікації програмних систем.

## Звіт до 1 етапу 

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

## Звіт до 2-3 етапу 

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

## Звіт до 10 етапу 

#### REST web-сервіси. 

REST web-сервіси реалізовані на фреймворку FastAPI. Ієрархічна структура має наступний вигляд: /database/{databaseId}/table/{tableId}. Реалізований REST API сервер, HTTP-запити протестовані у Postman.

## Звіт до 11 етапу

#### REST web-сервіси + HATEOAS

REST web-сервіси реалізовані на фреймворку FastAPI. Ієрархічна структура має наступний вигляд: /database/{databaseId}/table/{tableId}. Реалізований REST API сервер, HTTP-запити протестовані у Postman.

Архітектурні обмеження для REST-додатків реалізовані за допомогою методу [**_hateoas_links()_**](https://github.com/krispycrem/IT/blob/main/img/Stage%2011/hateoas.png), який повертає дозволені операції для бази даних та таблиці залежно від того, чи існують вони. 

## Звіт до 12 етапу

#### REST web-сервіси. Розробка OpenAPI Specification для взаємодії з ієрархічними даними (база, таблиця, ...).

REST web-сервіси реалізовані на фреймворку FastAPI. Ієрархічна структура має наступний вигляд: /database/{databaseId}/table/{tableId}. Реалізований REST API сервер, HTTP-запити протестовані у Postman.

Файл openapispec.yaml був створений для генерації стабу серверної частини додатка. 

## Звіт до 13 етапу

#### REST web-сервіси. Реалізація серверного проєкту, використовуючи кодогенерацію стабу за OpenAPI Specification.

REST web-сервіси реалізовані на фреймворку FastAPI. Ієрархічна структура має наступний вигляд: /database/{databaseId}/table/{tableId}. Реалізований REST API сервер, HTTP-запити протестовані у Postman. 

Використовуючи інтерфейс OpenAPI, було згенеровано [загальну структуру проекту](https://github.com/krispycrem/IT/blob/main/img/Stage%2013/openapi_spec.png). 

## Звіт до 14 етапу 

#### REST web-сервіси. Реалізація клієнтського проєкту за OpenAPI Specification.

REST web-сервіси реалізовані на фреймворку FastAPI. Ієрархічна структура має наступний вигляд: /database/{databaseId}/table/{tableId}. Реалізований REST API сервер, HTTP-запити протестовані у Postman.

Файл openapispec.yaml був написаний використовуючи програму OpenAPI Generator. Клієнтський проект - це бібліотека, яку використовується в додатку, що працює на API, тобто, робить запити до API, описані у визначенні OpenAPI.

## Звіт до 20 етапу 

#### Web-проект із використанням AJAX. Щонайменше повинно забезпечуватись часткове перезавантаження web-сторінки.

В основі підходу до побудови користувацьких інтерфейсів AJAX покладена ідея надсилання веб-сторінкою запитів на сервер у фоновому режимі і довантажування користувачу необхідних даних. 

## Звіт до 24 етапу 

#### Варіант проєкту із використанням реляційної СУБД (замість використання серіалізації об'єктів для збереження даних).

Проєкт реалізований з використанням класів "Таблиця" (table.py), "Колонка" (table_columns.py), "База даних" (database.py), з відношенням "один до багатьох". Уси три файли розташовані у папці проєкту *models*. Функціонал був реалізований на сонові попередньо створених Use-Case діаграм.

## Звіт до 27 етапу 

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



