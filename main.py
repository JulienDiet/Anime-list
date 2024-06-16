import tkinter as tk
from PIL import Image, ImageTk, ImageFilter  # Importez ImageFilter pour les filtres d'image
import requests
import io
import utile.data as data  # Assurez-vous que votre module `data` est correctement importé

def show_anime_cards(animes):
    root = tk.Tk()
    root.title("Anime List")
    # Créer un Canvas et une Scrollbar
    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Ajouter le Canvas et la Scrollbar à la fenêtre
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Créer un Frame dans le Canvas
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)
    for anime in animes:
        # Créer un Frame pour chaque anime
        anime_frame = tk.Frame(frame, padx=10, pady=10, bd=2, relief=tk.GROOVE)
        anime_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Afficher les informations de l'anime dans des Labels
        rank_label = tk.Label(frame, text=f"Rank: {anime[0]}")
        rank_label.pack(anchor=tk.W)

        title_label = tk.Label(frame, text=f"Title: {anime[1]}")
        title_label.pack(anchor=tk.W)

        url_label = tk.Label(frame, text=f"URL: {anime[2]}")
        url_label.pack(anchor=tk.W)

        # Charger l'image à partir de l'URL
        image_url = anime[3]
        response = requests.get(image_url)
        img_data = response.content if response.status_code == 200 else b''
        img = Image.open(io.BytesIO(img_data)) if img_data else None

        if img:
            # Redimensionner l'image si nécessaire
            max_width = 200  # Ajustez la taille maximale selon vos besoins
            max_height = 200
            img.thumbnail((max_width, max_height))

            # Convertir l'image pour Tkinter
            img_tk = ImageTk.PhotoImage(img)

            # Afficher l'image dans un Label
            image_label = tk.Label(frame, image=img_tk)
            image_label.image = img_tk  # Garder une référence pour éviter la suppression par le garbage collector
            image_label.pack(anchor=tk.CENTER)

        type_label = tk.Label(frame, text=f"Type: {anime[4]}")
        type_label.pack(anchor=tk.W)

        episodes_label = tk.Label(frame, text=f"Episodes: {anime[5]}")
        episodes_label.pack(anchor=tk.W)

        start_date_label = tk.Label(frame, text=f"Start Date: {anime[6]}")
        start_date_label.pack(anchor=tk.W)

        members_label = tk.Label(frame, text=f"Members: {anime[7]}")
        members_label.pack(anchor=tk.W)

        score_label = tk.Label(frame, text=f"Score: {anime[8]}")
        score_label.pack(anchor=tk.W)

    # Mettre à jour le scrollregion après avoir ajouté tous les animes
    frame.update()
    canvas.configure(scrollregion=canvas.bbox(tk.ALL))

    root.mainloop()


def main():
    animes = data.fetch_animes_from_db()
    show_anime_cards(animes)


if __name__ == '__main__':
    main()
