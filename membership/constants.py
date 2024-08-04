STATUS_ACTIVE = 0
STATUS_PASSIVE = 1
STATUS_CUSTOM = 2

STATUS_CHOICES = [
    (STATUS_ACTIVE, 'Active'),
    (STATUS_PASSIVE, 'Passive'),
    (STATUS_CUSTOM, 'Custom'),
]

SEX_MALE = 0
SEX_FEMALE = 1
SEX_OTHER = 2

SEX_CHOICES = [
    (SEX_MALE, 'Male'),
    (SEX_FEMALE, 'Female'),
    (SEX_OTHER, 'Other'),
]

DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%d hh:mm:ss'
