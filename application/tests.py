from django.urls import reverse
from django.conf import settings
from django.test.client import encode_multipart
from rest_framework import status
from rest_framework.test import APITestCase
from application.models import Application

class Applicationtest(APITestCase):
    '''
        There are 6 tests for input validation.
        Something to note is that the email and personal_website fields are 
        already validated through Django with the model field. 
        Each test represents a different thing. 
        0 - All of the fields in data are filled in properly
        1 - The github field is incorrect
        2 - The linkedin field is incorrect
        3 - The graduation_date field is incorrect
        4 - The is_eighteen field is incorrect 
        5 - The agreed field is incorrect
    '''
    def test_input_validation0(self):
        url = reverse('application')
        resume = {'file': 'Pls hire me Verizon!'}
        in_file = encode_multipart('BoUnDaRyStRiNg', resume)
        data = {
            'first_name': 'Stanley',
            'last_name': 'Armstrong',
            'email': 'stanleyarmstrong31@gmail.com',
            'phone_number': '4084997923',
            'is_eighteen': True,
            'school': 'California Polytechnic University - San Luis Obispo',
            'graduation_date': '2021-06-01',
            'major': 'Computer Science',
            'city': 'San Jose',
            'dietary_restrictions': 0,
            'allergies': 'None',
            'github': 'https://github.com/stonewallstan',
            'linkedin': 'https://www.linkedin.com/in/stonewallstan/',
            'personal_website': 'https://www.google.com/',
            'resume': in_file,
            'short_answer': 'For the memes',
            'gender': 1,
            'ethnicity': 5,
            'anything_else': 'For the memes',
            'agreed': True
        }
        content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
        response = self.client.post(url, data, format = 'multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_input_validation1(self):
        url = reverse('application')
        resume = open('resume.txt', 'w')
        data = {
            'first_name': 'Stanley',
            'last_name': 'Armstrong',
            'email': 'stanleyarmstrong31@gmail.com',
            'phone_number': '4084997923',
            'is_eighteen': True,
            'school': 'California Polytechnic University - San Luis Obispo',
            'graduation_date': '2021-06-01',
            'major': 'Computer Science',
            'city': 'San Jose',
            'dietary_restrictions': 0,
            'allergies': 'None',
            'github': 'https://github.com/stonewallstan',
            'linkedin': 'https://www.linkedin.com/in/stonewallstan/',
            'personal_website': 'https://www.google.com/',
            'resume': resume,
            'short_answer': 'For the memes',
            'ethnicity': 5,
            'anything_else': 'For the memes',
            'agreed': True
        }
        pass
    def test_input_validation2(self):
        url = reverse('application')
        resume = open('resume.txt', 'w')
        data = {
            'first_name': 'Stanley',
            'last_name': 'Armstrong',
            'email': 'stanleyarmstrong31@gmail.com',
            'phone_number': '4084997923',
            'is_eighteen': True,
            'school': 'California Polytechnic University - San Luis Obispo',
            'graduation_date': '2021-06-01',
            'major': 'Computer Science',
            'city': 'San Jose',
            'dietary_restrictions': 0,
            'allergies': 'None',
            'github': 'https://github.com/stonewallstan',
            'linkedin': 'https://www.linkedin.com/in/stonewallstan/',
            'personal_website': 'https://www.google.com/',
            'resume': resume,
            'short_answer': 'For the memes',
            'gender': 1,
            'ethnicity': 5,
            'anything_else': 'For the memes',
            'agreed': True
        }
        pass
    def test_input_valdiation3(self):
        url = reverse('application')
        resume = open('resume.txt', 'w')
        data = {
            'first_name': 'Stanley',
            'last_name': 'Armstrong',
            'email': 'stanleyarmstrong31@gmail.com',
            'phone_number': '4084997923',
            'is_eighteen': True,
            'school': 'California Polytechnic University - San Luis Obispo',
            'graduation_date': '2021-06-01',
            'major': 'Computer Science',
            'city': 'San Jose',
            'dietary_restrictions': 0,
            'allergies': 'None',
            'github': 'https://github.com/stonewallstan',
            'linkedin': 'https://www.linkedin.com/in/stonewallstan/',
            'personal_website': 'https://www.google.com/',
            'resume': resume,
            'short_answer': 'For the memes',
            'gender': 1,
            'ethnicity': 5,
            'anything_else': 'For the memes',
            'agreed': True
        }
        pass
    def test_input_validation4(self):
        url = reverse('application')
        resume = open('resume.txt', 'w')
        data = {
            'first_name': 'Stanley',
            'last_name': 'Armstrong',
            'email': 'stanleyarmstrong31@gmail.com',
            'phone_number': '4084997923',
            'is_eighteen': True,
            'school': 'California Polytechnic University - San Luis Obispo',
            'graduation_date': '2021-06-01',
            'major': 'Computer Science',
            'city': 'San Jose',
            'dietary_restrictions': 0,
            'allergies': 'None',
            'github': 'https://github.com/stonewallstan',
            'linkedin': 'https://www.linkedin.com/in/stonewallstan/',
            'personal_website': 'https://www.google.com/',
            'resume': resume,
            'short_answer': 'For the memes',
            'gender': 1,
            'ethnicity': 5,
            'anything_else': 'For the memes',
            'agreed': True
        }
        pass
    def test_input_validation5(self):
        url = reverse('application')
        resume = open('resume.txt', 'w')
        data = {
            'first_name': 'Stanley',
            'last_name': 'Armstrong',
            'email': 'stanleyarmstrong31@gmail.com',
            'phone_number': '4084997923',
            'is_eighteen': True,
            'school': 'California Polytechnic University - San Luis Obispo',
            'graduation_date': '2021-06-01',
            'major': 'Computer Science',
            'city': 'San Jose',
            'dietary_restrictions': 0,
            'allergies': 'None',
            'github': 'https://github.com/stonewallstan',
            'linkedin': 'https://www.linkedin.com/in/stonewallstan/',
            'personal_website': 'https://www.google.com/',
            'resume': resume,
            'short_answer': 'For the memes',
            'gender': 1,
            'ethnicity': 5,
            'anything_else': 'For the memes',
            'agreed': True
        }
        pass