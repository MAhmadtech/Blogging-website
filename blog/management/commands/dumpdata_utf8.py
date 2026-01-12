from django.core.management.base import BaseCommand
from django.core import serializers
from django.apps import apps
import json

class Command(BaseCommand):
    help = 'Dump data with UTF-8 encoding support'

    def handle(self, *args, **options):
        # Get all models
        models = apps.get_models()
        all_objects = {}

        # Serialize each model
        for model in models:
            try:
                model_name = f"{model._meta.app_label}.{model._meta.model_name}"
                objects = model.objects.all()
                if objects.exists():
                    serialized = serializers.serialize('python', objects)
                    all_objects[model_name] = serialized
            except Exception as e:
                self.stderr.write(f"Error serializing {model.__name__}: {str(e)}")

        # Write to file with UTF-8 encoding
        with open('mysite_data_utf8.json', 'w', encoding='utf-8') as f:
            json.dump(all_objects, f, ensure_ascii=False, indent=2)

        self.stdout.write(self.style.SUCCESS('Successfully dumped data to mysite_data_utf8.json with UTF-8 encoding'))
