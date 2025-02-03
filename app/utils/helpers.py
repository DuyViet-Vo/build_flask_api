def validate_input(data, required_fields):
    for field in required_fields:
        if field not in data:
            return False
    return True
