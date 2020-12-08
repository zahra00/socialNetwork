import uuid


def get_random_code():
    """ when user name and last name are same so the slug are same"""
    code = str(uuid.uuid4())[:8].replace('-', '').lower()
