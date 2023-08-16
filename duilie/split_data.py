import os
input_file="./1.xml"
out_file="2.xml"
with open(input_file,"r",encoding="utf-8") as infile,open(out_file,'w',encoding="utf-8") as outfile:
    for line in infile:
        print(line)
        fields=line.strip().split("|+|")
        print(fields)
        new_fields = [field for idx,field in enumerate(fields,start=1)]
        outfile.write("|+|".join(new_fields)+"\n")