% Facts
male(john).
male(bob).
male(jim).
male(tom).
female(lisa).
female(anna).
female(susan).
parent(john, bob).
parent(john, jim).
parent(anna, bob).
parent(anna, jim).
parent(bob, tom).
parent(bob, lisa).
parent(susan, tom).
parent(susan, lisa).
% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
% Query to get details about parents
get_parents_details(Name) :-
    (father(Father, Name) -> format('Father of ~w is ~w.~n', [Name, Father]); true),
    (mother(Mother, Name) -> format('Mother of ~w is ~w.~n', [Name, Mother]); true).
% Query to get a list of males
get_males(Males) :-
    findall(X, male(X), Males).
% Query to get a list of females
get_females(Females) :-
    findall(X, female(X), Females).
