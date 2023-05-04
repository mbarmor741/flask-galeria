# Galeria

Aplicación de ejemplo para usar en práctica Deploy de contenedor Docker en EC2 AWS.

- Lanzar la aplicación (por defecto puerto 5000)

    ```console
    (venv) alu@xdebian11:~/galeria$ python src/app.py 
    * Serving Flask app 'app'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 944-294-141
    127.0.0.1 - - [13/Feb/2023 10:30:32] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [13/Feb/2023 10:30:32] "GET /static/estilos.css HTTP/1.1" 304 -

    ``` 

- Lanzar la aplicación con `gunicorn` (por defecto puerto 8000, en otro puerto usar `--bind 0.0.0.0:5000`)

    ```console
    (venv) alu@xdebian11:~/galeria$ gunicorn --chdir src app:app --bind 0.0.0.0:5000 --reload --access-logfile -
    [2023-02-13 10:32:50 +0100] [3863] [INFO] Starting gunicorn 20.1.0
    [2023-02-13 10:32:50 +0100] [3863] [INFO] Listening at: http://0.0.0.0:5000 (3863)
    [2023-02-13 10:32:50 +0100] [3863] [INFO] Using worker: sync
    [2023-02-13 10:32:50 +0100] [3864] [INFO] Booting worker with pid: 3864
    ```

- Error al hacer buil de la imagen por problema red

    ```console
    systemctl restart NetworkManager.service
    sudo service docker restart
    ``` 

- Crear y lanzar container

    ```console
    docker build -t testing .
    docker run -dp 5000:5000  testing
    curl localhost:5000
    ``` 

