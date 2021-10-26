import jwt

from django.http     import JsonResponse

from users.models    import User
from prejuhyun.settings import SECRET_KEY, ALGORITHMS

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHMS)
            user         = User.objects.get(id=payload['id'])
            request.user = user
            
        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE': 'DECODE_ERROR'}, status=401)
        
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE': 'USER_NOTEXIST'}, status=401)
        
        return func(self, request, *args, **kwargs)
    
    return wrapper 