%
% Input
%

% % Grid Size
% rows(0..6).
% cols(0..6).

% drawn(0, 0, v).
% drawn(0, 1, v).
% drawn(1, 0, v).
% drawn(1, 1, v).
% drawn(2, 0, v).
% drawn(2, 1, v).
% drawn(3, 0, v).
% drawn(3, 1, v).

% drawn(2, 3, v).
% drawn(2, 4, v).
% drawn(3, 3, v).
% drawn(3, 4, v).
% drawn(4, 3, v).
% drawn(4, 4, v).
% drawn(5, 3, v).
% %drawn(5, 4, v).


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


% Chains
chain(I, J) | not_chain(I, J) :- square(I, J).

chain_path(I, J, M, N) :- valence(I, J, 2), valence(M, N, 2), in_square(R, C, D, I, J), in_square(R, C, D, M, N), not drawn(R, C, D).
chain_path(I, J, M, N) :- chain_path(M, N, I, J).

chained(I, J, M, N) :- chain_path(I, J, M, N).
chained(I, J, M, N) :- chained(I, J, Z1, Z2), chain_path(Z1, Z2, M, N).

:- chain(I, J), chain(M, N), not chained(I, J, M, N).
:- chain(I, J), not_chain(M, N), chain_path(I, J, M, N).
:~ not #count { I, J : chain(I, J) } > 1. [ 1@9000 ]


% Game phases
%phase(X) :- #count { I, J : valence(I, J, 1) } > 0, X = 2.
%phase(X) :- #count { I, J : valence(I, J, 1) } = 0, X = 1.
phase(1).


%
% Utils
%
% in_square(LINE, SQUARE): Check if a SQUARE contains LINE.
in_square(I, J, D, M, N) :- grid(I, J, D), square(M, N), I = M, J = N.
in_square(I, J, h, M, N) :- grid(I, J, h), square(M, N), I = M + 1, J = N.
in_square(I, J, v, M, N) :- grid(I, J, v), square(M, N), I = M, J = N + 1.

% adj_square(SQUARE, SQUARE): Check if two SQUARE are adjacent or that SQUARE_A and SQUARE_B share at least one line.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M + 1, J = N.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M - 1, J = N.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M, J = N + 1.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M, J = N - 1.



%
% Guess & Check
%

% 1. Prepare
instances(I, J, D) :- drawn(I, J, D).

% 2. Guess
step(I, J, D) | not_step(I, J, D) :- grid(I, J, D), not instances(I, J, D).

% 3. Check
%   - Only one solution.
:- not #count { I, J, D : step(I, J, D) } = 1.

% 4. Optimize
%   - Phase 1.
%       1. Do not create a box with a valence of 1.
:~ phase(1), step(I, J, D), valence(M, N, 1), in_square(I, J, D, M, N). [ 1@1, I, J, D ]
%       2. Try to be the first player to enter the second phase.
:~ phase(1), chain(I, J). [ 1@2, I, J ]
:~ phase(1), step(I, J, D), not chain(M, N), in_square(I, J, D, M, N). [ 1@3, I, J, D ]

:~ not_step(I, J, D), valence(M, N, 1), in_square(I, J, D, M, N). [ 1@5, I, J, D ]