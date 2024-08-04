
def check_missing_fields( data, required_fields=[]):
    missing_fields = list(filter(lambda field: field not in data, required_fields))
    return missing_fields