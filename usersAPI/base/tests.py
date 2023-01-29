from rest_framework import status
from rest_framework.test import APITestCase
from api.serializers import *
from base.models import *

class AddTestCase(APITestCase):

    def test_addModerator(self):
        data = {"email":"m@onet.pl","imie":"s","nazwisko":"sdf","nickname":"frist",
        "haslo":"sdf"}
        response = self.client.post("/addModerator/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_addUser(self):
        data = {"email":"m@onet.pl","imie":"s","nazwisko":"sdf","nickname":"second",
        "haslo":"sdf"}
        response = self.client.post("/addUser/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_addBusinessUser(self):
        data = {"email":"m@onet.pl","imie":"s","nazwisko":"sdf","nickname":"third",
        "haslo":"sdf", "creditCardExpirationDate":"sdf"}
        response = self.client.post("/addBusinessUser/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

##########################################################################
##########################################################################
##########################################################################

class getLoginUpdateTestCase(APITestCase):

    def setUp(self):
        data = {"email":"m@onet.pl","imie":"s","nazwisko":"sdf","nickname":"first",
        "haslo":"sdf"}
        response = self.client.post("/addModerator/", data)
        data = {"email":"m@onet.pl","imie":"s","nazwisko":"sdf","nickname":"second",
        "haslo":"sdf"}
        response = self.client.post("/addUser/", data)
        data = {"email":"m@onet.pl","imie":"s","nazwisko":"sdf","nickname":"third",
        "haslo":"sdf", "creditCardExpirationDate":"sdf"}
        response = self.client.post("/addBusinessUser/", data)

    #=============================================================#

    def test_getAllModerators(self):
        response = self.client.get("/getAllModerators/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAllUsers(self):
        response = self.client.get("/getAllUsers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAllBusinessUsers(self):
        response = self.client.get("/getAllBusinessUsers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAllNicknames(self):
        response = self.client.get("/getAllNicknames/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    #=============================================================#

    def test_loginUser(self):
        data = {"nickname":"third",
        "haslo":"sdf"}
        response = self.client.post("/loginUser/", data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)


    def test_loginModerator(self):
        data = {"nickname":"first",
        "haslo":"sdf"}
        response = self.client.post("/loginModerator/", data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    #=============================================================#

    def test_detailModerator(self):
        response = self.client.get("/detailModerator/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detailUser(self):
        response = self.client.get("/detailUser/second")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detailBusinessUser(self):
        response = self.client.get("/detailBusinessUser/third")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #=============================================================#

    def test_detailModerator(self):
        data = {"email":"m@onet.pl","imie":"sasas","nazwisko":"sdxDf","nickname":"first",
        "haslo":"ssssdf"}
        response = self.client.post("/detailModerator/1", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_detailUser(self):
        data = {"email":"m@onet.pl","imie":"ssdsfds","nazwisko":"sdf","nickname":"second",
        "haslo":"sdwwwwwwwf"}
        response = self.client.post("/detailUser/second", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detailBusinessUser(self):
        data = {"email":"m@onet.pl","imie":"sadsf","nazwisko":"ssdfddf","nickname":"third",
        "haslo":"sdfXXX", "creditCardExpirationDate":"sdsf"}
        response = self.client.post("/detailBusinessUser/third", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


##########################################################################
##########################################################################
##########################################################################

class blockSubUnsubTestCase(APITestCase):

    def setUp(self):
        data = {"email":"m@onet.pl","imie":"s","nazwisko":"sdf","nickname":"second",
        "haslo":"sdf"}
        response = self.client.post("/addUser/", data)
        data = {"email":"m@onet.pl","imie":"s","nazwisko":"sdf","nickname":"third",
        "haslo":"sdf", "creditCardExpirationDate":"sdf"}
        response = self.client.post("/addBusinessUser/", data)

    #=============================================================#

    def test_blockUser(self):
        response = self.client.get("/block/second")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscribe(self):
        data = {"creditCardExpirationDate":"sdf"}
        response = self.client.post("/subscribe/second", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unsubscribe(self):
        data = {}
        response = self.client.post("/unsubscribe/third", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

##########################################################################
##########################################################################
##########################################################################

class deleteTestCase(APITestCase):

    def setUp(self):
        data = {"email":"m@onet.pl","imie":"s","nazwisko":"sdf","nickname":"frist",
        "haslo":"sdf"}
        response = self.client.post("/addModerator/", data)
        data = {"email":"m@onet.pl","imie":"s","nazwisko":"sdf","nickname":"second",
        "haslo":"sdf"}
        response = self.client.post("/addUser/", data)
        data = {"email":"m@onet.pl","imie":"s","nazwisko":"sdf","nickname":"third",
        "haslo":"sdf", "creditCardExpirationDate":"sdf"}
        response = self.client.post("/addBusinessUser/", data)

    def test_detailModerator(self):
        data = {"delete":1}
        response = self.client.post("/detailModerator/1", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_detailUser(self):
        data = {"delete":1}
        response = self.client.post("/detailUser/second", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_detailBusinessUser(self):
        data = {"delete":1}
        response = self.client.post("/detailBusinessUser/third", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    