__author__ = 'irashid'

# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _


ACTIVE = 1
INACTIVE = 2
DELETED = 3
HIDDEN = 4
ARCHIVED = 5

STATUSES = (
    ( ACTIVE,   _('Active')   ),
    ( INACTIVE, _('Inactive') ),
    ( HIDDEN,   _('Hidden')   ),
    ( DELETED,  _('Deleted')  ),
    ( ARCHIVED,  _('Archived')  ),
)

ACTIVE_INACTIVE_STATUSES = (

    ( ACTIVE,   _('Active')   ),
    ( INACTIVE, _('Inactive') )

)


MALE = 1
FEMALE = 2

GENDERS = (
    ( MALE    ,_("Male")   ),
    ( FEMALE  ,_("Female") ) ,
)


# ISLAM = 1
# CHRISTIAN  = 2
# HINDU = 3
#
# RELIGION = (
#     ( ISLAM    ,_("Islam")   ),
#     ( CHRISTIAN  ,_("Christian") ) ,
#     ( HINDU  ,_("Hindu") ) ,
# )

AETHIEST = 1
BUDDHIST = 2
CHRISTIAN  = 3
HINDU = 4
ISLAM = 5
NOTDECLARED = 6
NONE = 7

RELIGION = (
    ( AETHIEST  ,_("Aethiest") ) ,
    ( BUDDHIST  ,_("Buddhist") ) ,
    ( CHRISTIAN  ,_("Christian") ) ,
    ( HINDU  ,_("Hindu") ) ,
    ( ISLAM    ,_("Islam")) ,
    ( NOTDECLARED ,_(" Not Declared")),
    ( NONE  ,_("None") ) ,
)

LEADCLINICIAN = 1
LEADCAREWORKER = 2

USER_ROLE = (
    ( LEADCLINICIAN    ,_("Lead Clinician")   ),
    ( LEADCAREWORKER  ,_("Lead Care Worker") ) ,
)


date_f0 = ''
date_f1 = 'dd-mm-yy'
date_f2 = 'mm-dd-yy'
date_f3 = 'yy-mm-dd'


dob_f = (
    # ( date_f0,   _('Please Select Date format')   ),
    ( date_f1,   _('DD-MM-YYYY')   ),
    ( date_f2, _('MM-DD-YYYY') ),
    ( date_f3,   _('YYYY-MM-DD')   ),
)