% Define the vowel characters
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Predicate to count vowels in a list of characters
count_vowels([], 0). % Base case: empty list has 0 vowels
count_vowels([H|T], Count) :-
    (   vowel(H)               % Check if head is a vowel
    ->  count_vowels(T, RestCount), % Recursively count vowels in the tail
        Count is RestCount + 1     % Increment count
    ;   count_vowels(T, Count)     % If head is not a vowel, do not increment count
    ).

% Main predicate to read input and count vowels
main :-
    write('Enter a word: '),
    read_line_to_string(user_input, InputString), % Read input from the user
    string_chars(InputString, Chars),             % Convert string to list of characters
    count_vowels(Chars, Count),                   % Count the vowels
    write('Number of vowels: '),
    write(Count), nl.                             % Output the count

% To run the program, call the main predicate


