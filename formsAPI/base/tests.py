from rest_framework import status
from rest_framework.test import APITestCase
from api.serializers import *
from base.models import *
from datetime import datetime
import json

class AddOthersTestCase(APITestCase):

    def setUp(self):
        data = {"tytul":"s","opis":"s","owner":"test","czasTrwania":1,
        "terminOtwarcia":datetime.now(),"terminZamkniecia":datetime.now()}
        response = self.client.post("/addTest/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = {"numer":1,"tresc":"s","zamkniete":True,"test":1}
        response = self.client.post("/addPytanie/", data)
        data = {"numer":2,"tresc":"s","zamkniete":True,"test":1}
        response = self.client.post("/addPytanie/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_addRozwiazanie(self):
        data = {"pytanie":1,"pytanie":2,"odpowiedz":"s","odpowiedz":"b","test":1, "ktoRozwiazal":"ja"}
        response = self.client.post("/addRozwiazanie/", json.dumps(data),
                                content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_addOdp(self):
        data = {"czyPoprawna":True,"tresc":"s","pytanie":1,"test":1}
        response = self.client.post("/addOdp/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

##########################################################################

class AddPytanieTest(APITestCase):

    def setUp(self):
        data = {"tytul":"s","opis":"s","owner":"test","czasTrwania":1,
        "terminOtwarcia":datetime.now(),"terminZamkniecia":datetime.now()}
        response = self.client.post("/addTest/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_addPytanie(self):
        data = {"numer":1,"tresc":"s","zamkniete":True,"test":1}
        response = self.client.post("/addPytanie/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

##########################################################################

class AddTestCase(APITestCase):

    def test_addTest(self):
        data = {"tytul":"s","opis":"s","owner":"badanie","czasTrwania":1,
        "terminOtwarcia":datetime.now(),"terminZamkniecia":datetime.now()}
        response = self.client.post("/addTest/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

   
##########################################################################
##########################################################################
##########################################################################

class GetsAndUpdatesTestCase(APITestCase):
    def setUp(self):
        data = {"tytul":"s","opis":"s","owner":"test","czasTrwania":1,
        "terminOtwarcia":datetime.now(),"terminZamkniecia":datetime.now()}
        response = self.client.post("/addTest/", data)
        data = {"numer":1,"tresc":"s","zamkniete":True,"test":1}
        response = self.client.post("/addPytanie/", data)
        data = {"owner":"test","pytanie":1,"odpowiedz":"s","test":1}
        response = self.client.post("/addRozwiazanie/", json.dumps(data),
                                content_type="application/json")
        data = {"czyPoprawna":True,"tresc":"s","pytanie":1,"test":1}
        response = self.client.post("/addOdp/", data)

    #======================================================#

    def test_getAllTests(self):
        response = self.client.get("/getAllTests/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_getTest(self):
        response = self.client.get("/getTest/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getUsersTests(self):
        response = self.client.get("/getUsersTests/test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #======================================================#

    def test_getAllAnswears(self):
        response = self.client.get("/getAllAnswears/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_getFormAnswears(self):
        response = self.client.get("/getFormAnswears/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFormUserAnswears(self):
        response = self.client.get("/getFormUserAnswears/1/test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAnswearsForQuestion(self):
        response = self.client.get("/getAnswearsForQuestion/1/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAnswear(self):
        response = self.client.get("/getAnswear/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #======================================================#

    def test_getAllQuestions(self):
        response = self.client.get("/getAllQuestions/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_getFormQuestions(self):
        response = self.client.get("/getFormQuestions/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getQuestion(self):
        response = self.client.get("/getQuestion/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #======================================================#

    def test_getAllOdp(self):
        response = self.client.get("/getAllOdp/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getQuestionOdp(self):
        response = self.client.get("/getQuestionOdp/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getOdp(self):
        response = self.client.get("/getOdp/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #======================================================#

    def test_detailTest(self):
        response = self.client.get("/detailTest/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detailAnswear(self):
        response = self.client.get("/detailAnswear/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_detailPytanie(self):
        response = self.client.get("/detailPytanie/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detailOdp(self):
        response = self.client.get("/detailOdp/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

##########################################################################
##########################################################################
##########################################################################
class UpdateTestCase(APITestCase):
    def setUp(self):
        data = {"tytul":"s","opis":"s","owner":"test","czasTrwania":1,
        "terminOtwarcia":datetime.now(),"terminZamkniecia":datetime.now()}
        response = self.client.post("/addTest/", data)
        data = {"numer":1,"tresc":"s","zamkniete":True,"test":1}
        response = self.client.post("/addPytanie/", data)
        data = {"ktoRozwiazal":"test","pytanie":1,"odpowiedz":"s","test":1}
        response = self.client.post("/addRozwiazanie/", json.dumps(data),
                                content_type="application/json")
        data = {"czyPoprawna":True,"tresc":"s","pytanie":1,"test":1}
        response = self.client.post("/addOdp/", data)  


    def test_detailTest(self):
        data = {"tytul":"22s","opis":"123124124s","owner":"test","czasTrwania":1,
        "terminOtwarcia":datetime.now(),"terminZamkniecia":datetime.now()}
        response = self.client.post("/detailTest/1", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detailAnswear(self):
        data = {"owner":"test","pytanie":1,"odpowiedz":"s","test":1}
        response = self.client.post("/detailAnswear/1", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_detailPytanie(self):
        data = {"numer":1,"tresc":"s","zamkniete":True,"test":1}
        response = self.client.post("/detailPytanie/1", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detailOdp(self):
        data = {"czyPoprawna":False,"tresc":"sdfg","pytanie":1, "test":1}
        response = self.client.post("/detailOdp/1", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

##########################################################################
##########################################################################
##########################################################################

class DeleteOthersTestCase(APITestCase):
    def setUp(self):
        data = {"tytul":"s","opis":"s","owner":"test","czasTrwania":1,
        "terminOtwarcia":datetime.now(),"terminZamkniecia":datetime.now()}
        response = self.client.post("/addTest/", data)
        data = {"numer":1,"tresc":"s","zamkniete":True,"test":1}
        response = self.client.post("/addPytanie/", data)
        data = {"ktoRozwiazal":"test","pytanie":1,"odpowiedz":"s","test":1}
        response = self.client.post("/addRozwiazanie/", json.dumps(data),
                                content_type="application/json")
        data = {"czyPoprawna":True,"tresc":"s","pytanie":1,"test":1}
        response = self.client.post("/addOdp/", data)

    def test_detailAnswear(self):
        data = {"delete":"x"}
        response = self.client.post("/detailAnswear/1", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
   

    def test_detailOdp(self):
        data = {"delete":"x"}
        response = self.client.post("/detailOdp/1", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class DeletePytanieTestCase(APITestCase):
    def setUp(self):
        data = {"tytul":"s","opis":"s","owner":"test","czasTrwania":1,
        "terminOtwarcia":datetime.now(),"terminZamkniecia":datetime.now()}
        response = self.client.post("/addTest/", data)
        data = {"numer":1,"tresc":"s","zamkniete":True,"test":1}
        response = self.client.post("/addPytanie/", data)

    def test_detailPytanie(self):
        data = {"delete":"x"}
        response = self.client.post("/detailPytanie/1", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class DeleteFormsTestCase(APITestCase):
    def setUp(self):
        data = {"tytul":"s","opis":"s","owner":"test","czasTrwania":1,
        "terminOtwarcia":datetime.now(),"terminZamkniecia":datetime.now()}
        response = self.client.post("/addTest/", data)


    def test_detailTest(self):
        data = {"delete":"x"}
        response = self.client.post("/detailTest/1", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)