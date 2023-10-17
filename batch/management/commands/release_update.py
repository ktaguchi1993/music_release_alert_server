import logging
import requests
import os

from django.core.management import BaseCommand

from music_release_alert_portal_app.models import NewRelease
from batch import consts

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("handle start")

        GRANT_TYPE = 'client_credentials'
        body_params = {'grant_type': GRANT_TYPE}

        CLIENT_ID = os.environ['CLIENT_ID']
        CLIENT_SECRET = os.environ['CLIENT_SECRET']

        token = requests.post(consts.token_url, data=body_params,
                              auth=(CLIENT_ID, CLIENT_SECRET)).json()['access_token']

        info = requests.get(consts.release_url,
                            headers={'Authorization': f"Bearer {token}"})

        # delete all data
        NewRelease.objects.all().delete()

        content = info.json()
        for item in content["albums"]["items"]:
            # print(item["artists"][0]["name"] + 'の' + item["name"])
            new_release = NewRelease()
            new_release.title = item["name"]
            new_release.artist = item["artists"][0]["name"]
            new_release.release_date = item["release_date"]
            new_release.url = item["uri"]
            new_release.type = item["type"]
            new_release.genre = "undefined"
            new_release.save()
