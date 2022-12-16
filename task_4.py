import random
def task_4(length,
             format='.txt',
             ABC='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'):
    return ''.join(random.choice(ABC) for n in range(length)) + format