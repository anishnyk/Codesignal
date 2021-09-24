# time complexity O[n]
# space complexity O[1]

def rotateImage(a):
    
    n = len(a)
    for i in range((n+1)//2):
        for j in range(i, n-1-i):
            r, c = i, j
            temp = a[r][c]
            for _ in range(4):
                new_r, new_c = new_coords(r, c, n)
                swap = a[new_r][new_c]
                a[new_r][new_c] = temp
                temp = swap
                r, c = new_r, new_c         
        
    return a
            
            
def new_coords(r, c, n):
    # new_c = len(a) - r - 1
    # new_r = c
    return (c, n - r - 1)