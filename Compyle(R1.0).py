# Clear File (Temporary)
with open('newgcode.txt', 'w') as newgcode:
    newgcode.write('')



# Functions
def remove_ef(rline):
    """Remove feedrate (F) and e-axis (E) commands from a line."""

    e_start = rline.find('E')  # start of E
    f_start = rline.find('F')  # start of F
    f_end = rline.find(' ', f_start + 1)  # space after F

    # Removes E and F
    if f_start != -1 and f_end != -1 and e_start != -1:
        rline = f'{rline[: f_start]}{rline[(f_end + 1) : (e_start - 1)]}\n'

    elif f_start != -1 and f_end != -1:
        rline = f'{rline[: f_start]}{rline[(f_end + 1) :]}'

    elif e_start != -1:
        rline = f'{rline[: (e_start - 1)]}\n'

    return rline if len(rline.strip()) > 2 else ''

def get_g(rline):
    """Returns G-Code command from line."""

    return rline.split(' ')[0]

def start_id(filename):
    """Find line index of 'Translator Call ID' comment."""

    with open(filename) as f:
        for count, line in enumerate(f, start = 1):
            if line.strip() == ';Translater Call ID':
                return count

    return -1

def end_id(filename):
    """Find line index of 'End Code Call ID' comment."""

    with open(filename) as f:
        for count, line in enumerate(f, start = 1):
            if line.strip() == ';End Code Call ID':
                return count

    return -1

# Main Program
import_file = 'BenchyTest.gcode' # original G-Code filename
export_file = 'newgcode.txt' # new G-Code filename
v = 20.0 # speed [mm/s]
pressure = 65.0 # psi
dwell = 0.15 # seconds



curastart = 7 # offset for mandatory Cura start G-Code
gval = 'G0' # G-Code command used to compare
startindex = start_id(import_file)
endindex = end_id(import_file)


sfile = open(import_file)
newgcode = open(export_file, 'a') # New G-Code file



for linecount, aline in enumerate(sfile, start = 1):
    g = get_g(aline)

    if (startindex + curastart) < linecount < endindex and (g in ['G0', 'G1']):
        if g != gval:
            if g == 'G1': # if next G-Code line is a G1 command
                newgcode.write('Call toggle_pressure_nordson_updated P0 ; ON\n')
                newgcode.write(f'G4 P{dwell}\n')
                newgcode.write(remove_ef(aline))

            elif g == 'G0': # if next G-Code line is a G0 command
                newgcode.write('Call toggle_pressure_nordson_updated P0 ; OFF\n')
                newgcode.write(remove_ef(aline)) # change G0 (absolute move) to G1

        else:
            newgcode.write(remove_ef(aline))

        gval = g

    elif (startindex + 1) < linecount <= (startindex + curastart):
        newgcode.write('')

    else:
        if 'Call set_pressure_nordson_updated P0 Q' in aline: # sets pressure
            newgcode.write(f'Call set_pressure_nordson_updated P0 Q{pressure}\n')

        elif 'G1 F' in aline: # sets speed
            newgcode.write(f'G1 F{v}\n')

        else:
            newgcode.write(aline)



sfile.close()
newgcode.close()