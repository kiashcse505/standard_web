#!/bin/bash

mysqladmin -u dev -pg0ldyl0ck$ drop mhealthcarev2
mysqladmin -u dev -pg0ldyl0ck$ create mhealthcarev2


./../manage.py syncdb  --noinput
./../manage.py migrate
./../manage.py createsuperuser

./../manage.py schemamigration prms --initial
./../manage.py schemamigration users --initial
./../manage.py schemamigration wisys --initial
./../manage.py schemamigration messages --initial
./../manage.py schemamigration geolocation --initial
./../manage.py schemamigration questionnaire --initial
./../manage.py schemamigration ir_alerts --initial
./../manage.py schemamigration mpayment --initial


./../manage.py migrate prms 0001 --fake
./../manage.py migrate users 0001 --fake
./../manage.py migrate wisys 0001 --fake
./../manage.py migrate messages 0001 --fake
./../manage.py migrate geolocation 0001 --fake
./../manage.py migrate questionnaire 0001 --fake
./../manage.py migrate ir_alerts 0001 --fake
./../manage.py migrate mpayment 0001 --fake


./../manage.py loaddata ../apps/users/fixtures/groups.json
./../manage.py loaddata ../apps/users/fixtures/permission.json
./../manage.py loaddata ../apps/users/fixtures/auth_user.json
./../manage.py loaddata ../apps/users/fixtures/profile.json
./../manage.py loaddata ../apps/users/fixtures/payments.json
./../manage.py loaddata ../apps/ir_messages/fixtures/messages.json
./../manage.py loaddata ../apps/ir_alerts/fixtures/alerts.json
./../manage.py loaddata ../apps/geolocation/fixtures/all_bd.json
./../manage.py loaddata ../apps/prms/fixtures/diseases.json
./../manage.py loaddata ../apps/prms/fixtures/options.json
./../manage.py loaddata ../apps/users/fixtures/transactions.json