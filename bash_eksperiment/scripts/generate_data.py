import random
import sys

seed = int(sys.argv[1] if len(sys.argv) > 1 else 20)
random.seed(seed)

n = 200
for i in range(n):
    random_number = random.randint(1, 100)
    print(random_number)
