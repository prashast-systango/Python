# Middleware
def my_middleware(get_response):
    # This will be initialized only once
    print('One time initialization')
    def my_function(request):
        # Everything between function start and get_response, will be called before view 
        print("I am before view")
        response = get_response(request)
        # Everything after get_response will be called after view 
        print("I am after view")
        return response
    return my_function