# Контейнеризация на приложение с база данни

## Описание
Това е просто Python приложение, което работи с MySQL база данни. То е контейнеризирано с Docker. Приложението позволява:
- Добавяне на записи (име и възраст)
- Извеждане на всички записи
- Изтриване на записи по идентификатор

## Файлове в репозиторията
- `app.py`: Основният код на приложението
- `Dockerfile`: Файл за изграждане на Docker образа за приложението
- `docker-compose.yml`: Файл за стартиране на приложението и MySQL базата данни

## Как да стартирате приложението

1. Клонирайте хранилището:
```
git clone https://github.com/TeodorManahilov/containerized-app-with-db.git
cd <repo_name>
```

Стартирайте Docker контейнерите:
```
docker-compose up --build
```

Влезте в контейнера на приложението:
```
docker exec -it python_app sh
```

Напишете следните Python команди в контекста на контейнера:
```
python app.py add Ivan 25
python app.py list
python app.py delete 1
```

За достъп до базата данни:
```
docker exec -it mysql_db mysql -uuser -ppassword app_db
```
