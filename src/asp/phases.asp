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
% drawn(5, 4, v).

player(2).

% Game phases
%phase(X) :- #count { I, J : valence(I, J, 1) } > 0, X = 2.
%phase(X) :- #count { I, J : valence(I, J, 1) } = 0, X = 1.
phase(1).


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
% Chains
%bigchain(X) :- chain(X, L, _, _), L = #max { H, K : chain(K, H, _, _) }. 


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
:~ phase(1), not_step(I1, J1, D1), drawn(I2, J2, D2), adj_grid(I1, J1, D1, I2, J2, D2), D1 == D2, chain_turn(opt). [ 1@2, I1, J1, D1 ]
:~ phase(1), not_step(I1, J1, D1), drawn(I2, J2, D2), adj_grid(I1, J1, D1, I2, J2, D2), D1 != D2. [ 1@1, I1, J1, D1 ]


%:~ phase(1), chain(I, J). [ 1@2, I, J ]
%:~ phase(1), step(I, J, D), not chain(M, N), in_square(I, J, D, M, N). [ 1@3, I, J, D ]


% Phase 1/2
:~ not_step(I, J, D), valence(M, N, 1), in_square(I, J, D, M, N). [ 1@5, I, J, D ]


% Debug
debug(chain_count_0) :- Z == 0, Z = #max { K : chain_count(K) }.
debug(chain_count_1) :- Z == 1, Z = #max { K : chain_count(K) }.
debug(chain_count_2) :- Z == 2, Z = #max { K : chain_count(K) }.
debug(chain_count_3) :- Z == 3, Z = #max { K : chain_count(K) }.
debug(chain_count_4) :- Z == 4, Z = #max { K : chain_count(K) }.
debug(chain_count_5) :- Z == 5, Z = #max { K : chain_count(K) }.
debug(chain_turn) :- chain_turn(opt).
