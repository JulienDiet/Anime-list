import utile.fetch_api as fetch_api


def main():
    top_50_animes = fetch_api.top_50_animes_from_myanimelist()
    for anime in top_50_animes:
        for key, value in anime.items():
            print(f'{key}: {value}')
        print()


if __name__ == '__main__':
    main()
