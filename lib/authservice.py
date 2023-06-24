from flask import session
import functools


def user_auth(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        uid = session.get('uid')
        role = session.get('role')
        if not uid and role != 'user':
            return "Access Not Allow"
        return func(*args,**kwargs)
    return inner

def admin_auth(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        uid = session.get('uid')
        role = session.get('role')
        if not uid and role != 'admin':
            return "Access Not Allow"
        return func(*args,**kwargs)
    return inner

# def token_auth(func):
#     @functools.wraps(func)
#     def inner(*args,**kwargs):
#         token = request.headers.get('token')
#         if not token:
#             return "login faild"
#         return func(*args,**kwargs)
#     return inner


if __name__ == "__main__":
    admin_auth()