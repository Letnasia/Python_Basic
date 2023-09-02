class Qux(Exception):
    pass

def foo():
    index = 2
    my_list = [0, 3, 9]
    dd = {}

    try:
        print(my_list[index])
        raise Qux()
    except IndexError:
        print("You input wrong index")
    except Exception as e:
        print('Óooooh')

try:
    foo()
except Exception as e:
    print(f'found an error: {type(e)} {e}')
print(AssertionError.mro())