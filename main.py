import random

U, D, F, B, L, R = 0, 1, 2, 3, 4, 5

#===================
#CREATION DU CUBE
#===================
def new_cube(): 
    cube = [
        [[(255,255,255)]*3 for _ in range(3)],  # Up
        [[(255,255,0)]*3 for _ in range(3)],  # Down
        [[(255,0,0)]*3 for _ in range(3)],  # Front
        [[(255,127,0)]*3 for _ in range(3)],  # Back
        [[(0,0,255)]*3 for _ in range(3)],  # Left
        [[(0,255,0)]*3 for _ in range(3)]   # Right
    ]

    return cube


#Faire tourner une face sur elle-même
def rotate_face_cw(face):
    return [list(row) for row in zip(*face[::-1])]

def rotate_face_ccw(face):
    return [list(row) for row in zip(*face)][::-1]

#=================================
# Mouvements de base U,D,F,B,L,R
#=================================

def move_F(cube):
    cube[F] = rotate_face_cw(cube[F])

    temp = cube[U][2].copy()

    cube[U][2] = [cube[L][2-i][2] for i in range(3)]
    cube[L][0][2], cube[L][1][2], cube[L][2][2] = cube[D][0]
    cube[D][0] = [cube[R][2-i][0] for i in range(3)]
    cube[R][0][0], cube[R][1][0], cube[R][2][0] = temp

def move_U(cube):
    cube[U] = rotate_face_cw(cube[U])

    temp = cube[F][0].copy()

    cube[F][0] = cube[R][0][:]
    cube[R][0] = cube[B][0][::-1]
    cube[B][0] = cube[L][0][::-1]
    cube[L][0] = temp

def move_D(cube):
    cube[D] = rotate_face_cw(cube[D])

    temp = cube[F][2].copy()

    cube[F][2] = cube[L][2][:]
    cube[L][2] = cube[B][2][::-1]
    cube[B][2] = cube[R][2][::-1]
    cube[R][2] = temp

def move_B(cube):
    cube[B] = rotate_face_cw(cube[B])

    temp = cube[U][0].copy()

    cube[U][0] = [cube[R][i][2] for i in range(3)]
    cube[R][2][2], cube[R][1][2], cube[R][0][2] = cube[D][2]
    cube[D][2] = [cube[L][i][0] for i in range(3)]
    cube[L][2][0], cube[L][1][0], cube[L][0][0] = temp

def move_L(cube):
    cube[L] = rotate_face_cw(cube[L])
    
    temp = [cube[U][i][0] for i in range(3)].copy()

    cube[U][0][0], cube[U][1][0], cube[U][2][0] = [cube[B][2-i][0] for i in range(3)]
    cube[B][2][0], cube[B][1][0], cube[B][0][0] = [cube[D][i][0] for i in range(3)]
    cube[D][0][0], cube[D][1][0], cube[D][2][0] = [cube[F][i][0] for i in range(3)]
    cube[F][0][0], cube[F][1][0], cube[F][2][0] = temp

def move_R(cube):
    cube[R] = rotate_face_cw(cube[R])

    temp = [cube[U][2-i][2] for i in range(3)]

    cube[U][0][2], cube[U][1][2], cube[U][2][2] = [cube[F][i][2] for i in range(3)]
    cube[F][0][2], cube[F][1][2], cube[F][2][2] = [cube[D][i][2] for i in range(3)]
    cube[D][0][2], cube[D][1][2], cube[D][2][2] = [cube[B][2-i][2] for i in range(3)]
    cube[B][0][2], cube[B][1][2], cube[B][2][2] = temp

#=====================
#Mouvements Inverses
#=====================
def move_F_(cube):
    cube[F] = rotate_face_ccw(cube[F])
    temp = cube[U][2].copy()

    cube[U][2] = [cube[R][i][0] for i in range(3)]
    cube[R][0][0], cube[R][1][0], cube[R][2][0] = cube[D][0][::-1]
    cube[D][0] = [cube[L][i][2] for i in range(3)]
    cube[L][0][2], cube[L][1][2], cube[L][2][2] = temp[::-1]

