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
%% Guess & Check
%%
% 1. Guess
%   - Calculate all possibile chain path for the current board state.
in_chain(I, J) | out_chain(I, J) :- square(I, J).
%
%
% 2. Check
%
%   - Empty solution are now allowed.
:- not #count { I, J : in_chain(I, J) } > 0.
%
%   - Calculate if two boxes has a shared empty line.
chain_path(I, J, M, N) :- valence(I, J, 2), valence(M, N, 2), in_square(R, C, D, I, J), in_square(R, C, D, M, N), not drawn(R, C, D).
chain_path(I, J, M, N) :- chain_path(M, N, I, J).
%
%   - Calculate recursively, if two or more boxes follow a path.
chained(I, J, M, N) :- chain_path(I, J, M, N).
chained(I, J, M, N) :- chained(I, J, Z1, Z2), chain_path(Z1, Z2, M, N).
%
%   - Only valid chain paths are allowed.
:- in_chain(I, J), in_chain(M, N), not chained(I, J, M, N).
%
%   - Two boxes which make a path and one of them is out of solution, are not allowed.
:- in_chain(I, J), out_chain(M, N), chain_path(I, J, M, N).
%
%
% 3. Collect all outer boxes of each chain.
%
%   - Calculated by substracting inner boxes inside a chain,
%     or that a box with two empty lines shared inside an another box in chain
outer_chain(I, J) :- in_chain(I, J), #count { I, J, R, C, D : inner_lines(I, J, R, C, D) } < 2. 
%
%   - Calculate all empty lines inside a chain which share two adjacent boxes.
inner_lines(I, J, R, C, D) :- in_chain(I, J), in_chain(M, N), not drawn(R, C, D), in_square(R, C, D, I, J), in_square(R, C, D, M, N), adj_square(I, J, M, N).
%
%
% 4. Result
%
%   - Chains:
%       a) Long Chain: a chain of 3 or more boxes.
%       b) Short Chain: a chain of one or two boxes.
chain(0, I, J) :- in_chain(I, J), not cycle(0, I, J).
%
%   - Cycles
%       A cycle is a closed loop of four or more boxes.
cycle(0, I, J) :- in_chain(I, J), #count { P, K : outer_chain(P, K) } == 0.
