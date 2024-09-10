1) Установите Python, если его нет

1) Скопируйте папку с проектом Avitotest на диск C: (полный путь будет: C:\Avitotest).

1) Откройте командную строку: (Win + R) выполните команду cmd

1) Установите необходимые библиотеки:

`	`pip install greenlet

`	`pip install playwright

`	`pip install pytest

`	`pip install pytest-playwright

1) Чтобы перейти в папку проекта, выполните команду в командной строке:

`	`cd C:\Avitotest

1) Для создания виртуальной среды выполните следующие команды в командной строке:

`	`python -m venv venv

.\venv\Scripts\activate

1) Установите все необходимые зависимости для работы проекта, прописав в терминале:



`	`pip install -r requirements.txt

1) Запустите тесты, прописав в консоли:

`	`pytest test\_avito.py
