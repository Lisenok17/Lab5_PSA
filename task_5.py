import random
class Password:
    def __init__(self, length, ABC='QWERTYUIOPASDFGHJKLZXCVBNM',
                 abc='qwertyuiopasdfghjklzxcvbnm',
                 numbers='1234567890',
                 special='?!&<>+=/'):
        self.length = length
        self.ABC = [ABC, abc, numbers, special]
    def gen(self):
        return ''.join(random.choice(self.ABC[random.randint(0, 3)]) for n in range(self.length))
