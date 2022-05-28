
import colorama
class BuildingError(Exception):
    def __init__(self):
        return f"With so much material the house "
def check_material(amount_of_material, limit_value)
    if amount_of_material > limit_value:
        return "enough material"
    else:
        raise BuildingError(amount_of_material)
check_material(int(input()),300)
a = int(input())

try:
    print(10/0)
    print("sucssesful")
except ZeroDivisionError:
    print(colorama.Fore.RED + "It is not possible to divide by 0")
except TypeError:
    print(colorama.Fore.RED + "It is not possible to divide by "str"")
except:
    print(colorama.Fore.ORANGE + "It is not possible to divide by "str"")
except NameError:
    print(colorama.Fore.YELLOW + "You are accessing an object that does not exist")
else:
    print(colorama.Fore.GREEN + "Nothing went wrong")
input()