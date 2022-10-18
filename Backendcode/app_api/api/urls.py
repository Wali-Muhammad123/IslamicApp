from django.urls import path
from .views import AnnouncementsView,prayerView,updateAnnouncement,updatePrayer
urlpatterns=[
    path('announcement/',AnnouncementsView.as_view()),
    path('prayer/',prayerView.as_view()),
    path('updateannouncement/',updateAnnouncement.as_view()),
    path('updateprayer/',updatePrayer.as_view())
]
