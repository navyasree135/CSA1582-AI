% hanoi/3 represents the solution to the Towers of Hanoi problem.
% Move N disks from Tower1 to Tower3 using Tower2 as an auxiliary tower.
hanoi(1, Tower1, Tower3, _) :-
    write('Move disk 1 from '), write(Tower1), write(' to '), write(Tower3), nl.
hanoi(N, Tower1, Tower3, Tower2) :-
    N > 1,
    M is N - 1,
    hanoi(M, Tower1, Tower2, Tower3),
    write('Move disk '), write(N), write(' from '), write(Tower1), write(' to '), write(Tower3), nl,
    hanoi(M, Tower2, Tower3, Tower1).
