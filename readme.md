### About
This project is just a getting-to-know flask, gunicorn and waitress.

***Flask*** is used to run a local development server.

### Running Flask
- make a .venv and install the packages
- Then execute the command:
    - `export FLASK_APP='app.main.create_app'` for unix
    - `$env:FLASK_APP="app/main.py"` for windows

- Then execute `flask run`

### Running a WSGI server
We use different frameworks between windows and unix.

-  `waitress-serve --host 127.0.0.1 --call app:create_app` for Window
-  `gunicorn --workers=2 app/main/create_app` for Unix

Go to an internet browser and surf to `localhost:8080` (or the port that is printed to the terminal)