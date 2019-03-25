import numpy as np

def count_distinct(b):
    tmp = []
    for pos in b:
        tmp.append(arr_to_bits(pos))
    return len(set(tmp))

def arr_to_bits(a):
    ret = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                ret = ret << 1
                if a[i][j][k] == 1:
                    ret += 1
    return ret

def print_pretty(b):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if b[i][j][k] == 1:
                    print(i, j, k, sep='', end = ' ')
    print("\n")

def get_cubes(b):
    ret = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if b[i][j][k] == 1:
                    ret.append((i, j, k))
    return ret

def get_rot(b, n = 4, axes = 'xy'):
    if axes == 'xy':
        ax = (0, 1)
    elif axes == 'xz':
        ax = (0, 2)
    elif axes == 'yz':
        ax = (2, 1)
    tmp = []
    ret = []
    for _ in range(n):
        b = np.rot90(b, 1, ax)
        tmp.append(b)
    for rot in tmp:
        trans = [2, 2, 2]
        cubes = get_cubes(rot)
        for i in range(3):
            for c in cubes:
                trans[i] = min(trans[i], c[i])
        for i in range(3):
            trans[i] = -trans[i]
            
        a = np.zeros((3, 3, 3))
        for c in cubes:
            a[c[0]+trans[0]][c[1]+trans[1]][c[2]+trans[2]] = 1
        ret.append(a)
    return ret

def get_trans(b):
    cubes = get_cubes(b)
    trans = [[2, 0], [2, 0], [2, 0]]
    for i in range(3):
        for c in cubes:
            trans[i][0] = min(trans[i][0], c[i])
            trans[i][1] = max(trans[i][1], c[i])
    
    for i in range(3):
       trans[i][0] = -trans[i][0]
       trans[i][1] = 3 - trans[i][1]

    ret = []

    for i in range(trans[0][0], trans[0][1]):
        for j in range(trans[1][0], trans[1][1]):
            for k in range(trans[2][0], trans[2][1]):
                tmp = cubes
                a = np.zeros((3, 3, 3))
                for c in cubes:
                    a[c[0]+i][c[1]+j][c[2]+k] = 1
                ret.append(a)
    return ret      

def get_perms(b):
    lp = [[0, 1, 2],  [1, 2, 0], [2, 0, 1]]
    ret = []
    for perm in lp:
        ret.append(np.transpose(b, perm))
    return ret

def check_dupes(b):
    for i in range(len(b)):
        for j in range(len(b)):
            if not i == j:
                if np.array_equal(b[i], b[j]):
                    print("DUPES FOUND", i, j)
                    print(b[i], "\n", b[j])
                    return         
    print("NO DUPES FOUND")
                

def gen_v():
    b = np.zeros((3, 3, 3))
    b[0][0][0] = 1
    b[0][1][0] = 1
    b[1][0][0] = 1
    ret = []
    tmp = []
    for i in range(4):
        perms = get_perms(b)
        for perm in perms:
            tmp.append(perm)
        b = np.rot90(b)

    for pos in tmp:
        ret.extend(get_trans(pos))
    return ret

def gen_l():
    b1 = np.zeros((3, 3, 3))
    b1[0][0][0] = 1
    b1[0][1][0] = 1
    b1[1][0][0] = 1
    b1[2][0][0] = 1

    b2 = np.zeros((3, 3, 3))
    b2[0][0][0] = 1
    b2[0][1][0] = 1
    b2[1][1][0] = 1
    b2[2][1][0] = 1

    rotated = get_rot(b1)
    rotated.extend(get_rot(b2))
    permuted = []
    ret = []
    for r in rotated:
        permuted.extend(get_perms(r))
    for p in permuted:
        ret.extend(get_trans(p))
    return ret


def gen_t():
   
    b = np.zeros((3, 3, 3))
    b[0][0][0] = 1
    b[1][0][0] = 1
    b[1][1][0] = 1
    b[2][0][0] = 1

    rotated = get_rot(b)
    permuted = []
    ret = []
    for r in rotated:
        permuted.extend(get_perms(r))
    for p in permuted:
        ret.extend(get_trans(p))
    return ret

def gen_z():

    b1 = np.zeros((3, 3, 3))
    b1[0][0][0] = 1
    b1[1][0][0] = 1
    b1[1][1][0] = 1
    b1[2][1][0] = 1

    b2 = np.zeros((3, 3, 3))
    b2[0][1][0] = 1
    b2[1][0][0] = 1
    b2[1][1][0] = 1
    b2[2][0][0] = 1

    rotated = get_rot(b1, 2)
    rotated.extend(get_rot(b2, 2))
    permuted = []
    ret = []
    for r in rotated:
        permuted.extend(get_perms(r))
    for p in permuted:
        ret.extend(get_trans(p))
    return ret

def gen_a():

    b1 = np.zeros((3, 3, 3))
    b1[0][0][0] = 1
    b1[0][1][0] = 1
    b1[1][0][0] = 1
    b1[1][0][1] = 1

    b2 = np.zeros((3, 3, 3))
    b2[0][1][0] = 1
    b2[1][0][1] = 1
    b2[1][1][0] = 1
    b2[1][1][1] = 1

    rotated = get_rot(b1, 3)
    rotated.append(b2)
    permuted = []
    ret = []
    for r in rotated:
        permuted.extend(get_perms(r))
    for p in permuted:
        ret.extend(get_trans(p))
    return ret


def gen_b():

    b1 = np.zeros((3, 3, 3))
    b1[0][0][0] = 1
    b1[0][0][1] = 1
    b1[1][0][0] = 1
    b1[1][1][0] = 1

    b2 = np.zeros((3, 3, 3))
    b2[1][0][0] = 1
    b2[1][1][0] = 1
    b2[1][1][1] = 1
    b2[0][1][1] = 1

    rotated = get_rot(b1, 3)
    rotated.append(b2)
    permuted = []
    ret = []
    for r in rotated:
        permuted.extend(get_perms(r))
    for p in permuted:
        ret.extend(get_trans(p))
    return ret

def gen_p():

    b1 = np.zeros((3, 3, 3))
    b1[0][0][0] = 1
    b1[0][0][1] = 1
    b1[0][1][0] = 1
    b1[1][0][0] = 1

    b2 = np.zeros((3, 3, 3))
    b2[0][1][1] = 1
    b2[1][0][1] = 1
    b2[1][1][0] = 1
    b2[1][1][1] = 1

    rotated = get_rot(b1)
    rotated.extend(get_rot(b2))
    permuted = []
    ret = []
    for r in rotated:
        ret.extend(get_trans(r))
    return ret

all_sols = []
all_sols.append(gen_v())
all_sols.append(gen_l())
all_sols.append(gen_t())
all_sols.append(gen_z())
all_sols.append(gen_a())
all_sols.append(gen_b())
all_sols.append(gen_p())

for block_type in all_sols:
    for move in block_type:
        print(arr_to_bits(move),", ",  sep = '')
    print("--------------------")
