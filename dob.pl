dob(john, '1990-05-15').
dob(alice, '1985-12-30').
dob(michael, '1995-08-20').
dob(susan, '1978-03-10').
dob(peter, '2000-11-05').
date_of_birth(Name, DateOfBirth) :-
    dob(Name, DateOfBirth).
