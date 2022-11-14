## Звіт до 11 етапу

#### REST web-сервіси + HATEOAS

REST web-сервіси реалізовані на фреймворку FastAPI. Ієрархічна структура має наступний вигляд: /database/{databaseId}/table/{tableId}. Реалізований REST API сервер, HTTP-запити протестовані у Postman.

Архітектурні обмеження для REST-додатків реалізовані за допомогою методу [hateoas_links()](https://github.com/krispycrem/IT/blob/main/img/Stage%2011/hateoas.png), який повертає дозволені операції для бази даних та таблиці залежно від того, чи існують вони. 
