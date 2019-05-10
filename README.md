Movies
======

Installation
------------

1. Create virtualenv:

    ```
    python3 -m venv /path/to/new/virtual/environment
    ```

2. Install requirements:

    ```
    pip install -r requirements.txt
    ```

3. Execute server:

    ```
    python app.py
    ```

4. In the browser go to:

    ```
    http://127.0.0.1:8080/
    ```


Testing and coverage
--------------------

Execute:

    coverage run -m pytest


Report:

    coverage report
