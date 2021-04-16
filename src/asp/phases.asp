
% Game phases
phase(X) :- #count { I, J : valence(I, J, V), V > 2 } != 0, X = 1.
phase(X) :- #count { I, J : valence(I, J, V), V > 2 } == 0, X = 2, not phase(3).
phase(X) :- #count { I, J : valence(I, J, V), V > 2 } == 0, X = 3, #count { I : chain_with_size(I, S), S <= 2 } == 0.

% Calculate if grid size is odd or even
grid_size(even) :- X = #max { H : rows(H) }, Y = #max { H : cols(H) }, N = Z / 2 * 2, Z = X + Y, Z == N.
grid_size(odd)  :- X = #max { H : rows(H) }, Y = #max { H : cols(H) }, N = Z / 2 * 2, Z = X + Y, Z != N.

% Calculate number of chains and cycles inside the board.
chain_count(Z) :- phase(1), X = #count { K : chain(K, _, _) }, Y = #count { K : cycle(K, _, _) }, Z = X + Y.

% Grid size odd: First player even number of chains, second player odd number of chains. 
chain_turn(opt) :- phase(1), player(2), grid_size(odd), N = Z / 2 * 2, Z != N, Z = #max { K : chain_count(K) }.
chain_turn(opt) :- phase(1), player(1), grid_size(odd), N = Z / 2 * 2, Z == N, Z = #max { K : chain_count(K) }.

% Grid size even: First player odd number of chains, second player even number of chains. 
chain_turn(opt) :- phase(1), player(2), grid_size(even), N = Z / 2 * 2, Z == N, Z = #max { K : chain_count(K) }.
chain_turn(opt) :- phase(1), player(1), grid_size(even), N = Z / 2 * 2, Z != N, Z = #max { K : chain_count(K) }.

% Calculate size for each chain.
chain_with_size(P, S) :- chain(P, _, _), S = #count { P, I, J : chain(P, I, J) }.


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
:~ phase(1), step(I, J, D), valence(M, N, 2), in_square(I, J, D, M, N). [ 1@3, I, J, D ]
%       2. Try to be the first player to enter the second phase.
%           a...
:~ phase(1), not_step(I1, J1, D1), drawn(I2, J2, D2), adj_grid(I1, J1, D1, I2, J2, D2), D1 == D2, chain_turn(opt). [ 1@2, I1, J1, D1 ]
:~ phase(1), not_step(I1, J1, D1), drawn(I2, J2, D2), adj_grid(I1, J1, D1, I2, J2, D2), D1 != D2. [ 1@1, I1, J1, D1 ]


% If there is a square of valence 1 then fill it in.
:~ not_step(I, J, D), valence(M, N, 1), in_square(I, J, D, M, N). [ 1@10, I, J, D ]


% Debug
%debug(chain_count, Z, 0) :- Z = #max { K : chain_count(K) }.
%debug(chain_turn_optimal, 0, 0) :- chain_turn(opt).
debug(phase, X, 0) :- phase(X).
%debug(chain_with_size, I, S) :- chain_with_size(I, S).
%debug(chain, I, 0) :- chain(I, _, _).