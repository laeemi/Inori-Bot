# Inori-Bot
 
### Запуск
```bash
uvicorn backend.app:app --host 127.0.0.1 --port 8001
```
### Docker
1) Билд
```bash
docker-compose up
```
2) Миграции
```bash
docker-compose exec api alembic revision --autogenerate -m 'init'
docker-compose exec api alembic upgrade head
```
