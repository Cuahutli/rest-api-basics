from rest_framework import serializers
from postings.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer): # form.ModelForm
    class Meta:
        model = BlogPost
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'timestamp'
        ]

        # converts to JSON
        # validations for data passed
     