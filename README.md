# Movie Uplink

This is a small application that, utilizing the TMDb API, provides movie information from the following APIs:

- Top Rated Movies
- Now Playing
- Trending Movies

After displaying the top 10 movies in the selected category, the user is able to choose to view movie details from any listed movie.

One major goal for the project was to explore the [Uplink](https://uplink.readthedocs.io/en/stable/) library which simplifies creating HTTP API clients.

## Screenshots

### Main Menu
```
Please choose a movie option
------------------------------------------------------------

 1. Top Rated Movies - TMDb
 2. Movies Now in Theatres
 3. Movies Currently Trending (24 hrs)

What would you like to view? ('Q' to quit)  _
```

### Trending Movies
```
Movies Currently Trending (24 hrs)
------------------------------------------------------------

 1. Joker (2019)
 2. Joker (2012)
 3. Zombieland: Double Tap (2019)
 4. Angel Has Fallen (2019)
 5. Joker Rising (2013)
 6. Ford v Ferrari (2019)
 7. Knives Out (2019)
 8. Once Upon a Time… in Hollywood (2019)
 9. Star Wars: The Rise of Skywalker (2019)
 10. The Addams Family (2019)

Would you like more information on one of these movies? ('Q' to quit)  _
```

### Movie Details
```
Movie information: Joker
------------------------------------------------------------

  Joker

  During the 1980s, a failed stand-up comedian is driven
  insane and turns to a life of crime and chaos in Gotham
  City while becoming an infamous psychopathic crime figure.

  Release Date: 2019-10-02
  User Rating: 8.3
  Genres: Crime, Drama, Thriller

Press ENTER to continue... 
```