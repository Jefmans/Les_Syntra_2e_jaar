from django.shortcuts import redirect



def only_provider():
    def decorators(view_func, *args, **kwargs):
        def wrapper_function(request, *args, **kwargs):
            try:
                request.user.provider
                return view_func(request, *args, **kwargs)
            except:
                redirect('index:home')



            return wrapper_function
        return decorators
    


def only_client():
    def decorators(view_func, *args, **kwargs):
        def wrapper_function(request, *args, **kwargs):
            try:
                request.user.client
                return view_func(request, *args, **kwargs)
            except:
                redirect('index:home')



            return wrapper_function
        return decorators
    

def only_current_user():
    def decorators(view_func, *args, **kwargs):
        def wrapper_function(request, *args, **kwargs):
            user_id = kwargs.get('pk')
            user = User.objects.get(id = user_id)
            if user == request.user:
                return view_func(request, *args, **kwargs)
            else:
                redirect('index:home')



            return wrapper_function
        return decorators
    

def only_company_user():
    def decorators(view_func, *args, **kwargs):
        def wrapper_function(request, *args, **kwargs):
            company_id = kwargs.get('company_id')
            company = Company.objects.get(id = company_id)
            
            if company == request.user.company :
                return view_func(request, *args, **kwargs)
            else:
                redirect('index:home')



            return wrapper_function
        return decorators