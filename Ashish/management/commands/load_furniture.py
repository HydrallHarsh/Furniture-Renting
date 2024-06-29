from django.core.management.base import BaseCommand
from Ashish.models import Furniture  # Ensure this import matches your app's name
import csv

class Command(BaseCommand):
    help = 'Load furniture data from a CSV file'

    def handle(self, *args, **kwargs):
        file_path = 'Ashish\management\commands\Final_data.csv'  # Update this path if necessary
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Furniture.objects.create(
                    owner=row['Owner'],
                    furniture_type=row['furniture_type'],
                    company_name=row['company_name'],
                    description=row['Description'],
                    average_cost=row['Average_Cost'],
                    image_url=row['image_url'],
                    minimum_rental_days=row['minimum_rental_days'],
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
