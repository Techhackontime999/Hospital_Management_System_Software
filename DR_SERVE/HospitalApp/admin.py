from django.contrib import admin
from .models import HospitalApp_Profile,Hospital_Management

# from .models import ServiceCategory, Service, Hospital, HospitalService

# # Registering ServiceCategory model
# @admin.register(ServiceCategory)
# class ServiceCategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')  # Show name and description in the admin list view
#     search_fields = ('name',)  # Allow search by name

# # Registering Service model
# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'service_type', 'category', 'price', 'is_available')  # Display service details
#     list_filter = ('service_type', 'is_available')  # Filter by type and availability
#     search_fields = ('name', 'category__name')  # Enable search by service name and category
#     list_editable = ('is_available',)  # Allow editing availability directly from the list view

# # Registering Hospital model
# @admin.register(Hospital)
# class HospitalAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location', 'contact_number', 'email')  # Display hospital details
#     search_fields = ('name', 'location')  # Enable search by name and location

# # Registering HospitalService model
# @admin.register(HospitalService)
# class HospitalServiceAdmin(admin.ModelAdmin):
#     list_display = ('hospital', 'service', 'availability_status', 'start_time', 'end_time')  # Display hospital services
#     list_filter = ('availability_status', 'hospital')  # Filter by availability and hospital
#     search_fields = ('hospital__name', 'service__name')  # Enable search by hospital and service name
#     list_editable = ('availability_status', 'start_time', 'end_time')  # Edit availability and timings from the list view


admin.site.register(HospitalApp_Profile)

admin.site.register(Hospital_Management)