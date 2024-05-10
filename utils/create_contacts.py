"""
This script generates and inserts a large number of fake contact objects into
a Django project.

**Functionality:**

1. **Configuration:**
    - Defines the base directory of the Django project (`DJANGO_BASE_DIR`).
    - Sets the number of contact objects to generate (`NUMBER_OF_OBJECTS`).
    - Configures the Django environment by adding the project path and
    setting the settings module.
    - Disables time zone support for the script (optional, might be 
    needed depending on your model).

2. **Data Generation:**
    - Creates a `Faker` instance for generating data in Brazilian Portuguese
    (`pt_BR`).
    - Defines a list of category names (`categories`).
    - Creates and saves Django `Category` objects from the list.
    - Iterates the specified number of times (`NUMBER_OF_OBJECTS`):
        - Generates a fake profile using `faker.profile()`.
        - Extracts email, first and last names, phone number, and description.
        - Selects a random category from the created categories.
        - Creates a new Django `Contact` object with the generated data and
          appends it to a list.

3. **Bulk Insertion:**
    - Checks if any `Contact` objects were created.
    - If the list is not empty, uses `Contact.objects.bulk_create()` to
    efficiently insert all objects at once.

**Usage:**

1. Save this script in your Django project directory.
2. Modify `NUMBER_OF_OBJECTS` to the desired number of contacts.
3. Ensure your `Contact` model has appropriate fields defined.
4. Run the script using `python script_name.py`.

**Notes:**

- This script assumes you have a working Django project with a `Contact` model
and `Category` model (if used).
- Adjust the `categories` list and `Faker` configuration for different data
requirements.
- Consider database capacity when setting `NUMBER_OF_OBJECTS`.
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact

    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)
