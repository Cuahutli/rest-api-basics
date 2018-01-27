# generic 

from rest_framework import generics
from postings.models import BlogPost

from .serializers import BlogPostSerializer

class BlogPostAPIView(generics.ListAPIView):
    lookup_field    = 'pk' #slug, id
    serializer_class     =  BlogPostSerializer
    #queryset        = BlogPost.objects.all()

    def get_queryset(self):
        # qs = BlogPost.objects.all()
        # qs = qs.exclude(pk=2)
        return BlogPost.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class BlogPostRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field    = 'pk' #slug, id
    serializer_class     =  BlogPostSerializer
    #queryset        = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_object(self):
    #     pk  = self.kwargs.get("pk")
    #     return BlogPost.objects.get(pk=pk)