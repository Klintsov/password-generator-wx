import secrets
from random import SystemRandom


def create_new(lenght, characters):
    rnd: SystemRandom = secrets.SystemRandom()
    return "".join(rnd.choice(characters) for _ in range(lenght))
