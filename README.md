## task-1
* створення venv
 **python -m venv fastapi-project**
* активації venv
  **.\fastapi-project\Scripts\Activate.ps1**
* встановлення залежностей
  **pip install fastapi**
  **pip install uvicorn[standard]**
* побудова образу **docker build**
* запуску через docker-compose **docker-compose up**
* зупинки контейнерів. **docker stop** або **docker-compose down**
* ВІДОБРАЖЕННЯ НА СТОРІНЦІ LOCALHOST: **{"status" : "ok"}**

# Запуск проєкту
* через venv: для запуску проєкту локально через віртуальне середовище необхідно: створити середовище, активувати його, встановити залежності та запустити за допомогою uvicorn.
* через docker-compose: для запуску проєкту через docker потрібно створити файл docker-compose.yml, запустити проєкт, перевірити та зупинити проєкт.
