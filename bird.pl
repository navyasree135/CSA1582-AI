bird(eagel).
bird(sparrow).
bird(snake).
bird(tiger).
can_fly(eagel).
can_fly(sparrow).
cannot_fly(snake).
cannot_fly(tiger).
fly(Bird):- can_fly(Bird), write(Bird), write('can fly.').
fly(Bird):- cannot_fly(Bird), write(Bird), write('cannot fly.').
fly(Bird):-\+bird(Bird), write(Bird), write('is not a bird.').
