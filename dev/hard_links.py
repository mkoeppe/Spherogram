"""
A bunch of tricky links that used to break simplify.
"""

import spherogram
import random

def test(link):
    for i in range(10):
        L = link.copy()
        L.simplify('global')
        L.PD_code()
        expected = len(link.link_components) + L.unlinked_unknot_components
        print(L, L.unlinked_unknot_components, '\n')

C = spherogram.Link([(9, 17, 10, 16), (5, 18, 6, 19), (17, 4, 18, 5), (2, 15, 3, 16), (14, 8, 15, 7), (6, 14, 7, 13), (1, 13, 2, 12), (28, 22, 29, 21), (19, 11, 20, 10), (8, 4, 9, 3), (24, 27, 25, 0), (26, 23, 27, 24), (22, 25, 23, 26), (11, 21, 12, 20), (29, 0, 28, 1)])

test(C)

B = spherogram.Link([(9, 19, 10, 18), (4, 17, 5, 18), (16, 3, 17, 4), (2, 15, 3, 16), (14, 8, 15, 7), (6, 14, 7, 13), (1, 13, 2, 12), (28, 22, 29, 21), (19, 11, 20, 10), (8, 6, 9, 5), (24, 27, 25, 0), (26, 23, 27, 24), (22, 25, 23, 26), (11, 21, 12, 20), (29, 0, 28, 1)])

test(B)

# component incorrectly updated?
A = spherogram.Link([(21, 31, 22, 30), (16, 29, 17, 30), (28, 15, 29, 16),
                     (14, 27, 15, 28), (26, 20, 27, 19), (18, 26, 19, 25),
                     (13, 25, 14, 24), (37, 7, 32, 6), (5, 37, 6, 36),
                     (35, 3, 36, 2), (9, 34, 10, 35), (33, 8, 34, 9),
                     (31, 23, 0, 22), (20, 18, 21, 17), (7, 12, 8, 13),
                     (11, 4, 12, 5), (3, 10, 4, 11), (32, 1, 33, 2), (23, 1, 24, 0)])

test(A)

            
# Crazy recursion error                    
N = spherogram.Link([(14, 5, 15, 0), (6, 2, 7, 1), (15, 18, 16, 19), (17, 20, 18, 21),
                     (19, 16, 20, 17), (13, 2, 14, 3), (12, 10, 13, 9),
                     (8, 12, 9, 11), (10, 8, 11, 7), (21, 5, 6, 4), (3, 0, 4, 1)])

test(N)


# Failure to pull off a component sitting on top/bottom
M = spherogram.Link([(9,17,10,16),(5,18,6,19),(17,4,18,5),(2,15,3,16),(14,8,15,7),(6,14,7,13),(1,13,2,12),(28,22,29,21),(19,11,20,10),(8,4,9,3),(24,27,25,0),(26,23,27,24),(22,25,23,26),(11,21,12,20),(29,0,28,1)])
N = M.copy().mirror()

test(M)
test(N)

A = spherogram.Link([(13, 2, 14, 3), (21, 5, 6, 4), (15, 18, 16, 19), (17, 20, 18, 21), (19, 16, 20, 17), (14, 5, 15, 0), (12, 10, 13, 9), (8, 12, 9, 11), (10, 8, 11, 7), (6, 2, 7, 1), (3, 0, 4, 1)])

test(A)



X = spherogram.Link([(25, 30, 26, 31), (6, 30, 7, 33), (18, 11, 19, 12), (23, 15, 24, 14), (8, 15, 9, 16), (16, 3, 17, 4), (20, 10, 21, 9), (10, 22, 11, 21), (26, 29, 27, 0), (4, 27, 5, 28), (28, 5, 29, 6), (1, 13, 2, 12), (31, 24, 32, 25), (32, 8, 33, 7), (22, 20, 23, 19), (2, 17, 3, 18), (13, 1, 14, 0)])

Y = spherogram.Link([(8, 32, 9, 35), (29, 34, 30, 35), (1, 14, 2, 15), (26, 14, 27, 13), (12, 26, 13, 25), (24, 12, 25, 11), (10, 20, 11, 19), (7, 4, 8, 5), (31, 6, 0, 7), (5, 30, 6, 31), (20, 4, 21, 3), (2, 24, 3, 23), (27, 18, 28, 19), (21, 17, 22, 16), (32, 10, 33, 9), (33, 28, 34, 29), (15, 23, 16, 22), (17, 0, 18, 1)])

test(X)
test(Y)

B = spherogram.Link([(28, 39, 29, 40), (7, 39, 8, 38), (20, 13, 21, 14), (26, 16, 27, 15), (9, 16, 10, 17), (19, 2, 20, 3), (23, 11, 24, 10), (11, 25, 12, 24), (29, 37, 30, 36), (3, 30, 4, 31), (31, 4, 0, 5), (33, 12, 34, 13), (40, 27, 41, 28), (41, 9, 38, 8), (25, 23, 26, 22), (34, 22, 35, 21), (14, 35, 15, 36), (17, 33, 18, 32), (6, 37, 7, 32), (18, 2, 19, 1), (5, 0, 6, 1)])
test(B)

