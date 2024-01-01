class Film:
    def __init__(
            self,
            titre="",
            description="",
            img_url="",
            horaires_list=None,
            public_rating="",
            press_rating="",
    ):
        self._titre = titre
        self._description = description
        self._img_url = img_url
        self._horaires = horaires_list
        self._public_rating = public_rating
        self._press_rating = press_rating

    @property
    def titre(self):
        return self._titre

    @property
    def description(self):
        return self._description

    @property
    def img_url(self):
        return self._img_url

    @property
    def horaires_list(self):
        return self._horaires

    @property
    def public_rating(self):
        return self._public_rating

    @property
    def press_rating(self):
        return self._press_rating

    @titre.setter
    def titre(self, value):
        self._titre = value

    @description.setter
    def description(self, value):
        self._description = value

    @img_url.setter
    def img_url(self, value):
        self._img_url = value

    @horaires_list.setter
    def horaires_list(self, value):
        self._horaires = value

    @press_rating.setter
    def press_rating(self, value):
        self._press_rating = value

    @public_rating.setter
    def public_rating(self, value):
        self._public_rating = value

    def __str__(self):
        return f"Titre: {self._titre}\n" + f"Description: {self._description}\n" \
               + f"Public rating: {self._public_rating}\n" \
               + f"Press rating: {self._press_rating}\n" \
               + f"Horaires: {self._horaires}\n" \
               + f"Img url: {self._img_url}"
