# generic 

from rest_framework import generics, mixins
from postings.models import BlogPost

from .serializers import BlogPostSerializer

class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field    = 'pk' #slug, id
    serializer_class     =  BlogPostSerializer
    #queryset        = BlogPost.objects.all()

    def get_queryset(self):
        # qs = BlogPost.objects.all()
        # qs = qs.exclude(pk=2)
        return BlogPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def post(self, request, *args, **kwargs):
         return self.create(request, *args, **kwargs)


class BlogPostRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field    = 'pk' #slug, id
    serializer_class     =  BlogPostSerializer
    #queryset        = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_object(self):
    #     pk  = self.kwargs.get("pk")
    #     return BlogPost.objects.get(pk=pk)