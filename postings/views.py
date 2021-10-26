import json
from json.decoder import JSONDecodeError

from django.http  import JsonResponse
from django.views import View
from django.db    import transaction

from postings.models import Posting
from users.decorators  import login_decorator


class PostingView(View):
    @login_decorator
    def post(self, request):
        try:
            data    = json.loads(request.body)
            user    = request.user
            title   = data['title']
            content = data['content']

            Posting.objects.create(
                user_id = user.id,
                title   = title,
                content = content
            )
            return JsonResponse({'data': 'SUCCESS'}, status=201)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)
        
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        
    def get(self, request):
        try:
            limit  = int(request.GET.get('limit', 10))
            offset = int(request.GET.get('offset', 0))

            if limit > 10:
                return JsonResponse({'message':'TOO_MUCH_LIMIT'}, status=400)

            postings  = Posting.objects.all()[offset:offset+limit]

            result = [{
                'post_id'    : posting.id,
                'user'       : posting.user.name,
                'title'      : posting.title,
                "created_at" : posting.created_at,
                "updated_at" : posting.updated_at
                } for posting in postings]
            
            return JsonResponse({'count': len(postings), 'data':result}, status=200)

        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)