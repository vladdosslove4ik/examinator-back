from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('getAllModerators/', views.getAllModerators),
    path('detailModerator/<int:pk>', views.detailModerator),
    path('addModerator/', views.addModerator), ### Dodawanie moderatora jeśli trzeba
    ###########################################
    path('getAllUsers/', views.getAllUsers), 
    path('detailUser/<str:nick>', views.detailUser),
    path('addUser/', views.addUser), ### dodawanie aka resjestracja użytkownika, jeśli nickname już istnieje to zwraca json, gdzie możesz error wypisać
    ###########################################
    path('getAllBusinessUsers/', views.getAllBusinessUsers),
    path('detailBusinessUser/<str:nick>', views.detailBusinessUser),
    path('addBusinessUser/', views.addBusinessUser), ### Dodawanie aka rejestracja biznesowego jeśli odrazu biznesowe zakłada
    ###########################################
    path('getAllNicknames/', views.getAllNickNames), ### Aby sprawdzić czy nicknama już nie ma, nie można dwóch tych samych dla użytkowników
    path('loginUser/', views.loginUser), ### Zaloguj użytkownika
    path('loginModerator/', views.loginModerator), ### Zaloguj moderatora
    path('subscribe/<str:nick>', views.subscribe), ### Upgrade konta zwykłego użytkownika na użytkownika biznesowego
    path('unsubscribe/<str:nick>', views.unsubscribe), ### degrade biznesowego na zwykłego
    path('block/<str:username>', views.blockUser), ### Zablokowanie użytkownika o nicku username
]

urlpatterns = format_suffix_patterns(urlpatterns)
