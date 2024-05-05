from django.core.management.base import BaseCommand
from faker import Faker
from fire.models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions
import random

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_locations(10)
        self.create_incidents(10)
        self.create_fire_stations(20)
        self.create_firefighters(25)
        self.create_fire_trucks(30)
        self.create_weather_conditions(10)

    def create_locations(self, count):
        fake = Faker()
        for _ in range(count):
            Locations.objects.create(
                name=fake.city(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )
            self.stdout.write(self.style.SUCCESS('Initial data for locations created successfully.'))

    def create_incidents(self, count):
        fake = Faker()
        locations = Locations.objects.all()
        for _ in range(count):
            Incident.objects.create(
                location=random.choice(locations),
                date_time=fake.date_time_this_year(),
                severity_level=random.choice(['Minor Fire', 'Moderate Fire', 'Major Fire']),
                description=fake.sentence()
            )
            self.stdout.write(self.style.SUCCESS('Initial data for incidents created successfully.'))

    def create_fire_stations(self, count):
        fake = Faker()
        for _ in range(count):
            FireStation.objects.create(
                name=fake.company(),
                latitude=fake.latitude(),
                longitude=fake.longitude(),
                address=fake.address(),
                city=fake.city(),
                country=fake.country()
            )
            self.stdout.write(self.style.SUCCESS('Initial data for fire stations created successfully.'))

    def create_firefighters(self, count):
        fake = Faker()
        for _ in range(count):
            Firefighters.objects.create(
                name=fake.name(),
                rank=random.choice(['Probationary Firefighter', 'Firefighter I', 'Firefighter II', 'Firefighter III', 'Driver', 'Captain', 'Battalion Chief']),
                experience_level=fake.word(),
                station=random.choice(['Probationary Firefighter', 'Firefighter I', 'Firefighter II', 'Firefighter III', 'Driver', 'Captain', 'Battalion Chief'])
            )
            self.stdout.write(self.style.SUCCESS('Initial data for firefighters created successfully.'))

    def create_fire_trucks(self, count):
        fake = Faker()
        fire_stations = FireStation.objects.all()
        for _ in range(count):
            FireTruck.objects.create(
                truck_number=fake.random_number(digits=4),
                model=fake.word(),
                capacity=fake.random_number(digits=3),
                station=random.choice(fire_stations)
            )
            self.stdout.write(self.style.SUCCESS('Initial data for fire trucks created successfully.'))

    def create_weather_conditions(self, count):
        fake = Faker()
        incidents = Incident.objects.all()
        for _ in range(count):
            WeatherConditions.objects.create(
                incident=random.choice(incidents),
                temperature=fake.random_number(digits=2, fix_len=True) - random.uniform(0, 20),
                humidity=fake.random_number(digits=2, fix_len=True) - random.uniform(0, 20),
                wind_speed=fake.random_number(digits=2, fix_len=True) - random.uniform(0, 20),
                weather_description=fake.sentence()
            )
            self.stdout.write(self.style.SUCCESS('Initial data for weather conditions created successfully.'))