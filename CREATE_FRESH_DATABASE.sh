mysqladmin -u root -proot drop standard_web
mysqladmin -u root -proot create standard_web

find -type d -name 'migrations' -exec rm -rfv {} \;

python manage.py syncdb  --noinput
python manage.py migrate

python manage.py syncdb 


