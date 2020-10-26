# Distinct Triples Morning Problem
# Careful with n = 673
n = int(input())
k = 3
count = 0

vec = []
for i in range(n):  # There's a better way, I am sure
    vec.append(" ")

index = 1
for i in range(n):
    # Change.  Do.
    vec[ i ] = str(i)
    for j in range(i+1, n-1):
        count += (n - j  - 1)

        # Change.  Do.
        vec[ j ] = str(j)
        for k in range(j+1, n):
            # Change.  Do.
            vec[ k ] = str(k)
            # print("%10d:" % index, end='')
            if n <= 8:
                # print(''.join(vec), "(%d,%d,%d)" % (i,j,k))
                pass
            else:
                # print()
                pass
            index += 1
            # Undo
            vec[ k ] = " "
        # Undo
        vec[ j ] = " "
   # Undo
    vec[ i ] = " "

# Prompts user:
# http://pythontutor.com/visualize.html#code=n%20%3D%20int%28input%28%29%29%0Ak%20%3D%203%0Acount%20%3D%200%0A%0Avec%20%3D%20%5B%5D%0Afor%20i%20in%20range%28n%29%3A%20%20%23%20There's%20a%20better%20way,%20I%20am%20sure%0A%20%20%20%20vec.append%28%22%20%22%29%0A%20%20%20%20%20%20%20%20%0Aindex%20%3D%201%20%20%20%0Afor%20i%20in%20range%28n%29%3A%0A%20%20%20%20%23%20Change.%20%20Do.%0A%20%20%20%20vec%5B%20i%20%5D%20%3D%20str%28i%29%0A%20%20%20%20for%20j%20in%20range%28i%2B1,%20n-1%29%3A%0A%20%20%20%20%20%20%20%20count%20%2B%3D%20%28n%20-%20j%20%20-%201%29%0A%0A%20%20%20%20%20%20%20%20%23%20Change.%20%20Do.%0A%20%20%20%20%20%20%20%20vec%5B%20j%20%5D%20%3D%20str%28j%29%0A%20%20%20%20%20%20%20%20for%20k%20in%20range%28j%2B1,%20n%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20Change.%20%20Do.%0A%20%20%20%20%20%20%20%20%20%20%20%20vec%5B%20k%20%5D%20%3D%20str%28k%29%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22%2510d%3A%22%20%25%20index,%20end%3D''%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20n%20%3C%3D%208%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28''.join%28vec%29,%20%22%28%25d,%25d,%25d%29%22%20%25%20%28i,j,k%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28%29%0A%20%20%20%20%20%20%20%20%20%20%20%20index%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20Undo%0A%20%20%20%20%20%20%20%20%20%20%20%20vec%5B%20k%20%5D%20%3D%20%22%20%22%0A%20%20%20%20%20%20%20%20%23%20Undo%0A%20%20%20%20%20%20%20%20vec%5B%20j%20%5D%20%3D%20%22%20%22%0A%20%20%20%23%20Undo%0A%20%20%20%20vec%5B%20i%20%5D%20%3D%20%22%20%22%0A%0Aprint%28count%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

# Hardcode n=6
# http://pythontutor.com/visualize.html#code=n%20%3D%206%0Ak%20%3D%203%0Acount%20%3D%200%0A%0Avec%20%3D%20%5B%5D%0Afor%20i%20in%20range%28n%29%3A%20%20%23%20There's%20a%20better%20way,%20I%20am%20sure%0A%20%20%20%20vec.append%28%22%20%22%29%0A%20%20%20%20%20%20%20%20%0Aindex%20%3D%201%20%20%20%0Afor%20i%20in%20range%28n%29%3A%0A%20%20%20%20%23%20Change.%20%20Do.%0A%20%20%20%20vec%5B%20i%20%5D%20%3D%20str%28i%29%0A%20%20%20%20for%20j%20in%20range%28i%2B1,%20n-1%29%3A%0A%20%20%20%20%20%20%20%20count%20%2B%3D%20%28n%20-%20j%20%20-%201%29%0A%0A%20%20%20%20%20%20%20%20%23%20Change.%20%20Do.%0A%20%20%20%20%20%20%20%20vec%5B%20j%20%5D%20%3D%20str%28j%29%0A%20%20%20%20%20%20%20%20for%20k%20in%20range%28j%2B1,%20n%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20Change.%20%20Do.%0A%20%20%20%20%20%20%20%20%20%20%20%20vec%5B%20k%20%5D%20%3D%20str%28k%29%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22%2510d%3A%22%20%25%20index,%20end%3D''%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20n%20%3C%3D%208%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28''.join%28vec%29,%20%22%28%25d,%25d,%25d%29%22%20%25%20%28i,j,k%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28%29%0A%20%20%20%20%20%20%20%20%20%20%20%20index%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20Undo%0A%20%20%20%20%20%20%20%20%20%20%20%20vec%5B%20k%20%5D%20%3D%20%22%20%22%0A%20%20%20%20%20%20%20%20%23%20Undo%0A%20%20%20%20%20%20%20%20vec%5B%20j%20%5D%20%3D%20%22%20%22%0A%20%20%20%23%20Undo%0A%20%20%20%20vec%5B%20i%20%5D%20%3D%20%22%20%22%0A%0Aprint%28count%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
