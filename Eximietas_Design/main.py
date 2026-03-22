#decorator logic to add the country code +91
#input= 10 digit mob number


def add_country_code(func):
    def wrapper(*args, **kwargs):
        final = "91+" + func(*args, **kwargs)
        return final
    return wrapper

@add_country_code
def provide_mob_num(number):
    return number
print(provide_mob_num("8574205817"))




