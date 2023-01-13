from django.core.exceptions import ValidationError

from MyEventWorld.core.helpers.mb_to_bytes import megabytes_to_bytes


def validate_file_less_than_3mb(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 3.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f"Max file size is {megabyte_limit}MB")
