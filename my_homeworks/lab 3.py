from math import ceil, log, floor
#Var = 10
#m = 293
#p(x) = x^293 + x^11 + x^6 + x + 1
bin_string1 = str(input("Enter A: "))
bin_string2 = str(input("Enter B: "))
bin_string3 = str(input("Enter C: "))
a_lst = list(map(int, bin_string1))
b_lst = list(map(int, bin_string2))
c_lst = list(map(int, bin_string3))
px_lst = list(map(int,'100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100001000011'))
m = 293
help_m = [1, 0, 0, 1, 0, 0, 1, 0, 0]

def remove_zeros(a):
    while a[0] == 0 and len(a) > 1:
        a.pop(0)
    return a


def regulation(a, b):
    a = remove_zeros(a)
    b = remove_zeros(b)
    if len(a) == len(b):
        i = 0
        while i < len(a)-1 and a[i] == b[i]:
            i += 1
        if a[i] < b[i]:
            return 0
        else:
            return 1
    elif len(a) < len(b):
        return 0
    return 1


def add_zeros(a, b):
    if regulation(a, b) == 1:
        while len(b) != len(a):
            b = [0] + b
    else:
        while len(a) != len(b):
            a = [0] + a
    return a, b


def gf_add(a, b):
    a, b = add_zeros(a, b)
    c = list()
    for i in range(len(a)):
        c.append((a[i] + b[i]) % 2)
    c = remove_zeros(c)
    return c


def gf_mul(a, b):
    new_len = max(len(a), len(b))
    c = [0]*new_len*2
    a.reverse()
    b.reverse()
    i = 0
    while i < len(a):
        if a[i] == 0:
            i += 1
            continue
        else:
            j = 0
            while j < len(b):
                if b[j] == 0:
                    j += 1
                    continue
                else:
                    c[i+j] += 1
                    c[i+j] %= 2
                j += 1
        i += 1
    a.reverse()
    b.reverse()
    c.reverse()
    c = remove_zeros(c)
    return c

def gf_sqr(a):
    c = [0]*len(a)*2
    a.reverse()
    i = 0
    while i < len(a):
        if a[i] == 0:
            i += 1
            continue
        else:
            c[i*2] = 1
        i += 1
    a.reverse()
    c.reverse()
    c = remove_zeros(c)
    return c

def mod_px_lst(a):
    a = remove_zeros(a)
    if len(a) < len(px_lst):
        return a
    else:
        new_len = len(a) - len(px_lst) + 1
        b = [1] + [0]*(new_len - 1)
        c = gf_mul(px_lst, b)
        a = gf_add(a, c)
        a = mod_px_lst(a)
        a = remove_zeros(a)
        return a

def trace(a):
    t = a
    for i in range(0, m - 1):
        a = mod_px_lst(gf_sqr(a))
        t = gf_add(t, a)
        t = mod_px_lst(t)
    remove_zeros(t)
    return t


def inverse(a):
    b = a
    a = [1]
    for i in range (m - 1):
        b = mod_px_lst(gf_sqr(b))
        a = mod_px_lst(gf_mul(a, b))
    return a

def gf_power (a, power):
    first = a
    c = list()
    c.append(1)
    i = 0
    while i < len(power)-1:
        if power[i] == 1:
            c = gf_mul(c, first)
        c = mod_px_lst(gf_sqr(c))
        i += 1
    if power[i] == 1:
        c = mod_px_lst(gf_mul(c, first))
    return c

def is_prime(p):
    for i in (2, ceil(p**0.5)):
        if p % i == 0:
            return False
    return True

def find_min_k(p):
    start = floor(log(p, 2))
    i = start
    while 2**i % p != 1:
        i += 1
    return i

def ONB_exists():
    p = 2*m + 1
    if is_prime(p) == False:
        return False
    k = find_min_k(p)
    if not k == 2*m:
        if not (p % 4 == 3 and k == m):
            return False
        else:
            return True
    else:
        return True

def nb_regul(a):
    while len(a) < m:
        a = [0] + a
    return a

def nb_add(a, b):
    a = nb_regul(a)
    b = nb_regul(b)
    c = list()
    for i in range(len(a)):
        c.append((a[i] + b[i]) % 2)
    return c

def nb_sqr(a):
    a = nb_regul(a)
    u = a.copy()
    step = u[-1]
    u.pop(-1)
    u.reverse()
    u.append(step)
    u.reverse()
    return u


