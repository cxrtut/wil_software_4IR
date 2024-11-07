from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from RentBox.models import Available_Equipment, Tent, Decor, Catering, Seatings, Miscellaneous

class Command(BaseCommand):
    help = "Populate the Equipment model with data from Tent, Decor, Catering, Seatings, and Miscellaneous models"

    def handle(self, *args, **kwargs):
        models = [
            (Tent, 'Tent'),
            (Decor, 'Decor'),
            (Catering, 'Catering'),
            (Seatings, 'Tables_and_Chairs'),
            (Miscellaneous, 'Miscellaneous')
        ]

        for model, type_name in models:
            content_type = ContentType.objects.get_for_model(model)
            for item in model.objects.all():
                Available_Equipment.objects.create(
                    name=item.name,
                    equipment_type=type_name,
                    price_per_day=item.price_per_day,
                    quantity=item.quantity,
                    description=item.desc,
                    content_type=content_type,
                    object_id=item.id
                )
        self.stdout.write(self.style.SUCCESS("Equipment model populated successfully."))
