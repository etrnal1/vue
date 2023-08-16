# 使用yield 将程序分拆为工作流 一步一步实现
# yield处理管道和工作流相关的各种数据时,生成器特别有效
import pathlib
import re

def get_paths(topdir,pattern):
    pass
    for path in pathlib.Path(topdir).rglob(pattern):
        if path.exists():
            yield path

def get_files(paths):
    pass
    for path in paths:
        with path.open('rt',encoding='latin-1') as file:
            yield file
def get_lines(files):
   for file in files:
        yield from file

def get_comments(lines):
    pass
    for line in lines:
        m=re.match('.*(#.*)$',line)
        if m:
            yield m.group(1)
def print_matching(lines,substring):
    pass
    for line in lines:
        if substring in line:
            print(substring)

paths=get_paths('.','*.py')
files=get_files(paths)
lines=get_lines(files)
comments=get_comments(lines)
print_matching(comments,'ts')