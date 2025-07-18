@echo off
REM Ativar o ambiente virtual, se necessário
call venv\Scripts\activate.bat

REM Variáveis de ambiente
set DJANGO_SECRET_KEY=django-insecure-abc123!
set MYSQL_USER=root
set MYSQL_PASSWORD=ti@118
set MYSQL_DB_NAME=db_main
set MYSQL_HOST=127.0.0.1
set MYSQL_PORT=3306

REM Executar o servidor Waitress
python run_waitress.py
pause