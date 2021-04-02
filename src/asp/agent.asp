%
% Input
%

% Grid Size
rows(0..3).
cols(0..3).

% Drawn User Lines
drawn(2, 2, v, usr).
drawn(2, 1, v, usr).
drawn(2, 0, v, usr).
drawn(1, 2, v, usr).
drawn(1, 0, v, usr).
drawn(0, 2, v, usr).
drawn(2, 3, v, usr).
drawn(1, 3, v, usr).
drawn(0, 0, v, usr).
drawn(0, 1, h, usr).
drawn(0, 2, h, usr).
%drawn(0, 1, v, usr).

% drawn Opponents Lines
drawn(0, 0, h, opp).
drawn(1, 1, h, opp).
drawn(2, 0, h, opp).
drawn(2, 1, h, opp).
drawn(1, 0, h, opp).
drawn(0, 1, v, opp).
drawn(2, 2, h, opp).
drawn(0, 3, v, opp).
drawn(1, 1, v, opp).
drawn(1, 2, h, opp).
%drawn(0, 2, h, opp).


%
% ...
%

% Grid
grid(I, J, v) :- rows(I), cols(J), L = #max{ H : rows(H) }, I <= L - 1.
grid(I, J, h) :- rows(I), cols(J), L = #max{ H : cols(H) }, J <= L - 1.


% Squares
square(I, J) :- rows(I), cols(J), W = #max { K : cols(K) }, 
                                  H = #max { K : rows(K) }, I < H, J < W. 

% Valence
valence(I, J, Q) :- square(I, J), A = #count { I, J, D : drawn(I, J, D, _)     },
                                  B = #count { I, J    : drawn(I + 1, J, h, _) },
                                  C = #count { I, J    : drawn(I, J + 1, v, _) }, Q = 4 - (A + B + C).

% Game phases
phase(X) :- #count { I, J : valence(I, J, 1) } > 0, X = 1.
phase(X) :- #count { I, J : valence(I, J, 1) } = 0, X = 0.


%
% Utils
%
in_square(I, J, M, N) :- grid(I, J, _), square(M, N), I = M, J = N.
in_square(I, J, M, N) :- grid(I, J, _), square(M, N), I = M + 1, J = N.
in_square(I, J, M, N) :- grid(I, J, _), square(M, N), I = M, J = N + 1.


%
% Guess & Check
%

% 1. Prepare
instances(I, J, D) :- drawn(I, J, D, _).

% 2. Guess
in(I, J, D) | out(I, J, D) :- grid(I, J, D), not instances(I, J, D).

% 3. Check
:- not #count { I, J, D : in(I, J, D) } = 1.

% 4. Optimize
:~ in(I, J, _), valence(M, N, 1), in_square(I, J, M, N). [ 1@1, I, J ]