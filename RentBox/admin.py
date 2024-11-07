# admin.py
from django.contrib import admin
from RentBox.models import  Customer, Tent, Decor, Catering, Miscellaneous, Seatings, Organiser, Available_Equipment, BookedEquipment


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'mobile', 'address')  
    search_fields = ('username', 'email')

admin.site.register(Customer, CustomerAdmin)

admin.site.register(Tent)
admin.site.register(Decor)
admin.site.register(Catering)
admin.site.register(Miscellaneous)
admin.site.register(Seatings)

admin.site.register(Organiser)
admin.site.register(Available_Equipment)
admin.site.register(BookedEquipment)