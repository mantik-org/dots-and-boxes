%
% Chains
%

%
% Guess & Check
%

% 1. Guess
in_chain(I, J) | out_chain(I, J) :- square(I, J).

chain_path(I, J, M, N) :- valence(I, J, 2), valence(M, N, 2), in_square(R, C, D, I, J), in_square(R, C, D, M, N), not drawn(R, C, D).
chain_path(I, J, M, N) :- chain_path(M, N, I, J).

chained(I, J, M, N) :- chain_path(I, J, M, N).
chained(I, J, M, N) :- chained(I, J, Z1, Z2), chain_path(Z1, Z2, M, N).

% 2. Check
:- in_chain(I, J), in_chain(M, N), not chained(I, J, M, N).
:- in_chain(I, J), out_chain(M, N), chain_path(I, J, M, N).

% 3. Optimize
:- not #count { I, J : in_chain(I, J) } > 2.

chain(0, I, J) :- in_chain(I, J).