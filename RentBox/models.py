from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True, default='guest')  
    email = models.EmailField(max_length=50, unique=True, null=True)
    password = models.CharField(max_length=128)  
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    def set_password(self, raw_password):
        """Hashes the password."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Verifies the password."""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

class InventoryItem(models.Model):
    name = models.CharField(max_length=264, unique=True)
    desc = models.CharField(max_length=264, null=False)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantity = models.IntegerField(null=False)
    replacement_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    image_url = models.CharField(max_length=265, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Tent(InventoryItem):
    dimensions = models.CharField(max_length=10, null=False)

class Decor(InventoryItem):
    pass

class Catering(InventoryItem):
    pass

class Miscellaneous(InventoryItem):
    pass

class Seatings(InventoryItem):
    pass

class Organiser(models.Model):
    bus_name = models.CharField(max_length=250, primary_key=True)
    bus_loc =  models.TextField(max_length=250, null= False)
    bus_email =  models.CharField(max_length=250, null= False)
    bus_phone =  models.CharField(max_length=250, null= False)
    bus_services =  models.CharField(max_length=250, null= False)
    add_info =  models.TextField(max_length=300, null= False)

    def __str__(self):
        return self.bus_name
    
class Available_Equipment(models.Model):
    EQUIPMENT_TYPES = (
        ('Tent', 'Tent'),
        ('Decor', 'Decor'),
        ('Catering', 'Catering'),
        ('Tables_and_Chairs', 'Tables and Chairs'),
        ('Miscellaneous', 'Miscellaneous')
    )

    name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=20, choices=EQUIPMENT_TYPES)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    specific_equipment = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.name} ({self.equipment_type})"
    
class BookedEquipment(models.Model):
        name = models.ForeignKey(Available_Equipment, on_delete=models.CASCADE, related_name="booked_items")
        start_date = models.DateField()
        end_date = models.DateField()
        quantity = models.PositiveIntegerField()

        def __str__(self):
            return f"{self.name.name} booked from {self.start_date} to {self.end_date}"