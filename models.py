import requests

class InstagramAccount:
    def __init__(self, username, access_token):
        self.username = username
        self.access_token = access_token

    def get_user_id(self):
        url = f'https://api.instagram.com/v1/users/search?q={self.username}&access_token={self.access_token}'
        response = requests.get(url)
        response_json = response.json()

        for user in response_json['data']:
            if user['username'] == self.username:
                return user['id']

        return None

    def get_media(self):
        user_id = self.get_user_id()

        if not user_id:
            return None

        url = f'https://api.instagram.com/v1/users/{user_id}/media/recent/?access_token={self.access_token}'
        response = requests.get(url)
        response_json = response.json()

        if 'data' not in response_json:
            return None

        media = []

        for post in response_json['data']:
            if 'images' not in post:
                continue

            for image in post['images']:
                media.append(image['url'])

        return media
