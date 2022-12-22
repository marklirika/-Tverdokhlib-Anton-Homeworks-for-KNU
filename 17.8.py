def contain_only_key_arguments(func):
    def wrapper(*args, **kwargs):
        if args:
            raise TypeError("Only keyword arguments are allowed")
        return func(**kwargs)
    return wrapper


@contain_only_key_arguments
def find_biggest(**kwargs):
    return max(kwargs, key=kwargs.get)


print(find_biggest(a=1, b=2, c=3, d=4, nad=11, e=5))