from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

from django.contrib.auth import get_user_model

#automated
#new blank db
from postings.models import BlogPost
from rest_framework.reverse import reverse as api_reverse
User = get_user_model()

class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username="testcfeuser", email="test@test.com")
        user_obj.set_password("randompassword")
        user_obj.save()
        blog_post   = BlogPost.objects.create(user=user_obj, title="New Title", content="some_random_content")

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = BlogPost.objects.count()
        self.assertEqual(post_count, 1)
        
    def test_get_list(self):
        # tested the get list item
        data = {}
        url = api_reverse("api-postings:post-listcreate")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_post_item(self):
        # tested create item
        data = {
            "title": "Random title",
            "content": "Some more content"
        }
        url = api_reverse("api-postings:post-listcreate")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        # tested the get list item
        blog_post = BlogPost.objects.first()
        data = {}
        url = blog_post.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
    
    def test_update_item(self):
        # tested create item
        blog_post = BlogPost.objects.first()
        url = blog_post.get_api_url()
        data = {
            "title": "Random title",
            "content": "Some more content"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_item_with_user(self):
        # tested create item
        blog_post = BlogPost.objects.first()
        url = blog_post.get_api_url()
        data = {
            "title": "Random title",
            "content": "Some more content"
        }
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp) #"JWT <token>"

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_post_item_with_user(self):
        # tested create item

        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp) #"JWT <token>"

        data = {
            "title": "Random title",
            "content": "Some more content"
        }
        url = api_reverse("api-postings:post-listcreate")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_ownership(self):
        # tested create item

        owner = User(username="usertest2", email="test2@test.com")
        owner.save()
        blog_post   = BlogPost.objects.create(user=owner, title="New Title 2 ", content="some_random_content 2")

        user_obj = User.objects.first()
        self.assertNotEqual(user_obj.username, owner.username)

        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp) #"JWT <token>"

        url = blog_post.get_api_url()
        data = {"title": "Random title", "content": "Some more content" }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_login_and_update(self):
        data = {
            "username": "testcfeuser",
            "password": "randompassword"
        }
        url = api_reverse("api-login")
        response = self.client.post(url, data)
        print(response.data)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get("token")
        if token is not None:
            blog_post = BlogPost.objects.first()
            url = blog_post.get_api_url()
            data = {
                "title": "Random title",
                "content": "Some more content"
            }
            self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token) #"JWT <token>"
            response = self.client.put(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)




#request.post(url, data, headers={"Authorization": "JWT " + <token>})