import argparse, string, random

parser = argparse.ArgumentParser()
parser.add_argument("--f_raw_in" , help="[input] raw font",
                    required=True)
parser.add_argument("--f_raw_out", help="[output] modified raw font",
                    required=True)
parser.add_argument("--CMAP", help="[output] CMAP file", required=True)
args = parser.parse_args()

code_to_char = dict()
char_to_code = dict()

with open(args.f_raw_in,'r') as FIN:
    for line in FIN:
        if "dup" in line and "put" in line:
            m = line.strip().split(' ')
            code_to_char[m[1]] = m[2]
            char_to_code[m[2]] = m[1]

#sub_letters = string.ascii_letters + string.whitespace + string.digits
sub_letters = string.ascii_letters

CMAP = dict()
C1 = ['/%s'%c for c in sub_letters]

C2 = C1[:]
random.shuffle(C2)

CMAP = dict()
for c1,c2 in zip(C1,C2): CMAP[c1] = c2


# Make the substitution
with open(args.f_raw_out,'w') as FOUT, open(args.f_raw_in,'r') as FIN:
    for line in FIN:
        c = line.split(' ')[0]
        if c in CMAP:
            line = line.replace(c,CMAP[c])
        FOUT.write("%s\n"% line.rstrip())

# Export a nicer version

CLEAN_MAP = dict()
for k in CMAP: 
    CLEAN_MAP[k[1:]] = CMAP[k][1:]

with open(args.CMAP,'w') as FOUT:
    FOUT.write(str(CLEAN_MAP))



