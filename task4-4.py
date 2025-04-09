def arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Вызваны аргументы функции {func.__name__}")
        print(f"Позиционные аргументы -> {args}")
        print(f"Именованные аргументы -> {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"Площадь прямоугольника -> {result}")
        return result
    return wrapper

@arguments
def square(length, width):
    return length * width

square(8, 17)