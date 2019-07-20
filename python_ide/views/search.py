from flask import Blueprint,render_template,request,redirect
from python_ide.app import db
from python_ide.views.save import Codes
bp = Blueprint(__name__,__name__,template_folder='templates')

@bp.route('/search',methods=['GET','POST'])
def search():
    all=[]
    if request.method=='POST':
        if request.form.get('search'):
            query=request.form.get('search_query')
            try:
                #all=Codes.query.all()
                all=Codes.query.whoosh_search(query,or_=True).all()
        
            except:
                all=[]
        
    
    return render_template('search.html',codes=all)