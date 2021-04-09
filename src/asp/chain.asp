%
% Chains
%

%
% Guess & Check
%

% 1. Guess
chain(I, J) | not_chain(I, J) :- square(I, J).

chain_path(I, J, M, N) :- valence(I, J, 2), valence(M, N, 2), in_square(R, C, D, I, J), in_square(R, C, D, M, N), not drawn(R, C, D).
chain_path(I, J, M, N) :- chain_path(M, N, I, J).

chained(I, J, M, N) :- chain_path(I, J, M, N).
chained(I, J, M, N) :- chained(I, J, Z1, Z2), chain_path(Z1, Z2, M, N).

% 2. Check
:- chain(I, J), chain(M, N), not chained(I, J, M, N).
:- chain(I, J), not_chain(M, N), chain_path(I, J, M, N).

% 3. Optimize
:~ not #count { I, J : chain(I, J) } > 1. [ 1@9000 ]