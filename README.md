WikiSummary
Сервис для парсинга статей с Wikipedia и генерации краткого содержания через GPT.

Как запустить проект
Склонируй репозиторий (или просто скачай папку):
git clone https://github.com/uldiniumGit/wikisummary.git
cd wikisummary

Установи зависимости
Убедись, что у тебя установлен Python 3.10+
Затем установи зависимости:
pip install -r requirements.txt

Настрой переменные окружения
Создай файл .env в корне проекта и добавь в него:
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/wiki
OPENAI_API_KEY=твой ключ
Замени логин/пароль и ключ на свои данные

Создай базу данных wiki в PostgreSQL
Можно через psql:
createdb wiki

Запусти приложение:
uvicorn app.main:app --reload

Открой в браузере http://localhost:8000/docs — там интерфейс для работы с API.

Доступные эндпоинты
POST /api/parse/ — запускает парсинг статьи по ссылке
POST /api/summary/ — генерирует summary для основной статьи
