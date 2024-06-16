import utile.fetch_api as fetch_api
import utile.data as data


def main():
    top_50_animes = fetch_api.top_50_animes_from_myanimelist()
    print(top_50_animes)
    data.store_animes_in_db(top_50_animes)


if __name__ == '__main__':
    main()
