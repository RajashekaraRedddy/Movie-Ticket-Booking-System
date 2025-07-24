import random

def get_otp():
    otp = random.randint(10000, 99999)
    return str(otp)
