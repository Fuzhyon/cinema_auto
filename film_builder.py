"The Builder Class"
from film_builder_interface import IFilmBuilder
from film import Film


class FilmBuilder(IFilmBuilder):
    def __init__(self):
        self._film = Film()

    def set_titre(self, titre):
        self._film._titre = titre
        return self

    def set_description(self, description):
        self._film._description = description
        return self

    def set_img_url(self, img_url):
        self._film._img_url = (
            img_url.replace("c_160_213", "c_620_840") if img_url else None
        )
        return self

    def set_horaires_list(self, horaires_list):
        self._film._horaires = horaires_list
        return self

    def set_press_rating(self, press_rating):
        self._film._press_rating = press_rating
        return self

    def set_public_rating(self, public_rating):
        self._film._public_rating = public_rating
        return self

    def get_film(self):
        return self._film
