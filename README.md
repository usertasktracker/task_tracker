#### Установка пакетов
```
sudo apt-get install python-dev python-pip
sudo pip install pip --upgrade
sudo pip install -r requirements.txt
```

#### Настройка базы данных
```
sudo add-apt-repository "deb https://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main"
sudo apt-get update
sudo apt-get install postgresql-9.6 postgresql-9.6-plv8 postgresql-contrib-9.6 postgresql-plpython-9.6
```
```
sudo -u postgres psql
create user task_tracker with password 'sjSejdDews';
create database task_tracker WITH OWNER = task_tracker;
\q;
```
```
python manage.py migrate
```

#### Запуск через devserver
```
python manage.py runserver
```

#### Запуск тестов
```
sudo ./tests/tests.sh
```
