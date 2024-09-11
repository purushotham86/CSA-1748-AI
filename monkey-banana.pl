% Initial state
initial_state(on_ground, box_underm, banana_hanging).

% Define actions that can be taken
action(on_ground, push_box, box_under_banana).
action(box_under_banana, climb, on_box).
action(on_box, reach, banana_reached).

% Plan predicate to start the planning process
plan(Plan) :-
    initial_state(State1, box_underm, banana_hanging),
    find_plan(State1, banana_reached, [], Plan).

% Base case: Goal reached, return the accumulated plan
find_plan(banana_reached, banana_reached, Plan, Plan).

% Recursive case: Find the next action and accumulate it in the plan
find_plan(State, Goal, Acc, Plan) :-
    action(State, Action, NextState),
    \+ member(Action, Acc),  % Ensure no repeated actions
    find_plan(NextState, Goal, [Action | Acc], Plan).
