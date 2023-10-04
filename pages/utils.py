import datetime
import logging
import random
import string
from time import sleep


def rand_password(password=13):
    generate_pass = ''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(password)])
    return generate_pass


def rand_email(email=7):
    generate_email = ''.join([random.choice(string.ascii_lowercase) for _ in range(email)]) + '@gmail.com'
    return generate_email


def rand_username(name=8):
    generate_name = ''.join([random.choice(string.ascii_lowercase) for _ in range(name)])
    return generate_name


def rand_str(stroke=14):
    generate_str = ''.join([random.choice(string.ascii_lowercase) for _ in range(stroke)])
    return generate_str


def rand_numb(numb=2):
    generate_numb = ''.join([random.choice(string.digits) for _ in range(numb)])
    return generate_numb


def wait_until_ok(timeout=5, period=0.5):
    """Reties until OK"""

    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        log.error(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_decorator(original_function):
    """Logging actions using docstrings"""
    log = logging.getLogger("[LogDecorator]")

    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        log.info(original_function.__doc__)
        return result

    return wrapper


class TextBox:

    def __init__(self, full_name='', email='', cur_address='', per_address=''):
        self.full_name = full_name
        self.email = email
        self.cur_address = cur_address
        self.per_address = per_address

    def fill_default(self):
        """Fill fields using random data"""
        self.full_name = rand_username(7)
        self.email = rand_email(8)
        self.cur_address = rand_str(11)
        self.per_address = rand_str(10)


class WebTable:

    def __init__(self, first_name='', last_name='', email='', age='', salary='', department=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.salary = salary
        self.department = department

    def fill_default(self):
        """Fill fields using random data"""
        self.first_name = rand_username(7)
        self.last_name = rand_username(7)
        self.email = rand_email(8)
        self.age = rand_numb()
        self.salary = rand_numb(6)
        self.department = rand_str(9)
