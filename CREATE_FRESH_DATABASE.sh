mysqladmin -u root -proot drop mhealthcarev2
mysqladmin -u root -proot create mhealthcarev2

find -type d -name 'migrations' -exec rm -rfv {} \;

python manage.py syncdb  --noinput
python manage.py migrate

python manage.py syncdb 


