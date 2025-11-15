from flask import Flask,render_template,redirect,url_for,request,session
from models import StudentsModel,db

app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)



@app.route("/create",methods=["POST","GET"])
def create():
    if request.method=='GET':
        return render_template ('create.html')

    if request.method=="POST":
        hobby=request.form.getlist('hobbies')
        hobbies=",".join(map(str,hobby))
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        password=request.form['password']
        gender=request.form['gender']
        hobbies=hobbies
        country=request.form['country']

        students=StudentsModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            gender=gender,
            hobbies=hobbies,
            country=country,

        )
        db.session.add(students)
        db.session.commit()
        return redirect ('/')



@app.route("/", methods=['GET'])
def Retrievelist():
    students=StudentsModel.query.all()
    return render_template ('index.html',students=students)


if __name__=="__main__":
    with app.app_context():

        db.create_all()
    app.run(debug=True)
