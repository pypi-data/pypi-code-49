import cProfile
import time
import traceback
from functools import wraps


def conn_try_again(function):
    retries = 5
    # retry time
    count = {"num": retries}

    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as err:
            if count['num'] < 2:
                count['num'] += 1
                return wrapped(*args, **kwargs)
            else:
                raise Exception(err)

    return wrapped


def catch_exception(function):
    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as err:
            traceback.print_exc()

    return wrapped


def exeTime(function):
    def wrapped(*args, **kwargs):
        t0 = time.time()
        print("@%s, {%s} start" % (time.strftime("%X", time.localtime()), function.__name__))
        back = function(*args, **kwargs)
        print("@%s, {%s} end" % (time.strftime("%X", time.localtime()), function.__name__))
        print("@%.3fs taken for {%s}" % (time.time() - t0, function.__name__))
        return back

    return wrapped


def statsProfile(function):
    """
    statics the detail of method run
    :param function:
    :return:
    """

    def wrapped(*args, **kwargs):
        profile = cProfile.Profile()
        profile.enable()
        back = function(*args, **kwargs)
        profile.disable()
        profile.print_stats(sort="tottime")

        return back

    return wrapped


class FunctionResultCacher:
    func_result_dict = {}
    # todo, there are another tools that support cache result by specified the number of cacher.
    # todo, implement.
    """
    From this page: https://www.cnblogs.com/ydf0509/p/9341365.html
    
    {
        (f1,(1,2,3,4)):(10,1532066199.739),
        (f2,(5,6,7,8)):(26,1532066211.645),
    }
    """

    @classmethod
    def cached_function_result_for_a_time(cls, cache_time):
        """
        函数的结果缓存一段时间装饰器
        :param cache_time 缓存的时间
        :type cache_time : float
        """

        def _cached_function_result_for_a_time(fun):

            @wraps(fun)
            def __cached_function_result_for_a_time(*args, **kwargs):
                if len(cls.func_result_dict) > 1024:
                    cls.func_result_dict.clear()

                key = cls._make_arguments_to_key(args, kwargs)
                if (fun, key) in cls.func_result_dict and time.time() - cls.func_result_dict[(fun, key)][
                    1] < cache_time:
                    return cls.func_result_dict[(fun, key)][0]
                else:
                    result = fun(*args, **kwargs)
                    cls.func_result_dict[(fun, key)] = (result, time.time())
                    # cls.logger.debug('函数 [{}] 此次不使用缓存'.format(fun.__name__))
                    return result

            return __cached_function_result_for_a_time

        return _cached_function_result_for_a_time

    @staticmethod
    def _make_arguments_to_key(args, kwds):
        key = args
        if kwds:
            sorted_items = sorted(kwds.items())
            for item in sorted_items:
                key += item
        return key
