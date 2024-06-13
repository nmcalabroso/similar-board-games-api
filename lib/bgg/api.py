import requests
import xmltodict
import time

from flask import current_app


class BoardGameGeekAPI:
    BASE_URL = 'https://www.boardgamegeek.com/xmlapi2/'

    def get_user(self, username):
        params = {'name': username, 'hot': 1, 'top': 1, 'buddies': 1, 'guilds': 1}
        response = requests.get(f'{self.BASE_URL}user', params=params)
        if response.status_code == 200:
            return self._parse_user(xmltodict.parse(response.content))
        else:
            response.raise_for_status()

    def get_collection(self, username):
        params = {
            'username': username,
            'stats': 1,
            'own': 1,
        }
        response = requests.get(f'{self.BASE_URL}collection', params=params)
        if response.status_code == 200:
            return self._parse_collection(xmltodict.parse(response.content))
        elif response.status_code == 202:
            current_app.logger.info('Collection request accepted, but not processed yet')
            time.sleep(5)
            return self.get_collection(username)
        else:
            response.raise_for_status()

    def _parse_user(self, user_info):
        return {
            'bgg_user_id': user_info['user']['@id'],
            'username': user_info['user']['@name'],
            'firstname': user_info['user']['firstname']['@value'],
            'lastname': user_info['user']['lastname']['@value'],
            'country': user_info['user']['country']['@value'],
        }
    
    def _parse_collection(self, collection_info):
        collections = []
        for item in collection_info['items']['item']:
            collections.append({
                'bgg_object_id': item['@objectid'],
                'name': item['name']['#text'],
                'sortindex': item['name']['@sortindex'],
                'subtype': item['@subtype'],
                'user_rating': item['stats']['rating']['@value'],
                'num_plays': item['numplays'],
                'ranks': item['stats']['rating']['ranks']['rank'],
            })
        return collections