def nb_trace(a):
    tr = 0
    for i in range (len(a)):
        tr += a[i]
    tr %= 2
    return tr

def mul_matrix():
    p = 2*m + 1
    M = list()
    for i in range(m):
        str = [0]*m
        M.append(str)
    for i in range(m):
        for j in range(m):
            if ((2**i + 2**j) % p == 1 or
                (2**i - 2**j) % p == 1 or
                (-2**i + 2**j) % p == 1 or
                (-2**i - 2**j) % p == 1):
                M[i][j] = 1
    return M

def nb_mul(a, b, mx):
    main_mx = [0]*m
    a = nb_regul(a)
    b = nb_regul(b)
    u = a.copy()
    v = b.copy()
    for k in range(m):
        mx1 = [0]*m
        if(k > 0):
            step1 = u[0]
            u.pop(0)
            u.append(step1)
            step2 = v[0]
            v.pop(0)
            v.append(step2)
        for i in range(m):
            for j in range(m):
                mx1[i] += u[j] * mx[j][i]
                mx1[i] %= 2
        for l in range(m):
            main_mx[k] += mx1[l]*v[l]
            main_mx[k] %= 2
    return main_mx


def nb_power(a, power, mx):
    a = nb_regul(a)
    c = list()
    while(len(c) < m):
        c.append(1)
    i = 0
    while i < len(power)-1:
        if power[i] == 1:
            c = nb_mul(c, a, mx)
        c = nb_sqr(c)
        i += 1
    if power[i] == 1:
        c = nb_mul(c, a, mx)
    return c


def nb_inverse(a, mx):
    a = nb_regul(a)
    beta = a.copy()
    k = 1
    t = len(help_m)
    for i in range(t-1, -1, -1):
        beta_memo = beta.copy()
        for j in range(k):
            beta_memo = nb_sqr(beta_memo)
        beta = nb_mul(beta_memo, beta, mx)
        k *= 2
        if help_m[i] == 1:
            beta = nb_mul(nb_sqr(beta), a, mx)
            k += 1
    beta = nb_sqr(beta)
    return beta

def transform_to_str(a):
    return ''.join(map(str, a))

#
# print("A + B =")
# print(transform_to_str(gf_add(a_lst,b_lst)))
# print("A * B =")
# print(transform_to_str(mod_px_lst(gf_mul(a_lst, b_lst))))
# print("A^2 =")
# print(transform_to_str(mod_px_lst(gf_sqr(a_lst))))
# print("Tr(A) =")
# print(transform_to_str(trace(a_lst)))
# print("Inverse(A) =")
# print(transform_to_str(inverse(a_lst)))
# print("A^C =")
# print(transform_to_str(gf_power(a_lst, c_lst)))
# print("A*C + B*C = ")
# print(transform_to_str(gf_add(mod_px_lst(gf_mul(a_lst, c_lst)), mod_px_lst(gf_mul(c_lst, b_lst)))))
# print("(A + B)*C = ")
# print(transform_to_str(mod_px_lst(gf_mul(gf_add(a_lst, b_lst), c_lst))))
#


M = mul_matrix()
print("Does ONB exist? ")
print(ONB_exists())
print("A + B =")
print(transform_to_str(nb_add(a_lst,b_lst)))
print("A^2 =")
print(transform_to_str(nb_sqr(a_lst)))
print("Tr(A) =")
print(nb_trace(a_lst))
print("A * 1 =")
print(transform_to_str(nb_mul(a_lst, [1]*293, M)))
print("Multiplicative matrix = ")
print(M)
print("A * B = ")
print(transform_to_str(nb_mul(a_lst, b_lst, M)))
print("A^C = ")
print(transform_to_str(nb_power(a_lst, [1,0], M)))
a_in = nb_inverse(a_lst, M)
print("Inverse(A) = ")
print(transform_to_str(a_in))
print("A * Inverse(A) = ")
print(transform_to_str(nb_mul(a_in, a_lst, M)))
print("A*C + B*C = ")
print(transform_to_str(nb_add(nb_mul(a_lst, c_lst, M), nb_mul(c_lst, b_lst, M))))
print("(A + B)*C = ")
print(transform_to_str(nb_mul(nb_add(a_lst, b_lst), c_lst, M)))


