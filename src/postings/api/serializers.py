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

        read_only_fields    = ['user']

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value) #incluye la instancia actual
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        
        if qs.exists():
            raise serializers.ValidationError("El titulo ya está en uso, y debería ser único")
        return value


        # converts to JSON
        # validations for data passed
     