import datetime

from http import HTTPStatus

from django import test
from django.urls import reverse

from app.models import User


class UserBaseTest(test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('index')

    def test_get_user_create_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_professor(self):
        payload = {
            'first_name': 'test',
            'last_name': 'professor',
            'date_of_birth': datetime.date.today,
            'role': 'professor',
            'phone_number': '+ 999 123 45 67',
            'email': 'example@mail.professor',
            'street': 'Some street',
            'street_number': '9',
            'city': 'Some City',
            'post_number': '12345',
            'country': 'Some Country'
        }

        response = self.client.post(reverse('index'), data=payload, format='multipart', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_professors_page(self):
        response = self.client.get(reverse('professors'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_professor_update_page(self):
        professor = User.objects.get(email='example@mail.professor')
        response = self.client.get(reverse('professor-update', kwargs=professor.pk),
                                   format='multipart',
                                   follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_update_professor(self):
        professor = User.objects.get(email='example@mail.professor')
        professor = professor.__dict__
        professor['first_name'] = 'new Name'
        response = self.client.post(reverse('professor-update', kwargs=professor['pk']), data=professor,
                                    format='multipart',
                                    follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_delete_professor(self):
        professor = User.objects.get(email='example@mail.professor')
        professor = professor.__dict__
        response = self.client.get(reverse('user-delete', kwargs=professor['pk']), format='multipart',
                                   follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_deleted_professor(self):
        professor = User.objects.get(email='example@mail.professor')
        self.assertFalse(professor)

    def test_email_uniqueness_professor(self):
        payload = {
            'first_name': 'test',
            'last_name': 'professor',
            'date_of_birth': datetime.date.today,
            'role': 'student',
            'phone_number': '+ 999 123 45 67',
            'email': 'example@mail.professor',
            'street': 'Some street',
            'street_number': '9',
            'city': 'Some City',
            'post_number': '12345',
            'country': 'Some Country'
        }

        response = self.client.post(reverse('index'), data=payload, format='multipart', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.NOT_ACCEPTABLE)

    # ----------------------------------------------------------------

    def test_create_student(self):
        payload = {
            'first_name': 'test',
            'last_name': 'student',
            'date_of_birth': datetime.date.today,
            'role': 'professor',
            'phone_number': '+ 999 123 45 67',
            'email': 'example@mail.student',
            'street': 'Some street',
            'street_number': '9',
            'city': 'Some City',
            'post_number': '12345',
            'country': 'Some Country'
        }

        response = self.client.post(reverse('index'), data=payload, format='multipart', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_students_page(self):
        response = self.client.get(reverse('students'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_student_update_page(self):
        student = User.objects.get(email='example@mail.student')
        response = self.client.get(reverse('student-update', kwargs=student.pk),
                                   format='multipart',
                                   follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_update_student(self):
        professor = User.objects.get(email='example@mail.student')
        professor = professor.__dict__
        professor['first_name'] = 'new Name'
        response = self.client.post(reverse('student-update', kwargs=professor['pk']), data=professor,
                                    format='multipart',
                                    follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_delete_student(self):
        student = User.objects.get(email='example@mail.student')
        student = student.__dict__
        response = self.client.get(reverse('user-delete', kwargs=student['pk']), format='multipart',
                                   follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_deleted_student(self):
        student = User.objects.get(email='example@mail.student')
        self.assertFalse(student)

    def test_email_uniqueness_student(self):
        payload = {
            'first_name': 'test',
            'last_name': 'student',
            'date_of_birth': datetime.date.today,
            'role': 'student',
            'phone_number': '+ 999 123 45 67',
            'email': 'example@mail.student',
            'street': 'Some street',
            'street_number': '9',
            'city': 'Some City',
            'post_number': '12345',
            'country': 'Some Country'
        }

        response = self.client.post(reverse('index'), data=payload, format='multipart', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.NOT_ACCEPTABLE)
