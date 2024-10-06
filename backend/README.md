Инструкция 

Вместо файла test.log в папке files положите свой с таким же названием (test.log)

1 Вариант запуска (На unix системе (Linux), Рекомендуется python 3.10)
1) Создать виртуальное окружение: python3 -m venv .venv
2) Запустить его: source .venv/bin/activate
3) Установить все библиотеки: pip install -r requirements.txt
4) Запустить командой: uvicorn main:app --reload


2 Вариант запуска (В докере)
1) Создать образ: docker build -t logs_backend .
2) Запустить: docker run -dp 127.0.0.1:8000:8000 logs_backend
3) Для остановки (все контейнеры остановит): docker stop $(docker ps -a -q)
4) Для удаления (все контейнеры удалит): docker rm $(docker ps -a -q)