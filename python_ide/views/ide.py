from flask import Blueprint,render_template,request,redirect
from python_ide.app import db
import random
from subprocess import Popen, PIPE
bp = Blueprint(__name__,__name__,template_folder='templates')

@bp.route("/ide",methods=['GET','POST'])
def ide():
    result=[]
    if request.method == 'POST':
        if request.form.get('run'):
            code=request.form.get('code')
            #writenotedb(text)
            #return redirect("/")
            
            out=""
            name=random_String()
            with open('python_ide/Codes/{}.cpp'.format(name),'w+') as _file:
                _file.write(code)
            _file.close()
            p1 = Popen(["g++", "python_ide/Codes/"+name+".cpp", "-o", "python_ide/Codes/"+name], stdout=PIPE, stderr=PIPE)
            err=p1.communicate()[1]
            
            if(err==''):
                p2 = Popen(["./python_ide/Codes/"+name],stdout=PIPE,stderr=PIPE)
                out=p2.communicate()[0]
            
            result.append(code)
            if(err == ''):
                result.append(out)
                
            else:
                temp=err.decode('utf-8')
                temp1='python_ide/Codes/'+name+'.cpp'
                error=temp.replace(temp1,"")

                result.append(error)
                
            #result.append(out)
            Popen(['rm','python_ide/Codes/'+name,'python_ide/Codes/'+name+'.cpp'],stdout=PIPE,stderr=PIPE)
            return render_template('ide.html',output=result)
            
            
    return render_template('ide.html',output=result)

def random_String(length=16):
    chars='abcdefghijklmnopqrstuvwxyz0123456789'
    name=''
    for i in range(0,length):
        name=name+chars[random.randint(0,len(chars)-1)]
    return name





