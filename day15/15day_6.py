'''用装饰器实现单例模式'''
from functools import wraps
from threading import Lock
def singleton(cls):
    instances={}
    locker=Lock()  #线程安全的单例装饰器
    @wraps(cls)
    def wrapper(*args,**kwargs):
        if cls not in instances:
            instances[cls]=cls(*args,**kwargs)
        return instances[cls]
    return wrapper
@singleton
class President():
    """总统(单例类)"""
    pass