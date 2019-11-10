from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from Places.models import Places
from Places.api.views import UniquePlaceAPI
from rest_framework.test import APIRequestFactory
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
factory = APIRequestFactory()


class TestView(APITestCase):

    def setUp(self):
        self.place1=Places.objects.create(
            title='اصفهان',
            Description='اصفهان زیباست',
            Likes='2',
            categories='مذهبی',
            Hardness='متوسط',
            Address='اصفهان',
            Time='20',
            StartTime='8',
            EndTime='12',
            City='اصفهان',
            image1="http://127.0.0.1:8000/media/image/2019/11/07/1386_y7ISjz1.jpg",
            image2="http://127.0.0.1:8000/media/image/2019/11/07/1386_y7ISjz1.jpg",
            image3="http://127.0.0.1:8000/media/image/2019/11/07/1386_y7ISjz1.jpg",
        )

        self.place2=Places.objects.create(
            title='همدان',
            Description='همدان زیباست',
            Likes='2',
            categories='مذهبی',
            Hardness='متوسط',
            Address='همدان',
            Time='20',
            StartTime='8',
            EndTime='12',
            City='همدان',
            image1="http://127.0.0.1:8000/media/image/2019/11/07/1386_y7ISjz1.jpg",
            image2="http://127.0.0.1:8000/media/image/2019/11/07/1386_y7ISjz1.jpg",
            image3="http://127.0.0.1:8000/media/image/2019/11/07/1386_y7ISjz1.jpg",
        )

    def test_get_queryset(self):
        url='http://127.0.0.1:8000/api/Places/ViewPlace/'
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs=Places.objects.filter(City='همدان')
        self.assertEqual(qs.count(),1)


    def test_post_createplace(self):
        url='http://127.0.0.1:8000/api/Places/CreatePlace/'
        data={
              "id": 2,
              "leader": [
                {
                "nationalID": 9856,
                "has_car": True,
                "car_capacity": 2,
                "car_model": "BMW"
                }
            ],
            'title':"یزد",
            'Description':"یزد زیباست",
            'Likes':"2",
            'categories':"مذهبی",
            'Hardness':"متوسط",
            'Address':"یزد",
            'Time':"20",
            'StartTime':"8",
            'EndTime':"12",
            'City':"یزد",
            "Average": "0",
            'image1':"http://127.0.0.1:8000/media/image/2019/11/07/1386_y7ISjz1.jpg",
            'image2':"http://127.0.0.1:8000/media/image/2019/11/07/1386_y7ISjz1.jpg",
            'image3':"http://127.0.0.1:8000/media/image/2019/11/07/1386_y7ISjz1.jpg",
        }

        response=self.client.post(url,data,format='json')
       # print(response.status_code)
        self.assertEqual(response.status_code,415)


    def test_filter(self):
        url='http://127.0.0.1:8000/api/Places/UniquePlace/?search=1'
        data= {
            "id": 1,
            "leader": [
            {
                "nationalID": 9856,
                "has_car": True,
                "car_capacity": 2,
                "car_model": "BMW"
            },
            {
                "nationalID": 556,
                "has_car": True,
                "car_capacity": 1,
                "car_model": "perayd"
            }
            ],
            "title": "زاگرس",
            "Description": "کابل زیباست",
            "Likes": "2",
            "categories": "موزه",
            "Hardness": "متوسط",
            "Address": "افغانستان",
            "Time": "20",
            "StartTime": "بدون زمان شروع ",
            "EndTime": "بدون زمان پایان ",
            "City": "کابل",
            "Average": "0",
            "image1": "http://127.0.0.1:8000/media/image/2019/11/06/1386.jpg",
            "image2": "http://127.0.0.1:8000/media/image/2019/11/06/16224_655.jpg",
            "image3": "http://127.0.0.1:8000/media/image/2019/11/06/tabriz.jpg111-650x365.jpg"
        }
        response = self.client.get(url, data=data, format='json')
        self.assertEqual(response.status_code, 200)
        queryset=Places.objects.all()
        qs=queryset.filter(id__exact=1)
        self.assertEqual(len(qs),1)
        self.assertEqual(len(response.data), 2)

    def test_queryset_filter(self):
        queryset=Places.objects.all()
        qs=queryset.filter(id__exact=1).distinct()
        self.assertEqual(len(qs),1)
        url='http://127.0.0.1:8000/api/Places/UniquePlace/?search=1'
        data= {
            "id": 1,
            "leader": [
            {
                "nationalID": 9856,
                "has_car": True,
                "car_capacity": 2,
                "car_model": "BMW"
            },
            {
                "nationalID": 556,
                "has_car": True,
                "car_capacity": 1,
                "car_model": "perayd"
            }
            ],
            "title": "زاگرس",
            "Description": "کابل زیباست",
            "Likes": "2",
            "categories": "موزه",
            "Hardness": "متوسط",
            "Address": "افغانستان",
            "Time": "20",
            "StartTime": "بدون زمان شروع ",
            "EndTime": "بدون زمان پایان ",
            "City": "کابل",
            "Average": "0",
            "image1": "http://127.0.0.1:8000/media/image/2019/11/06/1386.jpg",
            "image2": "http://127.0.0.1:8000/media/image/2019/11/06/16224_655.jpg",
            "image3": "http://127.0.0.1:8000/media/image/2019/11/06/tabriz.jpg111-650x365.jpg"
        }
        self.assertQuerysetEqual(qs, ['<Places: اصفهان>'],ordered=False)
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(qs.count(),1)