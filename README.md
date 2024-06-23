# Загрузка проекта
1. Клонируйте проект на собственный компьютер:
```
git clone https://github.com/GasilinEgor/Educational-Games-WebSite.git
```
2. Создайте виртуальное окружение и загрузите зависимости:
## Для Windows:
1) Для стабильной загрузки и работы с проектом рекомендуется выполнять следующие компанды в среде разработке (Например Pycharm)
2) Создайте виртуальное окружение и загрузите зависимости:
```
python -m venv .venv
.venv\Scripts\activate.bat
pip3 install -r requirements.txt
```
## Для Linux:
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
3. Выполните миграции БД
```
python manage.py makemigrations
python manage.py migrate
```
4. Запустите сервер
```
python manage.py runserver
```
