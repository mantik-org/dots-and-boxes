%
% Statement
%


% Grid
grid(I, J, v) :- rows(I), cols(J), L = #max{ H : rows(H) }, I <= L - 1.
grid(I, J, h) :- rows(I), cols(J), L = #max{ H : cols(H) }, J <= L - 1.


% Squares
square(I, J) :- rows(I), cols(J), W = #max { K : cols(K) },
                                  H = #max { K : rows(K) }, I < H, J < W.

% Valence
valence(I, J, Q) :- square(I, J), A = #count { I, J, D : drawn(I, J, D)     },
                                  B = #count { I, J    : drawn(I + 1, J, h) },
                                  C = #count { I, J    : drawn(I, J + 1, v) }, Q = 4 - (A + B + C).