set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input

if [[$CREATE_SUPERUSER]];
then
    python manage.py createsuperuser --email getu@gmail.com --password getu1234

fi    

python manage.py migrate