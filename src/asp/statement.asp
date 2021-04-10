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



%
% Utils
%

% in_square(LINE, SQUARE): Check if a SQUARE contains LINE.
in_square(I, J, D, M, N) :- grid(I, J, D), square(M, N), I = M, J = N.
in_square(I, J, h, M, N) :- grid(I, J, h), square(M, N), I = M + 1, J = N.
in_square(I, J, v, M, N) :- grid(I, J, v), square(M, N), I = M, J = N + 1.

% adj_square(SQUARE, SQUARE): Check if two SQUARE are adjacent or that SQUARE_A and SQUARE_B share at least one line.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M + 1, J = N.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M - 1, J = N.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M, J = N + 1.
adj_square(I, J, M, N) :- square(I, J), square(M, N), I = M, J = N - 1.

% adj_grid(LINE, LINE): Check if two LINE are adjacent or that LINE_A and LINE_B share at least one dots.
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




