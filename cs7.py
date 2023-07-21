import datetime,os
# 临时写的python 程序,拼接sql语句
def process_file(input_file,output_file,new_file):
    with open(input_file,'r') as file:
        lines=file.readlines()
        keys_to_remove=[line.strip().split('|+|')[0]  for line in lines]
    with open(output_file,'r') as file:
        lines=file.readlines()
        new_lines=[]
        count=0
        log=[]
        for line in lines:
            if 'PAGENO' in line:
                continue
            if '</PAGE>' in line:
                continue
            parts=line.strip().split('|+|',1)
            if 'DP20' in line:
                 if parts[0] not in keys_to_remove:
                    new_lines.append('|+|'.join(parts)+'\n')
                    count+=1
            else:
                new_lines.append(line)
                log.append('|+|'.join(parts)+'\n')
    with open("cs.log",'w') as file:
        file.writelines(log)
    with open(new_file,'w') as file:
        file.writelines(new_lines)