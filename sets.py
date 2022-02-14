# Eliminar los repetidos de una lista
# [1, 1, 2, 2, 3] -> [1, 2, 3]

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates: # Pregunta si no estan los elementos de la lista without_duplicates.
            without_duplicates.append(element)
    return without_duplicates


def run():
    random_list = [1, 1, 2, 2, 3]
    print(remove_duplicates(random_list))


if __name__ == '__main__':
    run()

    