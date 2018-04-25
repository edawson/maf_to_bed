import sys

if __name__ == "__main__":
    
    slop = 20
    for line in sys.stdin:
        if line .startswith ("#") or line.startswith("individual") or line.startswith("Hugo_Symbol"):
            continue
        tokens = line.strip().split("\t")
        chr_1 = tokens[4]
        start = int(tokens[5])
        end = int(tokens[6])
        line_one = "\t".join([ chr_1, str(start - slop), str(start + slop), ";".join(tokens)])
        print(line_one)
