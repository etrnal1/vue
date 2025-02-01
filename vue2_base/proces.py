import subprocess
try:
    pass
    out=subprocess.check_output(['ps','-a']) 
    text=out.decode('utf-8')
    print(text)
except Exception as e:
    #pass
    print("it failed:",e)