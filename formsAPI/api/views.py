import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework import status
from datetime import datetime
from django.utils import timezone


#=======================================================================
#======================     GET Tests    ===============================
#=======================================================================

@api_view(['GET'])
def getAllTests(request):
    forms = Test.objects.all()
    serializer = TestSerializer(forms, many=True)
    return JsonResponse({'testy':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getTest(request, pk):
    test = Test.objects.get(id=pk)
    serializerT = TestSerializer(test, many=False)
    pytania = Pytanie.objects.all().filter(test=pk)
    serializerP = PytanieSerializer(pytania, many=True)
    odp = Odpowiedz.objects.all().filter(test=pk)
    serializerO = OdpowiedzSerializer(odp, many=True)
    return JsonResponse({"test":serializerT.data} | {"pytania":serializerP.data} | {"odpowiedzi":serializerO.data},
     status=status.HTTP_200_OK)

@api_view(['GET'])
def getUsersTests(request, username):
    form = Test.objects.all().filter(owner=username)
    serializer = TestSerializer(form, many=True)
    return JsonResponse({'testy':serializer.data}, status=status.HTTP_200_OK)
#=======================================================================
#======================    GET ANSWERS   ===============================
#=======================================================================

@api_view(['GET'])
def getAllAnswears(request):
    forms = Rozwiazanie.objects.all()
    serializer = RozwiazanieSerializer(forms, many=True)
    return JsonResponse({'rozwiazania':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getFormAnswears(request, formid):
    forms = Rozwiazanie.objects.all().filter(test=Test.objects.get(id=formid))
    serializer = RozwiazanieSerializer(forms, many=True)
    return JsonResponse({'rozwiazania':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getFormUserAnswears(request, formid, username):
    forms = Rozwiazanie.objects.all().filter(test=Test.objects.get(id=formid),
    ktoRozwiazal=username)
    serializer = RozwiazanieSerializer(forms, many=True)
    return JsonResponse({'rozwiazania':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAnswearsforQuestion(request, formid, questionNr):
    form = Test.objects.get(id=formid)
    answ = Rozwiazanie.objects.all().filter(test=form,
    pytanie=Pytanie.objects.get(test=form, numer=questionNr))
    serializer = RozwiazanieSerializer(answ, many=True)
    return JsonResponse({'rozwiazania':serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getAnswear(request, ansID):
    forms = Rozwiazanie.objects.get(id=ansID)
    serializer = RozwiazanieSerializer(forms, many=False)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

#=======================================================================
#======================  GET Questions   ===============================
#=======================================================================

@api_view(['GET'])
def getAllQuestions(request):
    forms = Pytanie.objects.all()
    serializer = PytanieSerializer(forms, many=True)
    return JsonResponse({'pytania':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getFormQuestions(request, formid):
    forms = Pytanie.objects.all().filter(test=Test.objects.get(id=formid))
    serializer = PytanieSerializer(forms, many=True)
    return JsonResponse({'pytania':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getQuestion(request, questionID):
    forms = Pytanie.objects.get(id=questionID)
    serializer = PytanieSerializer(forms, many=False)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

#=======================================================================
#======================  GET Odpowiedzi  ===============================
#=======================================================================

@api_view(['GET'])
def getAllOdp(request):
    forms = Odpowiedz.objects.all()
    serializer = OdpowiedzSerializer(forms, many=True)
    return JsonResponse({'odpowiedzi':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getQuestionOdp(request, questionid):
    forms = Odpowiedz.objects.all().filter(pytanie=Pytanie.objects.get(id=questionid))
    serializer = OdpowiedzSerializer(forms, many=True)
    return JsonResponse({'odpowiedzi':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getOdp(request, odpID):
    forms = Odpowiedz.objects.get(id=odpID)
    serializer = OdpowiedzSerializer(forms, many=False)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

#=======================================================================
#======================   Create Test   ===============================
#=======================================================================

@api_view(['POST'])
def addTest(request):
    serializer = TestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#=======================================================================
#======================   Create other   ===============================
#=======================================================================

@api_view(['POST'])
def addPytanie(request):
    serializer = PytanieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addOdp(request):
    serializer = OdpowiedzSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#=======================================================================
#======================    WUD Tests   =================================
#=======================================================================

@api_view(['GET','PUT', 'POST','DELETE'])
def detailTest(request, formid):
    try:
        form = Test.objects.get(id=formid)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if form.terminOtwarcia < timezone.now() > form.terminZamkniecia:
        return Response(status=status.HTTP_306_RESERVED)
    
    if request.method == 'GET':
        serializer = TestSerializer(form, many=False)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TestSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST' :
        if request.POST.get('delete', False):
            form.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = TestSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#=======================================================================
#======================   WUD Answers  =================================
#=======================================================================

@api_view(['GET','PUT', 'POST','DELETE'])
def detailAnswear(request, answId):
    try:
        answ = Rozwiazanie.objects.get(id=answId)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RozwiazanieSerializer(answ, many=False)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = RozwiazanieSerializer(answ, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST' :
        if request.POST.get('delete', False):
            answ.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = RozwiazanieSerializer(answ, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        answ.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#=======================================================================
#======================   WUD Others   =================================
#=======================================================================

@api_view(['GET','PUT', 'POST','DELETE'])
def detailPytanie(request, pytanie):
    try:
        user = Pytanie.objects.get(id=pytanie)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PytanieSerializer(user, many=False)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = PytanieSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST' :
        if request.POST.get('delete', False):
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PytanieSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT', 'POST','DELETE'])
def detailOdp(request, odp):
    try:
        user = Odpowiedz.objects.get(id=odp)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OdpowiedzSerializer(user, many=False)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = OdpowiedzSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST' :
        if request.POST.get('delete', False):
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = OdpowiedzSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#=======================================================================
#======================   Add Test V   =================================
#=======================================================================


@api_view(['POST'])
def addTestV(request):
    getted = json.loads(request.body)
    result = []
    for entry in getted:
        result.append({entry.get('name'):entry.get('value')})
    test = Test.objects.create(tytul=result[0].get("test-title"), opis='done',owner="user",czasTrwania=34232,terminOtwarcia=datetime.now(),
    terminZamkniecia=datetime.now())
    test.save()
    ###################
    questionTitle = 'question-title'
    checkbox = 'checkbox-answer[]'
    answ = 'input-answer[]'
    ###################
    nrPytania = 0
    czyPoprawnaOdp = False
    for dict in result:
        if questionTitle in dict.keys():
            if dict.get(questionTitle) == '' or dict.get(questionTitle) == None:
                continue
            nrPytania+=1
            Pytanie.objects.create(numer=nrPytania, tresc=dict.get(questionTitle), test=test)
        elif checkbox in dict.keys():
            czyPoprawnaOdp = True
        elif answ in dict.keys():
            if dict.get(answ) == '' or dict.get(answ) == None:
                continue
            Odpowiedz.objects.create(tresc=dict.get(answ), test=test, 
            pytanie=Pytanie.objects.get(numer=nrPytania, test=test), czyPoprawna=czyPoprawnaOdp)
            czyPoprawnaOdp = False

    # for nr, tr, zam in zip(result.get('numerP'),result.get('trescPyt'),result.get('zamkniete')):
    #     if Pytanie.objects.filter(test=test.id, numer=nr):
    #         continue
    #     Pytanie.objects.create(numer=nr, tresc=tr, zamkniete=zam, test=test)
    # if result.get('poprawna', False):
    #     for nr, tr, pop in zip(result.get('numerPOdp'),result.get('trescOdp'),result.get('poprawna')):
    #         Odpowiedz.objects.create(pytanie=Pytanie.objects.get(test=test.id,numer=nr), tresc=tr, czyPoprawna=pop, test=test)
    # else:
    #     for nr, tr in zip(result.get('numerPOdp'),result.get('trescOdp')):
    #         Odpowiedz.objects.create(pytanie=Pytanie.objects.get(test=test.id,numer=nr), tresc=tr, czyPoprawna=False, test=test)
    return Response(status=status.HTTP_201_CREATED)



@api_view(['GET'])
def getWynik(request, nickname, testid):
    test = Test.objects.get(id=testid)
    pkt = 0
    max = 0
    for roz in Rozwiazanie.objects.filter(test=testid, ktoRozwiazal=nickname):
        try:
            if Odpowiedz.objects.get(pytanie=roz.pytanie, czyPoprawna=True).tresc == roz.odpowiedz:
                pkt+=1
        except:
            pass
        max+=1
    return JsonResponse({"wynik":pkt,"maxWynik":max}, status=status.HTTP_200_OK)


@api_view(['POST'])
def addRozwiazanie(request):
    result = json.loads(request.body)
    test = Test.objects.get(id=result.get('test'))
    kto = result.get('ktoRozwiazal')
    pkt = 0
    max = 0
    if isinstance(result.get('pytanie'), int):
        pyt=result.get('pytanie')
        Rozwiazanie.objects.create(ktoRozwiazal=result.get('ktoRozwiazal'), 
        odpowiedz=result.get('odpowiedz'), test=test,
        pytanie=Pytanie.objects.get(numer=pyt, test=test))
        return Response(status=status.HTTP_201_CREATED)
    for odp, pyt in zip(result.get('odpowiedz'),result.get('pytanie')):
        pytanie = Pytanie.objects.get(numer=pyt, test=test)
        Rozwiazanie.objects.create(ktoRozwiazal=kto, odpowiedz=odp, test=test,
        pytanie=pytanie)
    return Response(status=status.HTTP_201_CREATED)
