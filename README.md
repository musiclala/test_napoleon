https://hub.docker.com/repository/docker/musiclala/napoleon_test/general

Запуск проекта:
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

Endpoints: curl/postman/

- users/ - список всех зарегистрировавшихся пользователей;
- users/<int> - определенный пользователь;
- users/reg/ - регистрация пользователя;
- users/update/<int> - обновление определенного пользователя;

- companies/ - список всех компаний с пользователями;
- companies/create/ - создание организации.

Не стал использовать .env для одного секретного ключа.
