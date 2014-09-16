#!/bin/bash

mysqladmin -u dev -pg0ldyl0ck$ drop mhealthcarev2
mysqladmin -u dev -pg0ldyl0ck$ create mhealthcarev2


./manage.py syncdb  --noinput
./manage.py migrate
./manage.py createsuperuser


./manage.py loaddata apps/users/fixtures/groups.json
./manage.py loaddata apps/users/fixtures/permission.json
./manage.py loaddata apps/users/fixtures/auth_user.json
./manage.py loaddata apps/users/fixtures/profile.json
./manage.py loaddata apps/users/fixtures/payments.json
./manage.py loaddata apps/ir_messages/fixtures/messages.json

./manage.py loaddata apps/geolocation/fixtures/bd/country.json
./manage.py loaddata apps/geolocation/fixtures/bd/division.json
./manage.py loaddata apps/geolocation/fixtures/bd/district.json
./manage.py loaddata apps/geolocation/fixtures/india/country.json
./manage.py loaddata apps/geolocation/fixtures/india/division.json
./manage.py loaddata apps/geolocation/fixtures/india/district.json
./manage.py loaddata apps/geolocation/fixtures/india/region.json
./manage.py loaddata apps/geolocation/fixtures/uk/country.json
./manage.py loaddata apps/geolocation/fixtures/uk/division.json
./manage.py loaddata apps/geolocation/fixtures/uk/district.json
./manage.py loaddata apps/geolocation/fixtures/uk/region.json
./manage.py loaddata apps/geolocation/fixtures/uk/ethnicity.json
./manage.py loaddata apps/prms/fixtures/tests.json
./manage.py loaddata apps/prms/fixtures/thresholds.json
./manage.py loaddata apps/prms/fixtures/diseases.json
./manage.py loaddata apps/prms/fixtures/diagnosis.json

./manage.py loaddata apps/users/fixtures/transactions.json

./manage.py loaddata apps/prms/fixtures/patients.json  ## To Insert the Patient Thresholds

./manage.py loaddata apps/prms/fixtures/thc_packages.json

./manage.py loaddata apps/ir_alerts/fixtures/alerts.json
./manage.py loaddata apps/ir_messages/fixtures/messages.json

./manage.py loaddata apps/prms/fixtures/demo/investigation.json
./manage.py loaddata apps/prms/fixtures/demo/test_option.json
./manage.py loaddata apps/prms/fixtures/demo/patient_option.json


./manage.py loaddata apps/questionnaire/fixtures/question_types.json
./manage.py loaddata apps/questionnaire/fixtures/questions.json
./manage.py loaddata apps/questionnaire/fixtures/questionXquestion_set.json
./manage.py loaddata apps/questionnaire/fixtures/question_answers.json
./manage.py loaddata apps/questionnaire/fixtures/answers.json

