#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
    except IndexError:
        return False
    except Exception as err:
        return False
