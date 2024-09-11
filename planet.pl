% Facts representing planets
% Format: planet(Name, Size_in_km, Distance_from_Sun_in_million_km, Habitable)

planet(mercury, 4879, 57.9, no).
planet(venus, 12104, 108.2, no).
planet(earth, 12742, 149.6, yes).
planet(mars, 6779, 227.9, no).
planet(jupiter, 139820, 778.5, no).
planet(saturn, 116460, 1434, no).
planet(uranus, 50724, 2871, no).
planet(neptune, 49244, 4495, no).

% Rule to find the size of a specific planet
find_size(Planet, Size) :-
    planet(Planet, Size, _, _).

% Rule to find the distance of a specific planet from the Sun
find_distance(Planet, Distance) :-
    planet(Planet, _, Distance, _).

% Rule to check if a planet is habitable
is_habitable(Planet) :-
    planet(Planet, _, _, yes).

% Rule to find all planets within a certain distance from the Sun
find_within_distance(MaxDistance, Planet) :-
    planet(Planet, _, Distance, _),
    Distance =< MaxDistance.

% Rule to find planets larger than a specified size
find_larger_planets(MinSize, Planet) :-
    planet(Planet, Size, _, _),
    Size > MinSize.

% Rule to display all information related to a planet
display_planet_info(Planet) :-
    planet(Planet, Size, Distance, Habitable),
    format('Planet: ~w~n', [Planet]),
    format('Size (km): ~w~n', [Size]),
    format('Distance from Sun (million km): ~w~n', [Distance]),
    format('Habitable: ~w~n', [Habitable]).
