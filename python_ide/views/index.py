from flask import Blueprint,render_template,request,redirect
bp = Blueprint(__name__,__name__,template_folder='templates')

@bp.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')