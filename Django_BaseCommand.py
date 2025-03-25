from django.core.management.base import BaseCommand
from faker import Faker
from core.models import College, Program, Organization, Student, OrgMember
import random

class Command(BaseCommand):
    help = "Seed database with sample data"

    def handle(self, *args, **kwargs):
        faker = Faker()

        colleges = [College.objects.create(name=f"College of {faker.word()}", code=faker.lexify('???')) for _ in range(8)]

        programs = [Program.objects.create(name=f"Bachelor of Science in {faker.word()}", college=random.choice(colleges)) for _ in range(10)]

        orgACS = Organization.objects.create(name="ACS")
        orgSITE = Organization.objects.create(name="SITE")

        student1 = Student.objects.create(name=faker.name(), email=faker.email(), program=random.choice(programs))
        student2 = Student.objects.create(name=faker.name(), email=faker.email(), program=random.choice(programs))

        OrgMember.objects.create(student=student1, organization=orgACS)
        OrgMember.objects.create(student=student2, organization=orgSITE)

        self.stdout.write(self.style.SUCCESS("Database successfully seeded!"))



