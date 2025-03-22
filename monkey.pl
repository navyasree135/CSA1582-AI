move(state(on_floor, middle, has_not), grasp, state(on_floor, middle, has)).  
move(state(on_floor, L, H), walk(L, M), state(on_floor, M, H)).  
move(state(on_floor, L, H), climb, state(on_box, L, H)).  
move(state(on_box, L, H), jump, state(on_floor, L, H)).  
can_get(state(_, _, has)).  
can_get(State1) :- move(State1, _, State2), can_get(State2).
