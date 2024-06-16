import http.client
import json

top_50_animes = []


def top_50_animes_from_myanimelist():

    conn = http.client.HTTPSConnection("myanimelist.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "bfd1f30ae0msh032d618bba13158p1e8492jsn1ea08ff93fc2",
        'x-rapidapi-host': "myanimelist.p.rapidapi.com"
    }

    conn.request("GET", "/anime/top/%7Bcategory%7D", headers=headers)

    res = conn.getresponse()
    data = res.read()
    animes = data.decode("utf-8")
    animes_list = json.loads(animes)
    sorted_animes = sorted(animes_list, key=lambda anime: anime['rank'])

    for anime in sorted_animes:
        top_50_animes.append(anime)
    return top_50_animes