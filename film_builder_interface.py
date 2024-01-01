from abc import ABCMeta, abstractmethod

class IFilmBuilder(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def set_titre(self, titre):
        "Build Title"

    @staticmethod
    @abstractmethod
    def set_description(self, description):
        "Build Description"

    @staticmethod
    @abstractmethod
    def set_img_url(self, img_url):
        "Build Image URL"

    @staticmethod
    @abstractmethod
    def set_horaires_list(self, horaires_list):
        "Build horaires list"

    @staticmethod
    @abstractmethod
    def set_press_rating(self, press_rating):
        "Build press rating"

    @staticmethod
    @abstractmethod
    def set_public_rating(self, public_rating):
        "Build public rating"

    @staticmethod
    @abstractmethod
    def get_film(self):
        "Build film"