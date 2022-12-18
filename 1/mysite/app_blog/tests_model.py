from django.test import TestCase

# Create your tests here.

from .models import Category, Article, ArticleImage
class CategoryModelTest(TestCase): 
    
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test
        Category.objects.create(category='Innovations', slug='innovations')

    def test_get_absolute_url(self): 
        category=Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(),'/articles/category/innovations')

class ArticleModelTest(TestCase): 
    
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test
        Article.objects.create(title='No Way!', slug='no_way')

    def test_get_absolute_url(self): 
        title=Article.objects.get(id=1)
        self.assertEquals(title.get_absolute_url(),'/articles/2022/12/18/no_way')
