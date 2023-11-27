## Задание
### Реализовать Django + Stripe API бэкенд

Список технологий: Python, Django, DRF, Stripe,Docker
 
## Подготовка и запуск проекта
#### Проверьте установлен ли у вас Docker
Прежде, чем приступать к работе, необходимо знать, что Docker установлен. Для этого достаточно ввести:
```bash
docker -v
```
Или скачайте [Docker Desktop](https://www.docker.com/products/docker-desktop) для Mac или Windows. [Docker Compose](https://docs.docker.com/compose) будет установлен автоматически. В Linux убедитесь, что у вас установлена последняя версия [Compose](https://docs.docker.com/compose/install/). Также вы можете воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).

#### Шаг 1. Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/Stripe_test.git
```
#### Шаг 2. Создайте в клонированной директории stripetest файл .env можете использовать эти данные
Пример:
```bash

DB_ENGINE=django.db.backends.postgresql
DB_NAME=stripetest
DB_USER=postgres
DB_PASSWORD=zhenya
DB_HOST=localhost
DB_PORT=5432
STRIPE_API_KEY=sk_test_51OGlf1EQj5G4dxj6u8HhkKPVM85T0kdNaOvGhL8UTUif9UIyzdFd7LlYVfP9DmAMNkj2eooXmQDOxMbEbPbb9WzI00NibA7Lsj
```
Запуск с помощью Docker
#### Для пересборки и запуска контейнеров
```bash
    docker-compose up --build -d 

```
#### Для создания суперюзера
```bash
    1 docker  ps 
    2 docker-compose run web_app python manage.py createsuperuser
```
Запуск локально

#### Шаг 1. Для создания и активации виртуального окружения:
```python
    python -m venv venv

    venv\Scripts\activate - для Windows;
    
    source venv/bin/activate - для Linux и MacOS
```
#### Шаг 2.Создаем и применяем миграции:
```python
    python manage.py makemigrations
    python manage.py migrate
```
#### Шаг 3.Устанавливаем все зависимости:
```python
    pip install -r requirements.txt
```