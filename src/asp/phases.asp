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



% Game phases
%phase(X) :- #count { I, J : valence(I, J, 1) } > 0, X = 2.
%phase(X) :- #count { I, J : valence(I, J, 1) } = 0, X = 1.
phase(1).


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
:~ phase(1), not_step(I1, J1, D1), drawn(I2, J2, D2), adj_grid(I1, J1, D1, I2, J2, D2). [ 1@1, I1, J1, D1 ]


%:~ phase(1), chain(I, J). [ 1@2, I, J ]
%:~ phase(1), step(I, J, D), not chain(M, N), in_square(I, J, D, M, N). [ 1@3, I, J, D ]


% Phase 1/2
:~ not_step(I, J, D), valence(M, N, 1), in_square(I, J, D, M, N). [ 1@5, I, J, D ]