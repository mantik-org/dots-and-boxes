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
%% Utils Rules
%%
%
% Lines
%   A connection between two dots. A line that has not yet been drawn is 
%   deﬁned as being ”empty”.
grid(I, J, v) :- rows(I), cols(J), L = #max{ H : rows(H) }, I <= L - 1.
grid(I, J, h) :- rows(I), cols(J), L = #max{ H : cols(H) }, J <= L - 1.
%
%
% Boxes
%   A box is an area in the grid that, when bounded by four lines, awards 
%   a single point to whichever player drew the fourth and ﬁnal line.
square(I, J) :- rows(I), cols(J), W = #max { K : cols(K) },
                                  H = #max { K : rows(K) }, I < H, J < W.
%
% Valences
%   This is a measure of how many empty lines a box has. It can, therefore, 
%   vary between 0 and 4.
valence(I, J, Q) :- square(I, J), A = #count { I, J, D : drawn(I, J, D)     },
                                  B = #count { I, J    : drawn(I + 1, J, h) },
                                  C = #count { I, J    : drawn(I, J + 1, v) }, Q = 4 - (A + B + C).
%
%
%  Check if a SQUARE contains LINE.
in_square(I, J, D, M, N) :- grid(I, J, D), square(M, N), I = M, J = N.
in_square(I, J, h, M, N) :- grid(I, J, h), square(M, N), I = M + 1, J = N.
in_square(I, J, v, M, N) :- grid(I, J, v), square(M, N), I = M, J = N + 1.
%
% Check if two SQUARE are adjacent or that SQUARE_A and SQUARE_B share at least one line.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M + 1, J = N.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M - 1, J = N.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M, J = N + 1.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M, J = N - 1.
%
% Check if two LINE are adjacent or that LINE_A and LINE_B share at least one dots.
adj_grid(I1, J1, v, I2, J2, v) :- grid(I1, J1, v), grid(I2, J2, v), I1 = I2 - 1, J1 = J2.
adj_grid(I1, J1, v, I2, J2, v) :- grid(I1, J1, v), grid(I2, J2, v), I1 = I2 + 1, J1 = J2.
adj_grid(I1, J1, h, I2, J2, h) :- grid(I1, J1, h), grid(I2, J2, h), I1 = I2, J1 = J2 - 1.
adj_grid(I1, J1, h, I2, J2, h) :- grid(I1, J1, h), grid(I2, J2, h), I1 = I2, J1 = J2 + 1.
adj_grid(I1, J1, v, I2, J2, h) :- grid(I1, J1, v), grid(I2, J2, h), I1 = I2, J1 = J2.
adj_grid(I1, J1, v, I2, J2, h) :- grid(I1, J1, v), grid(I2, J2, h), I1 = I2, J1 = J2 + 1.
adj_grid(I1, J1, v, I2, J2, h) :- grid(I1, J1, v), grid(I2, J2, h), I1 = I2 - 1, J1 = J2.
adj_grid(I1, J1, v, I2, J2, h) :- grid(I1, J1, v), grid(I2, J2, h), I1 = I2 - 1, J1 = J2 + 1.
adj_grid(I1, J1, h, I2, J2, v) :- grid(I1, J1, h), grid(I2, J2, v), I1 = I2, J1 = J2.
adj_grid(I1, J1, h, I2, J2, v) :- grid(I1, J1, h), grid(I2, J2, v), I1 = I2, J1 = J2 - 1.
adj_grid(I1, J1, h, I2, J2, v) :- grid(I1, J1, h), grid(I2, J2, v), I1 = I2 + 1, J1 = J2.
adj_grid(I1, J1, h, I2, J2, v) :- grid(I1, J1, h), grid(I2, J2, v), I1 = I2 + 1, J1 = J2 - 1.
%
%
%
% Calculate size for each chain.
% N.B: chains and cycle are calculated by chain.asp
chain_with_size(P, S) :- chain(P, _, _), S = #count { P, I, J : chain(P, I, J) }.
% Calculate size for each cycle.
cycle_with_size(P, S) :- cycle(P, _, _), S = #count { P, I, J : cycle(P, I, J) }.
% Calculate size for each chain and cycle.
chain_and_cycle_with_size(P, S) :- chain_with_size(P, S).
chain_and_cycle_with_size(P, S) :- cycle_with_size(P, S).
% Calculate union between chain and cycle.
chain_and_cycle(P, I, J) :- chain(P, I, J).
chain_and_cycle(P, I, J) :- cycle(P, I, J).
