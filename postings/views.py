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
        
class PostingDetailView(View):
    
    def get(self, request, posting_id):
        try:
            posting = Posting.objects.get(id=posting_id)

            data = {
                    'post_id'    : posting.id,
                    'user'       : posting.user.name,
                    'title'      : posting.title,
                    'content'    : posting.content,
                    "created_at" : posting.created_at,
                    "updated_at" : posting.updated_at
                }
            return JsonResponse({'data': data}, status=200)

        except Posting.DoesNotExist:
            return JsonResponse({'message' : 'POST_NOT_FOUND'}, status=404)
        
    @login_decorator
    @transaction.atomic
    def patch(self, request, posting_id):
        try:
            data    = json.loads(request.body)
            user    = request.user
            title   = data['title']
            content = data['content']
            
            if not Posting.objects.filter(id=posting_id, user=user).exists():
                
                return JsonResponse({'message':'INVALID_POST_ID'}, status=404)

            posting = Posting.objects.get(id=posting_id, user=user)

            posting.content = content
            posting.title   = title
            posting.save()
            return JsonResponse({'message':'UPDATED'}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        
    @login_decorator
    def delete(self, request, posting_id):

        user = request.user

        if not Posting.objects.filter(id=posting_id, user=user).exists():
            return JsonResponse({'message':'INVALID_POSTING_ID'}, status=404)

        post = Posting.objects.get(id=posting_id, user=user)
            
        post.delete()
        return JsonResponse({'message':'DELETED'}, status=200)