import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')
django.setup()

from properties.models import Property

# Sample property data
properties_data = [
    {
        'title': 'Modern Downtown Apartment',
        'description': 'Beautiful modern apartment in the heart of downtown with stunning city views. Features include hardwood floors, stainless steel appliances, and a private balcony.',
        'property_type': 'apartment',
        'status': 'for_sale',
        'price': 450000,
        'bedrooms': 2,
        'bathrooms': 2,
        'area': 1200,
        'address': '123 Main Street',
        'city': 'New York',
        'state': 'NY',
        'zip_code': '10001'
    },
    {
        'title': 'Spacious Family House',
        'description': 'Perfect family home with large backyard, updated kitchen, and excellent schools nearby. This house offers comfort and convenience for growing families.',
        'property_type': 'house',
        'status': 'for_sale',
        'price': 650000,
        'bedrooms': 4,
        'bathrooms': 3,
        'area': 2400,
        'address': '456 Oak Avenue',
        'city': 'Los Angeles',
        'state': 'CA',
        'zip_code': '90210'
    },
    {
        'title': 'Luxury Condo with Ocean View',
        'description': 'Stunning luxury condominium with panoramic ocean views. Features premium finishes, private elevator access, and resort-style amenities.',
        'property_type': 'condo',
        'status': 'for_sale',
        'price': 850000,
        'bedrooms': 3,
        'bathrooms': 2,
        'area': 1800,
        'address': '789 Beach Drive',
        'city': 'Miami',
        'state': 'FL',
        'zip_code': '33101'
    },
    {
        'title': 'Cozy Studio for Rent',
        'description': 'Perfect studio apartment for young professionals. Located in trendy neighborhood with easy access to public transportation and entertainment.',
        'property_type': 'apartment',
        'status': 'for_rent',
        'price': 2500,
        'bedrooms': 1,
        'bathrooms': 1,
        'area': 600,
        'address': '321 Creative Street',
        'city': 'San Francisco',
        'state': 'CA',
        'zip_code': '94102'
    },
    {
        'title': 'Elegant Townhouse',
        'description': 'Beautifully maintained townhouse in quiet residential area. Features include updated bathrooms, modern kitchen, and private garage.',
        'property_type': 'townhouse',
        'status': 'for_sale',
        'price': 520000,
        'bedrooms': 3,
        'bathrooms': 2,
        'area': 1600,
        'address': '654 Maple Lane',
        'city': 'Chicago',
        'state': 'IL',
        'zip_code': '60601'
    },
    {
        'title': 'Luxury Villa with Pool',
        'description': 'Magnificent villa with private pool, landscaped gardens, and premium finishes throughout. Perfect for entertaining and luxury living.',
        'property_type': 'villa',
        'status': 'for_sale',
        'price': 1250000,
        'bedrooms': 5,
        'bathrooms': 4,
        'area': 3500,
        'address': '987 Hillcrest Boulevard',
        'city': 'Beverly Hills',
        'state': 'CA',
        'zip_code': '90210'
    }
]

# Create properties
for prop_data in properties_data:
    property_obj, created = Property.objects.get_or_create(
        title=prop_data['title'],
        defaults=prop_data
    )
    if created:
        print(f"Created property: {property_obj.title}")
    else:
        print(f"Property already exists: {property_obj.title}")

print(f"Total properties in database: {Property.objects.count()}")
