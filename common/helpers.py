import string
import random


def generate_random_string(size):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(size))
