def create_app():
    middlewares = []
    registered = dict()

    def register(name, fun):
        registered[name] = fun

    def use(middleware):
        middlewares.append(middleware)

    def remove(middleware):
        middlewares.remove(middleware)

    def call(name, request):
        fun = registered[name]

        next = lambda req: fun(req)
        for it in reversed(list(middlewares)):
            def n(req, next=next,it=it):
                return it(req, next)

            next = n

        return next(request)

    return register, use, remove, call

register, use, remove, call = create_app()

def upper(req):
    return req.upper()

def lower(req):
    return req.upper()

register("upper", upper)
register("lower", lower)
print(call("upper", "first request"))
    
def log_middleware(req, next):
    print(f"request: {req}")
    response = next(req)
    print(f"response: {response}")
    return response

use(log_middleware);
call("upper", "second request" )

def lower_middleware(req, next):
    response = next(req)
    return response.lower()

use(lower_middleware)
call("upper", "ThIrD rEqUeSt" )

remove(log_middleware)
print(call("lower", "FOURTH REQUEST"))

remove(lower_middleware)
print(call("upper", "fifth request"))