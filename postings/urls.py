from django.urls    import path

from postings.views import PostingDetailView, PostingView, PostingDetailView

urlpatterns = [
    path('', PostingView.as_view()),
    path('/<int:posting_id>', PostingDetailView.as_view())
]