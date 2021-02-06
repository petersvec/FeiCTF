import string
import random

def generate_random_block(size):
    return "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(size))

print("[*] Generating flag:")

flag = "bispp_flag{"

block_size = 6

for _ in range(4):
    flag += generate_random_block(block_size)
    flag += "-"

flag += generate_random_block(block_size)
flag += "}"

print(flag)
