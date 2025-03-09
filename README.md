# Описание:
# Инструкция по запуску: 
1. Установка Python и pip

Убедитесь, что у вас установлен Python (рекомендуется версия 3.6 и выше). Вы можете проверить это, выполнив команду:

python --version

или

python3 --version


Также убедитесь, что у вас установлен pip, пакетный менеджер для Python:

pip --version


2. Скачайте проект с гитхаба

Скачайте архив с проектом и распакуйте его на рабочий стол

или

откройте командную строку и введите команды:

cd Desktop

git clone https://github.com/NazarEE127/Historical_helper.git


3. Установка виртуального окружения (опционально)

Рекомендуется создать виртуальное окружение для вашего проекта, чтобы изолировать зависимости:

Переход в папку с проектом
cd Historical_helper

Установите virtualenv, если он еще не установлен
pip install virtualenv

Создайте виртуальное окружение
virtualenv venv

Активируйте виртуальное окружение
На Windows:
venv\Scripts\activate
На macOS/Linux:
source venv/bin/activate


4. Установка зависимостей

Перейдите в каталог вашего проекта (где находится файл requirements.txt) и установите зависимости:

cd historical_helper
pip install -r requirements.txt


5. Применение миграций

Примените миграции, чтобы создать необходимые таблицы в базе данных:

python manage.py migrate


6. Создание суперпользователя (опционально)

Если вам нужна административная панель(Уже существует аккаунт админа: логин - admin, пароль - 123), создайте суперпользователя:

python manage.py createsuperuser


7. Запуск сервера разработки

Теперь вы готовы запустить сервер разработки:

python manage.py runserver

8. Откройте http://127.0.0.1:8000/ в браузере, чтобы проверить работу проекта.
