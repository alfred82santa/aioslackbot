from inspect import signature

from functools import wraps


def return_model(func=None, *, just_return_bool=False):

    def inner(func):
        type_hints = signature(func).parameters

        try:
            klass = type_hints['return'].annotation
            klass = klass.__args__[0]
        except (AttributeError, IndexError):  # pragma: no cover
            try:
                klass = klass.__union_params__[0]
            except (AttributeError, IndexError):
                klass = None

        @wraps(func)
        async def wrapper(self, request):

            result = await self.parent.service_client.call(method="{}__{}".format(self._method_prefix,
                                                                                  func.__name__),
                                                           payload=request)

            if just_return_bool:
                return True

            if klass is not None:
                return klass(data=result.data)

            return result.data

        return wrapper

    if func:
        return inner(func)
    return inner