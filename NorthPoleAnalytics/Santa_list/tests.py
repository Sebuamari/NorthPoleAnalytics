import random
import requests
from django.test import TestCase

class ProductCreationTest(TestCase):
    def test_should_create_kids(self):
        for _ in range(10):
            kid_data = {
                "name": random.choice([
                    'Mari', 'Giorgi', 'Nana', 'Lina', 'Guga', 'Vazha', 'Niko', 'Teo',
                    'Lado', 'Dato', 'Lile', 'Sandro', 'Mancho', 'Guri', 'Lela', 'Saba'
                ]),
                "niceness_coefficient": random.randint(0, 10),
                "gift": random.choice([
                    'Ball', 'Phone', 'Car', 'Train', 'Bear', 'Lego',
                ]),
                "santas_list": 1
            }

            response = requests.post('http://127.0.0.1:8000/santa-list/', data=kid_data)
            self.assertEqual(response.status_code, 201)