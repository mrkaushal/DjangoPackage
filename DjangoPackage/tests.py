import unittest
import datetime
from authApp.models import CustomUser


# Create your tests here.
# Execute Test.py file in windows : manage.py test Genetic.tests.MainTestCase.MainCase
# Execute Test.py file in linux   : ./manage.py test Genetic.tests.MainTestCase.MainCase

class MainTestCase(unittest.TestCase):
    def MainCase(self):
        current_date = datetime.date.today()
        print('Creating Account....')

        add = CustomUser.objects.create_user(username='admin', password='admin@123', email='admin@admin.com', role=1,
                                             aid=1)
        add.save()
