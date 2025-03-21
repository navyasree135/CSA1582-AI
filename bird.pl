% Query to check if a bird can fly.
can_fly(Bird) :-
    bird(Bird, yes),
    write(Bird), write(' can fly.'), nl.
can_fly(Bird) :-
    bird(Bird, no),
    write(Bird), write(' cannot fly.'), nl.
can_fly(Bird) :-
    \+ bird(Bird, _),
    write('Unknown bird: '), write(Bird), nl.
