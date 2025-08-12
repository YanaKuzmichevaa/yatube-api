# YATUBE API

## Описание проекта:
API для социальной сети Yatube. Что можно делать в этом API:
* Создавать и публиковать собственные посты
* Просматривать посты других пользователей
* Комментировать посты пользователей
* Подписываться на других людей

*В чём польза?*

**Это полноценный backend для социальной сети с подписками, постами и комментариями!**

## Установка:
**1. Клонируйте репозиторий на своё устройство в рабочую папку**
```  
git clone https://github.com/yourusername/api-final-yatube.git
```
**2. Перейдите в этот репозиторий в командной строке**
```
cd api-final-yatube
```
**3. Создайте виртуальное окружение** 
* Для Windows
```
python -m venv venv
```
* Для Linux/macOS
```
python3 -m venv venv
```
**4. Активируйте виртуальное окружение**
* Для Windows
```
source venv/Scripts/activate
```
* Для Linux/macOS
```
source env/bin/activate
```
**5. Обновите пакетный менеджер pip**
```
python -m pip install --upgrade pip
```
или 
```
python3 -m pip install --upgrade pip
```
**6. Установите зависимости из файла requirements.txt**
```
pip install -r requirements.txt
```
**7. Выполните миграции**
```
python manage.py migrate
```
**8. Запустите проект**
```
python manage.py runserver
```

### Стек технологий:
* Python 3.12
* Django
* Django Rest Framework
* Djoser
* PyJWT

### Спецификация API
Находится в файле `yatube_api/static/redoc.yaml`

#### Автор проекта
Проект разработан: Яна (https://github.com/YanaKuzmichevaa)