def move_U_(cube):
    cube[U] = rotate_face_ccw(cube[U])
    temp = cube[F][0].copy()

    cube[F][0] = cube[L][0][:]
    cube[L][0] = cube[B][0][::-1]
    cube[B][0] = cube[R][0][::-1]
    cube[R][0] = temp

def move_D_(cube):
    cube[D] = rotate_face_ccw(cube[D])
    temp = cube[F][2].copy()

    cube[F][2] = cube[R][2][:]
    cube[R][2] = cube[B][2][::-1]
    cube[B][2] = cube[L][2][::-1]
    cube[L][2] = temp

def move_B_(cube):
    cube[B] = rotate_face_ccw(cube[B])
    temp = cube[U][0].copy()

    cube[U][0] = [cube[L][2-i][0] for i in range(3)]
    cube[L][0][0], cube[L][1][0], cube[L][2][0] = cube[D][2]
    cube[D][2] = [cube[R][2-i][2] for i in range(3)]
    cube[R][0][2], cube[R][1][2], cube[R][2][2] = temp

def move_L_(cube):
    cube[L] = rotate_face_ccw(cube[L])
    temp = [cube[U][i][0] for i in range(3)]

    cube[U][0][0], cube[U][1][0], cube[U][2][0] = [cube[F][i][0] for i in range(3)]
    cube[F][0][0], cube[F][1][0], cube[F][2][0] = [cube[D][i][0] for i in range(3)]
    cube[D][0][0], cube[D][1][0], cube[D][2][0] = [cube[B][2-i][0] for i in range(3)]
    cube[B][0][0], cube[B][1][0], cube[B][2][0] = temp[::-1]

def move_R_(cube):
    cube[R] = rotate_face_ccw(cube[R])
    temp = [cube[U][i][2] for i in range(3)]

    cube[U][0][2], cube[U][1][2], cube[U][2][2] = [cube[B][2-i][2] for i in range(3)]
    cube[B][0][2], cube[B][1][2], cube[B][2][2] = [cube[D][2-i][2] for i in range(3)]
    cube[D][0][2], cube[D][1][2], cube[D][2][2] = [cube[F][i][2] for i in range(3)]
    cube[F][0][2], cube[F][1][2], cube[F][2][2] = temp


#==========================
# Séquences et mélange
#==========================
MOVES = {
    "U": move_U, "U'": move_U_,
    "D": move_D, "D'": move_D_,
    "F": move_F, "F'": move_F_,
    "B": move_B, "B'": move_B_,
    "L": move_L, "L'": move_L_,
    "R": move_R, "R'": move_R_,
}

def apply_moves(cube, sequence):
    for token in sequence.split():
        if token.endswith("2"):
            base = token[:-1]
            MOVES[base](cube)
            MOVES[base](cube)
        else:
            MOVES[token](cube)

def scramble(cube, n=20):
    faces = ["U", "D", "F", "B", "L", "R"]
    suffixes = ["", "'", "2"]
    sequence = []
    last_face = None
    for _ in range(n):
        face = random.choice([f for f in faces if f != last_face])
        sequence.append(face + random.choice(suffixes))
        last_face = face
    moves_str = " ".join(sequence)
    apply_moves(cube, moves_str)
    return moves_str


def is_solve(cube):
    solve_cube = [
        [[(255,255,255)]*3 for _ in range(3)],  # Up
        [[(255,255,0)]*3 for _ in range(3)],  # Down
        [[(255,0,0)]*3 for _ in range(3)],  # Front
        [[(255,127,0)]*3 for _ in range(3)],  # Back
        [[(0,0,255)]*3 for _ in range(3)],  # Left
        [[(0,255,0)]*3 for _ in range(3)]   # Right
    ]

    if cube==solve_cube:
        return True
    else:
        return False