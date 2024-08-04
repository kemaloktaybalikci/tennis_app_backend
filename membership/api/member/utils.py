def create_member(data):
    member = Member.objects.create(**data)
    return member

def detail_data(data):
    from membership.constants import DATE_FORMAT, DATETIME_FORMAT
    res = {}
    for key, value in data.items():
        if isinstance(value, datetime.datetime):
            data[key] = value.strftime(constants.DATETIME_FORMAT)
        elif isinstance(value, datetime.date):
            data[key] = value.strftime(constants.DATE_FORMAT)
        elif isinstance(value, models.ForeignKey):
            if value and hasattr(value, 'name'):
                data[key] = value.name
            elif value:
                data[key] = value.pk
            else:
                data[key] = None
        else:
            data[key] = value
    return res

def put_member(member, data):
    member.update(**data)
    return member