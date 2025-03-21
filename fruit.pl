fruit(apple, red).
fruit(orange, orange).
fruit(grape, green).
find_colour(Name, Colour):-
    fruit(Name, Colour).
