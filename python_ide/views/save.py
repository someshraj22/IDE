from flask import Blueprint,render_template,request,redirect
import flask_whooshalchemy as wa
from python_ide.app import db,app
import random
bp = Blueprint(__name__,__name__,template_folder='templates')


def random_String(length=16):
    chars='abcdefghijklmnopqrstuvwxyz0123456789'
    name=''
    for i in range(0,length):
        name=name+chars[random.randint(0,len(chars)-1)]
    return name
class Codes(db.Model):
    __tablename__='Codes'
    __searchable__=['description','tags']
    code_id=db.Column('code_id',db.Unicode,primary_key=True)
    description=db.Column('description',db.Unicode)
    tags=db.Column('tags',db.Unicode)
    code=db.Column('code',db.Unicode)

    def __init__(self,code_id,description,tags,code):
        self.code_id=code_id
        self.description=description
        self.tags=tags
        self.code=code

wa.whoosh_index(app,Codes)
@bp.route('/save',methods=['GET','POST'])
def save():
    if request.method == 'POST':
        if request.form.get('save'):
            code=request.form.get('code')
            tags=request.form.get('tags')
            description=request.form.get('problem')
            code_id=random_String()
            temp=Codes(code_id,description,tags,code)
            
            db.session.add(temp)
            db.session.commit()

            return redirect("/")
            
    return render_template('save.html')