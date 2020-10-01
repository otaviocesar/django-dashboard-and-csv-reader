# CSV READER DASHBOARD


## Como rodar o projeto?

```bash
source ./venv/scripts/activate or cd ./venv/scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser or winpty python manage.py createsuperuser
python manage.py runserver 8000
```