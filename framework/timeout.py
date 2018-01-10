import threading
import sys
class Timeout(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
class KThread(threading.Thread):
    """Subclass of threading.Thread, with a kill() method."""
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.killed = False
    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        """Force the Thread to install our trace."""
        self.run = self.__run
        threading.Thread.start(self)
    def __run(self):
        """Hacked run function, which installs the trace."""
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup
    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace
        else:
            return None
    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()
        return self.localtrace
    def kill(self):
        self.killed = True
def timeout(seconds):
    def timeout_decorator(func):
        def _new_func(oldfunc, result, oldfunc_args, oldfunc_kwargs):
            result.append(oldfunc(*oldfunc_args, **oldfunc_kwargs))
        def _(*args, **kwargs):
            result = []
            '''create new args for _new_funcbecause
               we want to get the func return val to result list
            '''
            new_kwargs = {
                'oldfunc': func,
                'result': result,
                'oldfunc_args': args,
                'oldfunc_kwargs': kwargs
            }
            thd = KThread(target=_new_func, args=(), kwargs=new_kwargs)
            thd.start()
            thd.join(seconds)
            alive = thd.isAlive()
            '''kill the child thread'''
            thd.kill()
            if alive:
                alert_exce = u'function timeout for [%d s].' % seconds
                raise Timeout(alert_exce)
            else:
                return result[0]
        _.__name__ = func.__name__
        _.__doc__ = func.__doc__
        return _
    return timeout_decorator