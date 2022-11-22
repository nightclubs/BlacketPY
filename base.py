from BlacketPY import *

def login_test():
    login = BlacketPY.login(
        '' # username,
        '' # password
    )

    return login # will return the login status and, if successful, the PHPSESSID for other requests will be returned as well.

def token_test():
    auth = str(login_test()).split('PHPSESSID: ')[1]
    token = BlacketPY.add_tokens(
        auth # not an authentication token, just the PHPSESSID returned from the login response split to fit.
    )

    return token

def buy_boxes():
    auth = str(login_test()).split('PHPSESSID: ')[1] 
    box = BlacketPY.buy_boxes(
        auth
    )

    return box


