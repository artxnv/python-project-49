import random


def generate_random_number(start=1, end=100):
    """
    Генерирует случайное число в заданном диапазоне.
    """
    return random.randint(start, end)
