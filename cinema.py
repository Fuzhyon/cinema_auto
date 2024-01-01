from flask import render_template
import requests
from bs4 import BeautifulSoup
from film_builder import FilmBuilder
from configparser import ConfigParser


def requestUrlToSoup(code_cinema):
    # URL de la page du cinéma recherché
    url = "http://www.allocine.fr/seance/salle_gen_csalle=" + code_cinema + ".html"

    # Faire une requête GET à l'URL
    response = requests.get(url)

    # Créer un objet BeautifulSoup à partir du contenu HTML
    return BeautifulSoup(response.content, "html.parser")


def find_films_divs_list(soup):
    return soup.find("div", {"class": "showtimes-list-holder"}).find_all(
        "div", {"class": "movie-card-theater"}
    )


def find_films_ids_list(soup):
    divs_list = soup.find("div", {"class": "showtimes-list-holder"}).find_all(
        "div", {"class": "movie-card-theater"}
    )
    ids_list = [div.get("id") for div in divs_list]
    return ids_list


def get_id_film(film_div):
    return film_div.get("id")


def find_film_title(film_div):
    return film_div.find("a", {"class": "meta-title-link"}).text


def find_film_description(film_div):
    return film_div.find("div", {"class": "content-txt"}).text


def find_rating_list(film_div):
    return film_div.find_all("span", {"class": "stareval-note"})


def find_img_url(film_div):
    return film_div.find("img", {"class": "thumbnail-img"}).get("data-src")


def find_horaires(film_div):
    horaires = []
    horaires_div = film_div.find_all("div", {"class": "showtimes-hour-block"})
    for horaire_div in horaires_div:
        if (
            (horaire_div.find("span", {"class": "icon-3d"}))
            or (horaire_div.find("span", {"class": "icon-3d"}))
            or (horaire_div.find("span", {"class": "icon-4dx"}))
            or (horaire_div.find("span", {"class": "icon-ice"}))
        ):
            print("")
        else:
            horaires.append(
                horaire_div.find("span", {"class": "showtimes-hour-item-value"}).text
            )
    return horaires


def find_films_by_cinema(code_cinema):
    soup = requestUrlToSoup(code_cinema)
    films_divs_list = find_films_divs_list(soup)
    films_list = []
    for film_div in films_divs_list:
        film_builder = FilmBuilder()
        film_rating = find_rating_list(film_div)
        film_rating_press = (
            film_rating[0].text if len(film_rating) > 0 else "Pas de note"
        )
        film_rating_public = (
            film_rating[1].text if len(film_rating) > 1 else "Pas de note"
        )
        film_builder.set_titre(find_film_title(film_div)).set_description(
            find_film_description(film_div)
        ).set_press_rating(film_rating_press).set_public_rating(
            film_rating_public
        ).set_img_url(
            find_img_url(film_div)
        ).set_horaires_list(
            find_horaires(film_div)
        )

        films_list.append(film_builder.get_film())
    return films_list


# icon-imax icon-4dx icon-ice
def get_film_list():
    # Liste des cinémas depuis le fichier config.txt
    parser = ConfigParser()
    parser.read("config.txt")
    cinemas = dict(parser.items("cinemas"))

    films_list_gaumont = find_films_by_cinema(cinemas["gaumont"])
    films_list_cgr = find_films_by_cinema(cinemas["cgr"])
    film_list = []
    for film_gaumont in films_list_gaumont:
        for film_cgr in films_list_cgr:
            if film_gaumont.titre == film_cgr.titre:
                film_builder = FilmBuilder()
                film_builder.set_titre(film_gaumont.titre).set_description(
                    film_gaumont.description
                ).set_img_url(film_gaumont.img_url).set_press_rating(
                    film_gaumont.press_rating
                ).set_public_rating(
                    film_gaumont.public_rating
                ).set_horaires_list(
                    {
                        "gaumont": film_gaumont.horaires_list,
                        "cgr": film_cgr.horaires_list,
                    }
                )
                film_list.append(film_builder.get_film())
    return film_list