L = spherogram.Link([(28, 39, 29, 40), (7, 39, 8, 38), (20, 13, 21, 14), (26, 16, 27, 15), (9, 16, 10, 17), (19, 2, 20, 3), (23, 11, 24, 10), (11, 25, 12, 24), (29, 37, 30, 36), (3, 30, 4, 31), (31, 4, 0, 5), (33, 12, 34, 13), (40, 27, 41, 28), (41, 9, 38, 8), (25, 23, 26, 22), (34, 22, 35, 21), (14, 35, 15, 36), (17, 33, 18, 32), (6, 37, 7, 32), (18, 2, 19, 1), (5, 0, 6, 1)])
test(L)


P0 = spherogram.Link([(31, 38, 32, 39), (37, 30, 38, 31), (12, 29, 13, 30), (18, 50, 19, 49), (48, 20, 49, 19), (46, 11, 47, 12), (45, 36, 46, 37), (7, 44, 8, 45), (2, 10, 3, 9), (20, 0, 21, 27), (56, 18, 57, 17), (23, 14, 24, 15), (35, 9, 36, 8), (15, 55, 16, 54), (16, 25, 17, 26), (22, 51, 23, 52), (26, 57, 27, 54), (55, 24, 56, 25), (10, 4, 11, 3), (28, 48, 29, 47), (43, 35, 44, 34), (50, 14, 51, 13), (52, 21, 53, 22), (6, 34, 7, 33), (5, 43, 6, 42), (4, 2, 5, 1), (39, 32, 40, 33), (40, 53, 41, 42), (41, 0, 28, 1)])

P0.simplify('global')

test(P0)

P1 = spherogram.Link([(6, 32, 7, 31), (33, 38, 34, 39), (59, 35, 60, 34), (16, 54, 17, 53), (66, 8, 67, 7), (48, 46, 49, 45), (40, 48, 41, 47), (46, 40, 47, 39), (63, 44, 64, 45), (43, 21, 44, 20), (37, 59, 38, 58), (36, 26, 37, 25), (69, 14, 56, 15), (15, 68, 16, 69), (29, 18, 30, 19), (24, 57, 25, 58), (4, 13, 5, 14), (35, 26, 0, 27), (5, 57, 6, 56), (54, 18, 55, 17), (55, 2, 52, 3), (3, 52, 4, 53), (22, 42, 23, 41), (23, 32, 24, 33), (8, 20, 9, 19), (65, 43, 66, 42), (67, 30, 68, 31), (9, 63, 10, 62), (21, 65, 22, 64), (10, 61, 11, 62), (11, 28, 12, 29), (12, 1, 13, 2), (49, 60, 50, 61), (50, 27, 51, 28), (51, 0, 36, 1)])

test(P1)

P2 = spherogram.Link([(13, 19, 14, 18), (17, 39, 18, 38), (15, 20, 16, 21), (12, 8, 13, 7), (6, 12, 7, 11), (10, 40, 11, 39), (8, 41, 9, 42), (40, 5, 41, 6), (52, 47, 53, 48), (46, 53, 47, 54), (37, 57, 38, 56), (54, 0, 55, 21), (30, 52, 31, 51), (19, 42, 20, 43), (50, 32, 51, 31), (4, 9, 5, 10), (3, 16, 4, 17), (57, 2, 46, 3), (61, 35, 58, 34), (27, 48, 28, 49), (49, 26, 50, 27), (32, 26, 33, 25), (44, 55, 45, 56), (43, 15, 44, 14), (33, 61, 34, 60), (24, 59, 25, 60), (58, 23, 59, 24), (35, 28, 36, 29), (22, 30, 23, 29), (36, 2, 37, 1), (45, 0, 22, 1)])

test(P2)

P3 = spherogram.Link([(23, 54, 24, 55), (44, 17, 45, 18), (18, 45, 19, 46), (48, 0, 49, 13), (12, 37, 13, 38), (8, 12, 9, 11), (10, 6, 11, 5), (7, 35, 8, 34), (33, 7, 34, 6), (38, 49, 39, 50), (46, 41, 47, 42), (40, 47, 41, 48), (43, 23, 44, 22), (29, 32, 30, 33), (35, 30, 36, 31), (31, 36, 32, 37), (53, 24, 54, 25), (52, 16, 53, 15), (16, 52, 17, 55), (27, 51, 28, 50), (4, 10, 5, 9), (28, 3, 29, 4), (21, 43, 22, 42), (51, 2, 40, 3), (25, 21, 26, 20), (14, 19, 15, 20), (26, 2, 27, 1), (39, 0, 14, 1)])


test(P3)

P4 = spherogram.Link([(33, 17, 34, 16), (8, 11, 9, 12), (23, 13, 24, 12), (10, 35, 11, 30), (34, 9, 35, 10), (29, 5, 0, 4), (3, 29, 4, 28), (38, 26, 39, 25), (19, 22, 20, 23), (21, 18, 22, 19), (17, 20, 18, 21), (5, 30, 6, 31), (39, 6, 36, 7), (24, 38, 25, 37), (7, 36, 8, 37), (15, 2, 16, 3), (13, 33, 14, 32), (26, 32, 27, 31), (14, 2, 15, 1), (27, 1, 28, 0)])

test(P4)
