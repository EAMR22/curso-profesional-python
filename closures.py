# Hola 3 -> HolaHolaHola
# Moises 2 -> MoisesMoises

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))
    repeat_3 = make_repeater_of(3)
    print(repeat_3("Platzi"))


if __name__ == '__main__':
    run()