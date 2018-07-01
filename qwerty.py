from flask import *
info={}
store_comments=[]

app=Flask(__name__)
app.secret_key="koech"
@app.route('/')
def index():
    return "<h2><a href = '/loginPage'></b>" + \
          "login here</b></a><br><br><a href = '/register'>register</a></h2>" 
@app.route('/loginPage')
def loginPage():
    return render_template('test.html')
@app.route('/post_comments',methods = ['GET','POST'])

# route for home page
def post_comments():
    if request.method=='post':
        if request.form['username'] in info:
            if request.form['password']==info[request.form['username']][4]:
                session['username']=request.form['username'] 
                session['logged_in']=True
                return render_template('index.html')
            else:
                return "<h2>Wrong password </h2><br><a href =\"/loginPage\">Try Again</a>"
        elif request.form['username'] not in info:
            return "Unregistered User"            
        else:
            return redirect(url_for('loginPage'))
    elif session['logged_in']:
        return render_template('index.html')
    
    elif not session['logged_in']:
        return redirect(url_for('loginPage'))
    else:redirect(url_for('loginPage'))
        
    
"""
@app.route('/write_comment',method=['POST'])
def write_comment():
    if session['logged_in']:
        store_comments(request.form('write'))
        return redirect(url_for('post_comments'))
    return redirect(url_for('loginPage'))
"""
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/reg', methods=['POST'])
def reg_data():
    if request.method=='post':
        fname=request.form['Fname']
        lname=request.form['Lname']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        info.update({username:[fname,lname,email,username,password]})
        
    return redirect(url_for('loginPage'))
    
   # return render_template('register.html')
@app.route('/logout')
def logout():
    session.pop('username',None)
    session['logged_in']=False
    return redirect(url_for('loginPage'))
@app.route('/post',methods=['POST'])
def post():
    if session['logged_in']:
        comm="<h2>my comments</h2>"
        store_comments.append(request.form['write'])
        for each in store_comments:
            comm +="<p>" +each+"</p><br>"
        return comm
    else:
        redirect(url_for('loginPage'))
    
@app.route('/view_comments')
def view_comments():
    comm="<h2>my comments</h2>"
    if session['logged_in']:
        return comm

if __name__=='__main__':
    app.run(port=9870,debug=True)
    