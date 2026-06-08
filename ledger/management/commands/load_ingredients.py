from django.core.management.base import BaseCommand
from ledger.models import Ingredient


class Command(BaseCommand):
    help = "Load default ingredients"

    def handle(self, *args, **options):
        ingredients = [
            'kosher salt', 'sea salt',
            'black pepper', 'peppercorns', 'cayenne pepper',
            'chili powder', 'curry powder', 'onion powder', 'garlic powder',
            'vanilla extract', 'water', 'apple cider vinegar',
            'balsamic vinegar', 'red wine vinegar', 'rice vinegar',
            'olive oil', 'Worcestershire sauce', 'soy sauce', 'canola oil',
            'ketchup', 'mayonaise', 'mustard', 'hot sauce', 'chili sauce',
            'salted butter', 'unsalted butter', 'flour', 'eggs',
            'light brown sugar', 'granulated sugar', 'cornstarch',
            'all-purpose flour', 'baking powder', 'baking soda', 
            'milk', 'plain yogurt', 'honey',
            'parmesan', 'mozzarella', 'cheddar cheese', 'feta',
            'chicken', 'ground beef', 'pork', 
            'rice', 'rolled oat',
            'tomato paste', 'tomato sauce',  'chicken broth',
            'penne pasta',
            'carrot', 'garlic', 'red onion', 'yellow onion', 
            'potato',  'couscous', 'lentil',
            'lemon', 'strawberry', 'blackberry', 'blueberry',
            'apple', 'apricot', 'orange',
            'almond', 'peanut', 'sunflower', 
            'parsley', 'thyme leaves', 'bay leaves', 'oregano',
            'cinnamon', 'cloves', 'nutgmeg', 'ginger',
            'peas', 'spinach',
            'edamame', 'broccoli', 'corn', 'chickpeas',

        ]
        for name in ingredients:
           Ingredient.objects.get_or_create(name=name)
           self.stdout.write(f'Added: {name}')

        self.stdout.write(
            self.style.SUCCESS('DONE!')
        )