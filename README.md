# Локальная копия Реестра российской системы и плана нумерации

## Для запуска необходимо:
### Создать `.env` файл в корне репозитория с переменными:
| Parameter name            | Description                                                               |
|---------------------------|---------------------------------------------------------------------------|
| DJANGO_SETTINGS_MODULE    | Путь до settings.py                                                       |
| DJANGO_SECRET_KEY         | Секретный ключ                                                            |
| POSTGRES_DB               | Название базы данных в PostgreSQL.                                        |
| POSTGRES_USER             | Имя пользователя в БД                                                     |
| POSTGRES_PASSWORD         | Пароль пользователя в БД.                                                 |
| SUBDOMAIN_NAME            | Имя поддомена, где будет размещен проект.                                 |
| DOMAIN_NAME               | Имя домена, где будет размещен проект.                                    |
### Создать volume для хранения данных в БД: `docker volume create postgres_data`
### Заупстить Docker: `docker compose up -d`
### Выполнить миграции БД: `docker exec -it backend bash`, а затем `python3 manage.py migrate`
### Загрузить данные в БД: `docker exec -it backend bash`, а затем `python3 phone_numbers/services/download.py`