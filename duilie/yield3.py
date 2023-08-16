#未使用生成器的版本
#ts
import pathlib
import re
for path in pathlib.path('.').rglob('*.py'):
    pass
    if path.exists():
        with path.open('rt',encoding='latin-1') as file:
            for line in file:
                m=re.match('.*(#.*)$',line)
                if m:
                    comment = m.group(1)
                    if 'spam' in comment:
                        print(comment)
