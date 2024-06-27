import requests
import re,time
from random import randint

def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """
    def wrapper(*args, **kwargs):
        t1 = time.time()
        r = func(*args, **kwargs)
        t2 = time.time()
        print("Время выполнения функции %s: %s\n" % (func.__name__, t2 - t1))
        return r
    return wrapper

def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print("Функция вызвана с параметрами:\n%s, %s\n" % (args, kwargs))
        return r
    return wrapper

def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        wrapper.calls += 1
        print("Функция была вызвана: %s раз\n" % wrapper.calls)
        return r
    wrapper.calls = 0
    return wrapper

@counter
@logging
@benchmark
def word_count(word, url='https://www.gutenberg.org/files/2638/2638-0.txt'):
    # отправляем запрос в библиотеку Gutenberg и забираем текст
    raw = requests.get(url).text

    # заменяем в тексте все небуквенные символы на пробелы
    processed_book = re.sub('[\W]+', ' ', raw).lower()

    # считаем
    cnt = len(re.findall(word.lower(), processed_book))

    return f"Cлово {word} встречается {cnt} раз"


print(word_count('whole'))