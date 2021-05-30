%%                                                                      
%% GPL3 License 
%%
%% Author(s):                                                              
%%      Antonino Natale <ntlnnn97r06e041t@studenti.unical.it>
%%      Matteo Perfidio <prfmtt98e07f537p@studenti.unical.it>
%% 
%% 
%% Copyright (C) 2021 Mantik
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
%% Game phases
%%
% 1. Neutral Phase: 
%       This is the part of the game in which all chains and their lengths have been determined. 
%       Players alternate placing edges without capturing boxes. 
phase(X) :- current_phase(1), #max { V : valence(_, _, V) }  > 2, X = 1.
%
% 2. Short Chain Phase:
%       This is the part of the game in which all that is left is short chains, long chains, 
%       and cycles, and in which players alternate giving away short chains. 
phase(X) :- current_phase(1), #max { V : valence(_, _, V) } <= 2, X = 2, #count { I : chain_with_size(I, S), S <= 2 } > 0.
phase(X) :- current_phase(2), #max { V : valence(_, _, V) } <= 2, X = 2, #count { I : chain_with_size(I, S), S <= 2 } > 0.
%
% 3. Final Phase:
%       This is the part of the game in which there are only chains and cycles left. 
phase(X) :- current_phase(1), #max { V : valence(_, _, V) } <= 2, X = 3, not phase(2).
phase(X) :- current_phase(2), #max { V : valence(_, _, V) } <= 2, X = 3, not phase(2).
phase(X) :- current_phase(3), #max { V : valence(_, _, V) } <= 2, X = 3.


