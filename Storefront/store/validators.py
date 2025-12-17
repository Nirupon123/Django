from django.core.exceptions import ValidationError

def valid_files(file):

    max_size_kb=1000

    if file.size > max_size_kb*1024:
        raise ValidationError(f'this file must be less than {max_size_kb}KB!')