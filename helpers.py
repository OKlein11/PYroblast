def urlBuilder(*args, **kwargs): 
    '''Takes an arbitrary number of arguments and adds them together as str with a "/" in between them, as in a url 
    and adds an arbitrary number of keyword args as parameters at the end in the format ?key1=val1&key2=val2'''
    url = ""
    for arg in args:
        url += (str(arg) + "/")
    url += "?"
    for param in kwargs.items():
        url += (f"{param[0]}={str(param[1])}&")
    return url
