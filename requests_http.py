import requests

x = []


class Super_hero:

    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.intellegence = int()

    def get_inf(self):

        url = f'https://superheroapi.com/api/{self.token}/search/{self.name}'
        response = requests.get(url)
        id_dict = dict(response.json())
        self.intellegence = id_dict['results'][0]['powerstats']['intelligence']
        x.append([self.intellegence, self.name])
        return self.intellegence


hero_1 = Super_hero('Hulk', '2619421814940190')
hero_2 = Super_hero('Captain America', '2619421814940190')
hero_3 = Super_hero('Thanos', '2619421814940190')
hero_1.get_inf()
hero_2.get_inf()
hero_3.get_inf()


def find_most_intellegent():
    x.sort()
    most_int_hero = x[0][1]
    print(most_int_hero)
    return most_int_hero

find_most_intellegent()
