%%                                                                      
%% GPL3 License 
%%
%% Author(s):                                                              
%%      Antonino Natale <ntlnnn97r06e041t@studenti.unical.it>
%%      Matteo Perfidio <prfmtt98e07f537p@studenti.unical.it>
%% 
%% 
%% Copyright (C) 2021 AI Namp
%%
%% This file is part of DotsAndBoxesAI.  
%% 
%% This program is free software: you can redistribute it and/or modify
%% it under the terms of the GNU General Public License as published by
%% the Free Software Foundation, either version 3 of the License, or
%% (at your option) any later version.
%%
%% This program is distributed in the hope that it will be useful,
%% but WITHOUT ANY WARRANTY; without even the implied warranty of
%% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
%% GNU General Public License for more details.
%%
%% You should have received a copy of the GNU General Public License
%% along with this program. If not, see <https://www.gnu.org/licenses/>.
%%


%%
%% External Inputs
%%
%% player(I):           Player ID.
%% drawn(I, J):         Lines alredy drawn in the current board state.
%% rows(I), cols(I):    Rows and Columns of the board.


%%
%% Game phases
%%
% 1. Neutral Phase: 
%       This is the part of the game in which all chains and their lengths have been determined. 
%       Players alternate placing edges without capturing boxes. 
phase(X) :- #max { V : valence(_, _, V) }  > 2, X = 1.
%
% 2. Short Chain Phase:
%       This is the part of the game in which all that is left is short chains, long chains, 
%       and cycles, and in which players alternate giving away short chains. 
phase(X) :- #max { V : valence(_, _, V) } <= 2, X = 2, not phase(3).
%
% 3. Final Phase:
%       This is the part of the game in which there are only chains and cycles left. 
phase(X) :- #max { V : valence(_, _, V) } <= 2, X = 3, #count { I : chain_with_size(I, S), S <= 2 } == 0.
%
%

%%
%% Utils
%%
% Calculate size for each chain.
chain_with_size(P, S) :- chain(P, _, _), S = #count { P, I, J : chain(P, I, J) }.


%%
%% Chain Rule
%%
%   The chain rule tells you how many chains you should make to force your opponent to open 
%   the first long chain or cycle:
%       - First player even number of chains, second player odd number of chains. 
%       - First player odd number of chains, second player even number of chains.
%
% 1. If Grid Size is odd:
chain_turn(opt) :- phase(1), player(2), grid_size(odd), N = Z / 2 * 2, Z != N, Z = #max { K : chain_count(K) }.
chain_turn(opt) :- phase(1), player(1), grid_size(odd), N = Z / 2 * 2, Z == N, Z = #max { K : chain_count(K) }.
%
% 1. If Grid Size is even:
chain_turn(opt) :- phase(1), player(2), grid_size(even), N = Z / 2 * 2, Z == N, Z = #max { K : chain_count(K) }.
chain_turn(opt) :- phase(1), player(1), grid_size(even), N = Z / 2 * 2, Z != N, Z = #max { K : chain_count(K) }.
%
% Calculate if Grid Size is odd or even
grid_size(even) :- phase(1), X = #max { H : rows(H) }, Y = #max { H : cols(H) }, N = Z / 2 * 2, Z = X + Y, Z == N.
grid_size(odd)  :- phase(1), X = #max { H : rows(H) }, Y = #max { H : cols(H) }, N = Z / 2 * 2, Z = X + Y, Z != N.
%
% Calculate number of chains and cycles inside the current board state.
chain_count(Z) :- phase(1), X = #count { K : chain(K, _, _) }, Y = #count { K : cycle(K, _, _) }, Z = X + Y.



%%
%% Guess, Check & Optimize
%%
% 1. Prepare
%   - Calculate all instances of drawn lines.
instances(I, J, D) :- drawn(I, J, D).
%
% 2. Guess
%   - Calculate all possibile steps for the next turn excluding lines already drawn.
step(I, J, D) | not_step(I, J, D) :- grid(I, J, D), not instances(I, J, D).
%
% 3. Check
%   - Only one solution is allowed.
:- not #count { I, J, D : step(I, J, D) } = 1.
%
% 4. Optimize
%
%   - Phase 1 - Neutral Phase:
%       1. Do not create a box with a valence of 1.
:~ phase(1), step(I, J, D), valence(M, N, 2), in_square(I, J, D, M, N). [ 1@3, I, J, D ]
%
%       2. Try to be the first player to enter the second phase, applying the Chain Rule.
%          More precisely, the chain rule states that if a player wants to force his opponent 
%          to be the first to move into a chain or cycle, then:
%
%               a) If there is an odd total number of dots, then the first player should make 
%                  an odd number of chains and the second player an even number of chains.
%               b) If there is an even number of total dots, then the first player should make 
%                  an even number of chains and the second player an odd number of chains. 
%
%          If we're following in optimal way the Chain Rule then we play building long chains.
:~ phase(1), not_step(I1, J1, D1), drawn(I2, J2, D2), adj_grid(I1, J1, D1, I2, J2, D2), D1 == D2, chain_turn(opt). [ 1@2, I1, J1, D1 ]
%          Otherwise, we try to divide long chain in smaller chain.
:~ phase(1), not_step(I1, J1, D1), drawn(I2, J2, D2), adj_grid(I1, J1, D1, I2, J2, D2), D1 != D2. [ 1@1, I1, J1, D1 ]
%
%          In this way, the player who took the last turn is the one who get the control of the match 
%          and the one who forced his opponent to first move into a chain or cycle.
%
%
%   - Phase 2 - Short Chain Phase.
%       1. Give away the shortest short chains first to tie or get as many boxes as possible 
%          during the short chain phase. 
:~ phase(2), not_step(I, J, D), chain_with_size(P, S), chain(P, M, N), in_square(I, J, D, M, N), S = #min { K, Q : chain_with_size(Q, K) }. [ 1@1, I, J, D ] 
%
%
%   - Phase 3 - Final Phase.
%       TODO ...
%
%   - Exception Phase.
%       1. If there is a square of valence 1 and we're not applying the Double Dealing algorithm,
%          we can fill it in.
:~ not_step(I, J, D), valence(M, N, 1), in_square(I, J, D, M, N). [ 1@10, I, J, D ]



%%
%% Debug
%%
%debug(chain_count, Z, 0) :- Z = #max { K : chain_count(K) }.
%debug(chain_turn_optimal, 0, 0) :- chain_turn(opt).
debug(phase, X, 0) :- phase(X).
%debug(chain_with_size, I, S) :- chain_with_size(I, S).
%debug(chain, I, 0) :- chain(I, _, _).