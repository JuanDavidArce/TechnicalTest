import random

def generate_pin():
    pin = random.getrandbits(128)
    pin = '%032x'%pin
    return pin