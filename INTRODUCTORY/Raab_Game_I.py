import sys
input = sys.stdin.readline

def solve():
    n, a, b = map(int, input().split()) 

    if a + b  > n :
        print("NO")
        return
    
    if (a == 0 or b == 0) and a+b != 0 :
        print("NO")
        return
    
    print( "YES" )

    for i in range(1, n+1) : print(i, end = " ")
    print()

    for i in range(a+1, a+b+1) : print(i, end = " ")
    for i in range(1, a+1) : print(i, end = " ")
    for i in range(a+b+1, n+1) : print(i, end = " ")
    print()

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()