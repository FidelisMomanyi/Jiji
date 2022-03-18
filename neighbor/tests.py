from django.test import TestCase
from .models import Neighborhood
from django.contrib.auth.models import User

# Create your tests here.
class NeighborhoodTestClass(TestCase):
    
    def setUp(self):
        self.neighborhood = Neighborhood(name='Imara', location='Nairobi', total_occupants=5)


    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood, Neighborhood))

    def test_create_neighborhood(self):
        self.neighborhood.create_neighborhood()
        neighbors = Neighborhood.objects.all()
        self.asserTrue(len(neighbors)>0)

    def test_delete_neighborhood(self):
        self.neighborhood.delete_neighborhood()
        neighbors = Neighborhood.objects.all()
        self.asserTrue(len(neighbors) == 0)