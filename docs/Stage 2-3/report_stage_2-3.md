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
