%
% Input
%

% % Grid Size
% rows(0..3).
% cols(0..3).

% % Drawn User Lines
% drawn(2, 2, v).
% drawn(2, 1, v).
% drawn(2, 0, v).
% drawn(1, 2, v).
% drawn(1, 0, v).
% drawn(0, 2, v).
% drawn(2, 3, v).
% drawn(1, 3, v).
% drawn(0, 0, v).
% drawn(0, 1, h).
% drawn(0, 2, h).
% %drawn(0, 1, v).

% % Drawn Opponents Lines
% drawn(0, 0, h).
% drawn(1, 1, h).
% drawn(2, 0, h).
% drawn(2, 1, h).
% drawn(1, 0, h).
% drawn(0, 1, v).
% drawn(2, 2, h).
% drawn(0, 3, v).
% drawn(1, 1, v).
% drawn(1, 2, h).
% %drawn(0, 2, h).


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
valence(I, J, Q) :- square(I, J), A = #count { I, J, D : drawn(I, J, D)     },
                                  B = #count { I, J    : drawn(I + 1, J, h) },
                                  C = #count { I, J    : drawn(I, J + 1, v) }, Q = 4 - (A + B + C).

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
instances(I, J, D) :- drawn(I, J, D).

% 2. Guess
step(I, J, D) | not_step(I, J, D) :- grid(I, J, D), not instances(I, J, D).

% 3. Check
:- not #count { I, J, D : step(I, J, D) } = 1.

% 4. Optimize
:~ step(I, J, _), valence(M, N, 1), in_square(I, J, M, N). [ 1@1, I, J ]