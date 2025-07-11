from rest_framework import serializers
from django.contrib.auth.models import User
from cat.models import Cat
from subcat.models import SubCat
from newsletter.models import Newsletter
from news.models import News
from contactform.models import ContactForm
from comment.models import Comment

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']  # Make the id field read-only

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['id', 'name', 'count']  # Updated fields to match the model
        read_only_fields = ['id', 'count']  # Make the id and count fields read-only

# Subcategory Serializer
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCat
        fields = ['id', 'name', 'catname', 'catid']  # Updated fields to match the model
        read_only_fields = ['id']  # Make the id field read-only

# Newsletter Serializer
class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'txt', 'status']  # Updated fields to match the model
        read_only_fields = ['id']  # Make the id field read-only

# News Serializer
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id', 'name', 'short_txt', 'body_txt', 'date', 'time', 'picname',
            'picurl', 'writer', 'catname', 'catid', 'ocatid', 'show', 'tag', 'act', 'rand'
        ]  # Updated fields to match the model
        read_only_fields = ['id']  # Make the id field read-only

# Contact Form Serializer
class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['id', 'name', 'email', 'txt', 'date', 'time']  # Updated fields to match the model
        read_only_fields = ['id', 'date', 'time']  # Make the id, date, and time fields read-only

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'cm', 'news_id', 'date', 'time', 'status']  # Updated fields to match the model
        read_only_fields = ['id', 'date', 'time']  # Make the id, date, and time fields read-only