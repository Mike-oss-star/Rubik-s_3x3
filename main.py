U, D, F, B, L, R = 0, 1, 2, 3, 4, 5

def new_cube(): 
    cube = [
        [[U]*3 for _ in range(3)],  # Up
        [[D]*3 for _ in range(3)],  # Down
        [[F]*3 for _ in range(3)],  # Front
        [[B]*3 for _ in range(3)],  # Back
        [[L]*3 for _ in range(3)],  # Left
        [[R]*3 for _ in range(3)]   # Right
    ]

    return cube


def rotate_face_cw(face):
    return [list(row) for row in zip(*face[::-1])]


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
    
    
    



cube = new_cube()
move_R(cube)

print(cube)

