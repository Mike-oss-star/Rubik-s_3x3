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

    temp = cube[B][0].copy()

    cube[B][0]= cube[L][0]
    cube[L][0]= cube[F][0]
    cube[F][0]= cube[R][0]
    cube[R][0]= temp

def move_D(cube):
    cube[D] = rotate_face_cw(cube[D])

    temp = cube[F][2].copy()

    cube[F][2]= cube[L][2]
    cube[L][2]= cube[F][2]
    cube[F][2]= cube[R][2]
    cube[R][2]= temp

def move_B(cube):
    cube[B] = rotate_face_cw(cube[B])

    temp = cube[U][0].copy()

    cube[U][0] = [cube[R][i][2] for i in range(3)]
    cube[R][2][2], cube[R][1][2], cube[R][0][2] = cube[D][2]
    cube[D][2] = [cube[L][i][2] for i in range(3)]
    cube[L][2][2], cube[L][1][2], cube[L][0][2] = temp

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
    move_F(cube)
    move_F(cube)
    move_F(cube)

def move_U_(cube):
    move_U(cube)
    move_U(cube)
    move_U(cube)
    
def move_D_(cube):
    move_D(cube)
    move_D(cube)
    move_D(cube)

def move_B_(cube):
    move_B(cube)
    move_B(cube)
    move_B(cube)

def move_L_(cube):
    move_L(cube)
    move_L(cube)
    move_L(cube)


def move_R_(cube):
    move_R(cube)
    move_R(cube)
    move_R(cube)
    
