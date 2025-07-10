import sys
import struct

# Fix integrity (after opening and saving file in internal editor)

# Load the existing level
input_filename = R"C:\Programs\EOL\lev\test.lev"

print(sys.float_info)

integrity_bound = (
    (0, 0),
    (9786, 20000),
    (9786, 20000),
    (9875, 20000),
)

# Fix integrity check value
def fix(base, cur, i):
    min = integrity_bound[i][0]
    max = integrity_bound[i][1]
    #print(i, base, min, base + cur, max)
    # Already within range
    if min <= base + cur <= max:
        return cur
    # Get it more or less within range
    cur = min - base
    if min <= base + cur <= max:
        return cur
    # Nudge it into the right range
    if base + cur < min:
        offset = 1
        while base + cur < min:
            new = cur + offset
            if new == cur:
                offset *= 2
            cur = new
            #print(i, base, min, base + cur, max, offset)
    # No possible existing adjustment possible
    if base + cur > max:
        #print(i, base, min, base + cur, max)
        raise ValueError("Unable to fix")
    return cur

with open(input_filename, 'r+b') as f:
    f.seek(11)
    integrities = list(struct.unpack('<dddd', f.read(8*4)))
    for i in range(1, 4):
        integrities[i] = fix(integrities[0], integrities[i], i)
        print(integrities[0] + integrities[i])
    f.seek(11)
    f.write(struct.pack('<dddd', *integrities))
