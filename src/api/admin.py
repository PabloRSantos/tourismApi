from django.contrib import admin
from api.models.attractions import Attraction
from api.models.comments import Comments
from api.models.location import Location
from api.models.reviews import Reviews
from api.models.tourism_spot import TourismSpot
from api.actions.comments import approve_comment, disapprove_comment


class AdminComment(admin.ModelAdmin):
    list_display = '__all__'
    actions = [approve_comment, disapprove_comment]


admin.site.register(TourismSpot)
admin.site.register(Attraction)
admin.site.register(Comments, AdminComment)
admin.site.register(Reviews)
admin.site.register(Location)
