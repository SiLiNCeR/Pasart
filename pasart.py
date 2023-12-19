import math

def print_pasart():
    print("{0:^24}".format("PASART"))
    print("{0:^18}".format("CREATIVE COMPUTING"))
    print("{0:^16}".format("MORRISTOWN   NEW JERSEY"))
    print("\n\n")

def create_pascals_triangle(T):
    P = [[0] * T for _ in range(T)]
    for R in range(T):
        for C in range(T):
            if R == 0 or C == 0:
                P[R][C] = 1
            else:
                P[R][C] = P[R][C-1] + P[R-1][C]
    return P

def print_single_pasart(P, Q, T):
    for R in range(T):
        for C in range(T):
            if P[R][C] % Q != 0:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

def print_double_pasart(P, T):
    Z = T
    N = Z
    for R in range(N):
        for C in range(Z-1):
            if R == 0 or C == 0:
                P[R][C] = 1
            else:
                P[R][C] = P[R][C-1] + P[R-1][C]
        Z -= 1

    Z = N
    N = 2
    for R in range(Z, 0, -1):
        for C in range(Z, N, -1):
            if R == Z or C == Z:
                P[R][C] = 1
            else:
                P[R][C] = P[R][C+1] + P[R+1][C]
        N += 1

    print_single_pasart(P, 1, 2 * T)  # Fix the argument here

def print_corner_pasart(P, T):
    M = 1
    Y = T
    Z = math.floor(Y / 2)
    B5 = Z * 2
    Z1 = Z
    Z2 = Z1
    Z3 = Z2
    X4 = Z3
    X5 = X4

    for I in range(Z1):
        for J in range(Z):
            if I == 0 or J == 0:
                P[I][J] = 1
            else:
                P[I][J] = P[I][J-1] + P[I-1][J]
        Z -= 1

    N = Z1
    for I in range(Z1):
        for J in range(Y, X5+1, -1):
            if I != 0 and J != Y:
                P[I][J] = P[I][J+1] + P[I-1][J]
        X5 += 1

    N = Z2
    for I in range(Y, X4+1, -1):
        for J in range(Z2):
            if J != 0 and I != Y:
                P[I][J] = P[I][J-1] + P[I+1][J]
        Z2 -= 1

    N = Z3
    for I in range(Y, N+1, -1):
        for J in range(Y, Z3+1, -1):
            if J != Y and I != Y:
                P[I][J] = P[I+1][J] + P[I][J+1]
        Z3 += 1

    print_single_pasart(P, 1, T)

def main():
    print_pasart()

    print("THIS PROGRAM CREATES ARTIST DESIGNS BASED ON PASCAL'S TRIANGLE.")
    print("GLE.")
    print("YOU HAVE 3 BASIC TYPES OF DESIGNS TO SELECT FROM:")
    print("1. A SINGLE PASCAL'S TRIANGLE (PLAYED WITH AN ARTISTIC FLARE)")
    print("2. TWO 'ARTSY' PASCAL'S TRIANGLES PRINTED BACK TO BACK")
    print("3. FOUR 'ARTSY' TRIANGLES IN THE CORNER OF")
    print("   A SQUARE ARRAY.")

    O = int(input("WHAT'S YOUR PLEASURE? 1, 2 OR 3: "))
    Q = int(input("WHICH MULTIPLES DO YOU WANT REPRESENTED WITH BLANKS: "))
    T = int(input("HOW MANY ROWS AND COLUMNS IN THE ARRAY (36 IS MAXIMUM): "))

    if O == 1:
        P = create_pascals_triangle(T)
        print_single_pasart(P, Q, T)
    elif O == 2:
        P = create_pascals_triangle(T)
        print_double_pasart(P, T)
    elif O == 3:
        P = [[0] * T for _ in range(T)]
        print_corner_pasart(P, T)
    else:
        print("Invalid input. Please try again.")
        return

if __name__ == "__main__":
    main()
