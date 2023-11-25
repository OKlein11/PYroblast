def urlBuilder(*args): 
    '''Takes an arbitrary number of arguments and adds them together as str with a "/" in between them, as in a url'''
    url = ""
    for arg in args:
        url += (str(arg) + "/")
    return url