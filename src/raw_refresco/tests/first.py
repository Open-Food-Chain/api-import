# from django.utils.http import urlencode
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import RawRefresco
import views
import pytest


class RawRefrescoTests(APITestCase):

    @pytest.fixture
    def api_client():
        from rest_framework.test import APIClient
        return APIClient()

    @pytest.mark.django_db
    def test_unauthorized_request(api_client):
        url = reverse('need-token-url')
        response = api_client.get(url)
        assert response.status_code == 401

    def post_rawrefresco(self, data):
        url = reverse(views.RawRefrescoView)
        response = self.client.post(url, data, format='json')
        return response

    @pytest.mark.django_db
    def test_post_and_get_rawrefresco(self):
        """
        Ensure we can create a new DroneCategory and then retrieve it
        """
        data = {
            "anfp": "18505100",
            "dfp": "Description here",
            "bnfp": "448528",
            "pds": "2020-02-12",
            "pde": "2020-02-20",
            "jds": 43,
            "jde": 51,
            "bbd": "2020-05-20",
            "pc": "DE",
            "pl": "Herrath",
            "rmn": "11200100520",
            "rmn": "11200100520",
            "pon": "3895814603",
            "pop": "714",
            "raw_json": "eyBcImFuZnBcIjogXCIxODUwNTEwMFwiLFwiZGZwXCI6IFwiRGVzY3JpcHRpb24gaGVyZVwiLFwiYm5mcFwiOiBcIjQ0ODUyOFwiLFwicGRzXCI6IFwiMjAyMC0wMi0xMlwiLFwicGRlXCI6IFwiMjAyMC0wMi0yMFwiLFwiamRzXCI6IDQzLFwiamRlXCI6IDUxLFwiYmJkXCI6IFwiMjAyMC0wNS0yMFwiLFwicGNcIjogXCJERVwiLFwicGxcIjogXCJIZXJyYXRoXCIsXCJybW5cIjogXCIxMTIwMDEwMDUyMFwiLFwicG9uXCI6IFwiMzg5NTgxNDYwM1wiLFwicG9wXCI6IFwiNzE0XCIK"
        }
        response = self.post_rawrefresco(self, data)
        print("PK {0}".format(RawRefresco.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert RawRefresco.objects.count() == 1
        assert RawRefresco.objects.get().anfp == "18505100"
