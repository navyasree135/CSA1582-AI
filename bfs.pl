:- dynamic edge/3.  
edge(a, b, 2).  
edge(a, c, 4).  
edge(b, d, 3).  
edge(c, d, 1).  

bfs(Node, Goal) :- bfs([Node], Goal, []).  
bfs([Goal|_], Goal, _) :- write('Goal reached: '), write(Goal).  
bfs([N|Rest], Goal, Visited) :-  
    findall(X, (edge(N, X, _), \+ member(X, Visited)), Neighbors),  
    append(Rest, Neighbors, NewQueue),  
    bfs(NewQueue, Goal, [N|Visited]).
