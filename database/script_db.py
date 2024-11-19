import utile.fetch_api as fetch_api
import utile.data as data


def fetch_and_store_top_50_animes():
    top_50_animes = fetch_api.top_50_animes_from_myanimelist()
    data.store_animes_in_db(top_50_animes)

fetch_and_store_top_50_animes()