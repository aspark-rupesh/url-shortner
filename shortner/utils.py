import uuid
import random
import string
from .models import ShortUrl
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))



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
