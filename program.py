#!/usr/bin/env python3.8

import os
import sys
import textwrap

from api_tmdb import MovieClient
from pprint import pprint as pp


def process_genres(client) -> dict:
    """ Request genre id = name mapping for use in movie details later """
    genres = client.genres()

    return {genre["id"]: genre["name"] for genre in genres.json()["genres"]}


def clear_screen() -> None:
    """ Clear screen """
    os.system("cls" if os.name == "nt" else "clear")


def input_handler(
    options: list, question: str = "What would you like to view? ('Q' to quit) "
) -> int:
    """ Display input and handle processing response """
    """ Returns an 'index' of choices or -1 to indicate the user would like to 'quit' """
    INPUT_ERROR = f"\nPlease choice an option between 1 and {len(options)} or 'Q'.\n"

    while True:
        choice = input(question)

        if choice.lower() == "q":
            return -1

        try:
            choice = int(choice)
        except ValueError:
            print(INPUT_ERROR)
            continue

        if 1 <= choice <= len(options):
            return choice
        else:
            print(INPUT_ERROR)


def print_header(title: str):
    """ Print a header that includes a title and seperator """
    clear_screen()

    print(title)
    print(f"{'-' * 60}")
    print()


def print_menu(menu_options: list):
    """ Print the menu based upon passed in list of menu_options tuples """
    print_header("Please choose a movie option")

    for count, option in enumerate(menu_options, 1):
        print(f" {count}. {option[0]}")

    print()


def print_movie_choices(menu_option: tuple) -> list:
    """ Display movie options from passed in tuple """
    title, api_call = menu_option

    response = api_call()

    print_header(title)

    for count, movie in enumerate(response[:10], 1):
        print(f" {count}. {movie['title']} ({movie['release_date'].split('-')[0]})")

    print()

    return response[:10]


def print_movie_detail(movie_chosen: dict, genres: dict):
    """ Provide detailed information on a selected movie """

    movie_genres = [genres[genre] for genre in movie_chosen["genre_ids"]]

    print_header(f"Movie information: {movie_chosen['title']}")

    print(f"  {movie_chosen['title']}")
    print()

    for line in textwrap.wrap(movie_chosen["overview"], width=58):
        print(f"  {line}")

    print()
    print(f"  Release Date: {movie_chosen['release_date']}")
    print(f"  User Rating: {movie_chosen['vote_average']}")
    print(f"  Genres: {', '.join(movie_genres)}")

    print()
    _ = input("Press ENTER to continue...")


def main():
    mc = MovieClient()
    genres = process_genres(mc)

    menu_options = [
        ("Top Rated Movies - TMDb", mc.top_rated),
        ("Movies Now in Theatres", mc.now_playing),
        ("Movies Currently Trending (24 hrs)", mc.now_trending),
    ]

    while True:
        # Display top-level menu options listed in menu_options and handle input
        print_menu(menu_options)
        choice = input_handler(menu_options)

        if choice == -1:
            sys.exit()

        option_chosen = menu_options[choice - 1]

        while True:
            # Display returned movies list and query for movie detail request
            movies = print_movie_choices(option_chosen)
            choice = input_handler(
                movies,
                "Would you like more information on one of these movies? ('Q' to quit) ",
            )

            if choice == -1:
                break

            movie_chosen = movies[choice - 1]

            # Display movie detail
            print_movie_detail(movie_chosen, genres)


if __name__ == "__main__":
    main()
