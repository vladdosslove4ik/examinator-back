from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('getAllTests/', views.getAllTests), ### Dostajesz obiekty testów wszysktich w jsonie
    path('getTest/<int:pk>', views.getTest), ### Dostajesz obiekt testu i jego pytań i odp w jsonie
    path('getUsersTests/<str:username>', views.getUsersTests),
    path('getAllAnswears/', views.getAllAnswears),
    path('getFormAnswears/<int:formid>', views.getFormAnswears),
    path('getFormUserAnswears/<int:formid>/<str:username>', views.getFormUserAnswears),
    path('getAnswearsForQuestion/<int:formid>/<int:questionNr>', views.getAnswearsforQuestion),
    path('getAnswear/<int:ansID>', views.getAnswear),
    path('getAllQuestions/', views.getAllQuestions),
    path('getFormQuestions/<int:formid>', views.getFormQuestions),
    path('getQuestion/<int:questionID>', views.getQuestion),
    path('getAllOdp/', views.getAllOdp),
    path('getQuestionOdp/<int:questionid>', views.getQuestionOdp),
    path('getOdp/<int:odpID>', views.getOdp),
    path('addTest/', views.addTest),
    path('addTestV/', views.addTestV), ### Dodawanie testu z odp i pytaniami (Przykład w README)
    path('addPytanie/', views.addPytanie),
    path('addRozwiazanie/', views.addRozwiazanie), ### Dodaj rozwiązanie wysyłając posta z jsonem
    ### Musisz podać w jsonie zmienne jak 'test' czyli id testu, 'ktoRozwiazal' - nickname kto roziwazal, 
    ### 'pytanie' - numer pytania(wiele ich może być), 'odpowiedz' - tresc odpowiedzi
    path('addOdp/', views.addOdp),
    path('detailTest/<int:formid>', views.detailTest),
    path('detailAnswear/<int:answId>', views.detailAnswear),
    path('detailPytanie/<int:pytanie>', views.detailPytanie),
    path('detailOdp/<int:odp>', views.detailOdp),
]

urlpatterns = format_suffix_patterns(urlpatterns)
