from functools import wraps
import time

def howlong(func):
    @wraps(func)
    def howlong_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Fungsi {func.__name__} membutuhkan waktu {total_time:.4f} detik')
        return result
    return howlong_wrapper

@howlong
def loop(number):
    for _ in range(number):
        pass

if __name__ == '__main__':
    loop(100000000)