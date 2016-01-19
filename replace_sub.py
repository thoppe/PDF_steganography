import argparse, ast, string

parser = argparse.ArgumentParser()
parser.add_argument("--f_text_in" ,help="[input] text file to replace",
                    required=True)
parser.add_argument("--f_cmap_in", help="[input] character map",
                    required=True)
parser.add_argument("--f_text_out", help="[output] text result",
                    required=True)
args = parser.parse_args()

with open(args.f_cmap_in) as FIN:
    raw_cmap = FIN.read()
    CMAP = ast.literal_eval(raw_cmap)

table1,table2 = zip(*CMAP.items())
trans_table = string.maketrans(''.join(table1), ''.join(table2))

with open(args.f_text_in,'r') as FIN:
    raw = FIN.read()
    
with open(args.f_text_out,'w') as FOUT:
    FOUT.write( raw.translate(trans_table) )
