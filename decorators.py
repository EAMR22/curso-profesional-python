from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        # *args: No importa la cantidad de argumentos posicionales que se le envíen, la función los va a recibir.
        # *kwargs: No importa la cantidad de argumentos nombrados que se le envíen, la función también los va a recibir.
        initial_time = datetime.now() # Nos devuelve la fecha y hora exacta en el momento en que se ejecuta el codigo.
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10000000): # Ponemos _ porque no nos interesa la variable de cada una de las vueltas.
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre = "Cesar"):
    print("Hola " + nombre)


random_func()
suma(5, 5)
saludo("Fabian")
# random_func()