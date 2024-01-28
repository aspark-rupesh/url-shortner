from django.utils.text import slugify
import random
import string
from .models import ShortUrl
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

def unique_slug_generator(url, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(url)
        
    Klass = ShortUrl
    max_length = 10
    slug = slug[:max_length]
    qs_exists = ShortUrl.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug[: max_length - 5], randstr=random_string_generator(size=4)
        )

        return unique_slug_generator(url, new_slug=new_slug)
    return slug


import uuid

def unique_key_generator(id=None):
    if not id:
        last_url = ShortUrl.objects.last()
        if last_url:
            id = last_url.id +1
        else:
            id = 0
    
    uuid_ = str(uuid.uuid1(id))[:10]
    qs_exists = ShortUrl.objects.filter(short_key=uuid_).exists()
    if qs_exists:
        return unique_key_generator(uuid_)
    return uuid_
