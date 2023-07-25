from  flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)  # initilize Flask class

@app.route('/home')
def home():
    return 'Welcome to Flask'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return 'The Person passed and the avg score % is : ' + str(score)
@app.route('/failure/<int:score>')
def failure(score): 
    return 'The Person failed and the avg score % is: ' + str(score)
@app.route('/calculate', methods=['GET','POST'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')
    elif request.method == 'POST':
         math_score = float(request.form['maths'])
         science_score = float(request.form['science'])
         history_score = float(request.form['history'])
         subjects   = [math_score,science_score,history_score]

    return render_template('result.html',score=subjects)
        # avg_score = (math_score+science_score+history_score)/3
        # result = ""
        # if avg_score > 50 :
        #     result = "success"
        # elif avg_score <= 50 :
        #     result = "failure"
         # return redirect(url_for(result,score=avg_score))  
        
        
if __name__ == '__main__':
    app.run(debug=True)


