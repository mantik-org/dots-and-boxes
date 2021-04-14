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

% outer_chain(SQUARE): outer square inside a chain. 
%   Calculated by substracting inner square inside a chain,
%   or that a box with two empty lines shared inside an another box in chain)
outer_chain(I, J) :- in_chain(I, J), #count { I, J, R, C, D : inner_chain(I, J, R, C, D) } < 2. 
inner_chain(I, J, R, C, D) :- in_chain(I, J), not drawn(R, C, D), in_square(R, C, D, I, J), in_chain(M, N), in_square(R, C, D, M, N), adj_square(I, J, M, N).

% 2. Check
:- in_chain(I, J), in_chain(M, N), not chained(I, J, M, N).
:- in_chain(I, J), out_chain(M, N), chain_path(I, J, M, N).


% 3. Optimize
:- not #count { I, J : in_chain(I, J) } > 2.

% 4. Result
chain(0, I, J) :- in_chain(I, J), not cycle(0, I, J).
cycle(0, I, J) :- in_chain(I, J), #count { P, K : outer_chain(P, K) } == 0.

