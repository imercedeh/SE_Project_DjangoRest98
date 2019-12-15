from django.test import TestCase
from Places.models import Places



class PlacesTest(TestCase):

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


    def test_placeunicode(self):
        places=Places.objects.get(title='اصفهان')
        self.assertEqual(places.__unicode__(),'اصفهان')

    def test_placestr(self):
        places=Places.objects.get(title='همدان')
        self.assertEqual(places.__str__(),'همدان')

