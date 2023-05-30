# Questions

В сервисе реализован POST REST метод,
принимающий на вход запросы с содержимым вида {"questions_num": integer}.

После получения запроса происходит обращение к внешнему API для загрузки
указанного количества вопросов в локальную БД.

Ответом на запрос является запись в БД о последнем сохраненном вопросе.

## Функционал

- Реализация проекта на django
- Реализация API на django rest framework
- Реализация класса для взаимодействия с внешним API и реализация адаптера
для интеграции с внутренней бизнес - логикой
- Реализация выполнения фоновых задач общения с API с использованием Celery
- Разделение Бизнес логики и интерфейса пользователя. Единый вход через
сервисный слой.
- Запуск проекта в Docker

## Сборка

Для запуска проекта скопируйте папку проекта в локальную среду, и из папки
проекта запустите сборку командой

```sh
docker compose up -d --build
```

После первого запуска будет создана чистая БД из образа PostgreSQL, в которой
необходимо применить миграции проекта командой

```sh
docker compose exec questions python manage.py makemigrations
```

При дальнейшем использовании БД будет храниться на локальной машине и не будет
сбрасываться при перезапуске контейнеров.

## Использование

- API

адрес /api/v1/

схема API прописана в файле openapi-schema.yml в корне проекта