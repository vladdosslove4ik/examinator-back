from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework import status
from itertools import chain


#=======================================================================
#=====================    MODERATORS    ================================
#=======================================================================

@api_view(['GET'])
def getAllModerators(request, format=None):
    moderators = Moderator.objects.all()
    serializer = ModeratorSerializer(moderators, many=True)
    return JsonResponse({'moderators':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET','PUT', 'POST','DELETE'])
def detailModerator(request, pk):
    try:
        moderator = Moderator.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ModeratorSerializer(moderator, many=False)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        serializer = ModeratorSerializer(moderator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST' :
        if request.POST.get('delete', False):
            moderator.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ModeratorSerializer(moderator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        moderator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def addModerator(request):
    serializer = ModeratorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


#=======================================================================
#======================      USERS       ===============================
#=======================================================================

@api_view(['GET'])
def getAllUsers(request, format=None):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'users':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET','PUT', 'POST','DELETE'])
def detailUser(request, nick):
    try:
        user = User.objects.get(nickname=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user, many=False)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST' :
        if request.POST.get('delete', False):
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def addUser(request):
    if User.objects.get(nickname=request.POST['nickname']):
        return JsonResponse({"error":"This nickname already exists"}, status=status.HTTP_226_IM_USED)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#=======================================================================
#========================  BUSINESS USERS  =============================
#=======================================================================

@api_view(['GET'])
def getAllBusinessUsers(request, format=None):
    users = BusinessUser.objects.all()
    serializer = BusinessUserSerializer(users, many=True)
    return JsonResponse({'businessUsers':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET','PUT', 'POST','DELETE'])
def detailBusinessUser(request, nick):
    try:
        user = BusinessUser.objects.get(nickname=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BusinessUserSerializer(user, many=False)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        serializer = BusinessUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST' :
        if request.POST.get('delete', False):
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = BusinessUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def addBusinessUser(request):
    if User.objects.get(nickname=request.POST['nickname']):
        return JsonResponse({"error":"This nickname already exists"}, status=status.HTTP_226_IM_USED)
    serializer = BusinessUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)



#=======================================================================
#========================      LOGINS      =============================
#=======================================================================

@api_view(['GET'])
def getAllNickNames(request):
    busers = BusinessUser.objects.all().values('nickname')
    users = User.objects.all().values('nickname')
    nicknames = list(chain(users, busers))
    nicknames = [d['nickname'] for d in nicknames]
    return JsonResponse({'nicknames':nicknames}, status=status.HTTP_200_OK)

def makePayment(user):
    user.startSubscriptionDate = datetime.today
    user.save()

@api_view(['POST'])
def loginUser(request):
    users = User.objects.all().exclude(blocked=True)
    for user in users:
        if request.POST.get('nickname', False) == user.nickname:
            if request.POST.get('haslo', False == user.haslo):
                if user.blocked:
                    return Response(status=status.HTTP_403_FORBIDDEN)
                result = {"nickname":user.nickname,"haslo":user.haslo}
                if isinstance(user, BusinessUser):
                    if datetime.today - user.startSubscriptionDate >= 30:
                        makePayment(user)
                    result['business'] = True
                return JsonResponse(result, status=status.HTTP_202_ACCEPTED)
            else:
                return JsonResponse({"nickname":user.nickname}, status=status.HTTP_302_FOUND)
    return JsonResponse({"invalid": 0}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def loginModerator(request):
    mods = Moderator.objects.all()
    for mod in mods:
        if request.POST.get('nickname', False) == mod.nickname:
            if request.POST.get('haslo', False == mod.haslo):
                return JsonResponse({"nickname":mod.nickname,"haslo":mod.haslo}, status=status.HTTP_202_ACCEPTED)
            else:
                return JsonResponse({"nickname":mod.nickname}, status=status.HTTP_302_FOUND)
    return JsonResponse({"invalid": 0}, status=status.HTTP_404_NOT_FOUND)


#=======================================================================
#========================   SUBSCRIPTION   =============================
#=======================================================================

@api_view(['POST'])
def subscribe(request, nick):
    try:
        user = User.objects.get(nickname=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    userData = [user.email, user.nazwisko, user.imie, user.nickname, user.haslo]
    user.delete()
    buser = BusinessUser(email=userData[0],nickname=userData[3],imie=userData[2],
    nazwisko=userData[1],haslo=userData[4],
    creditCardNumber=request.POST.get('creditCardNumber', False),
    creditCardExpirationDate=request.POST['creditCardExpirationDate'],
    creditCardCode=request.POST.get('creditCardCode', False)
    )
    buser.save()
    serializer = BusinessUserSerializer(buser, many=False)
    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def unsubscribe(request, nick):
    try:
        user = BusinessUser.objects.get(nickname=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    userData = [user.email, user.nazwisko, user.imie, user.nickname, user.haslo]
    user.delete()
    nuser = User(email=userData[0],nickname=userData[3],imie=userData[2],
    nazwisko=userData[1],haslo=userData[4])
    nuser.save()
    serializer = UserSerializer(nuser, many=False)
    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
   
#=======================================================================
#========================     Blocking     =============================
#=======================================================================

@api_view(['GET'])
def blockUser(request, username):
    user = User.objects.get(nickname=username)
    if user.blocked:
        return Response(status=status.HTTP_208_ALREADY_REPORTED)
    user.blocked = True
    user.save()
    return Response(status=status.HTTP_200_OK)