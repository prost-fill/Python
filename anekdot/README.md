# Парсер анекдотов с anekdot.ru

Программа для получения случайных анекдотов с сайта anekdot.ru.

## Установка и запуск

### Вариант 1: Ручная установка
```bash
# Клонировать репозиторий
git clone <url-репозитория>
cd anekdot

# Создать виртуальное окружение
python3 -m venv venv

# Активировать виртуальное окружение
source venv/bin/activate  # для Linux/Mac
# или venv\Scripts\activate  # для Windows

# Установить зависимости
pip install -r requirements.txt

# Запустить программу
python anek.py