from django.utils.crypto import get_random_string


def create_new_ref_number(n):
    return get_random_string(n, allowed_chars='0123456789')
