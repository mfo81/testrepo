from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        idea_title = request.form['Idea']
        idea_type = request.form['Idea type']
        business = request.form['Business']
        leader = request.form['Leader']
        process = request.form['Process name']
        problem_statement = request.form['Problem']
        recommendation = request.form['Recommendation']
        print(idea_title, idea_type, business, leader, process, problem_statement, recommendation)
        return render_template('success.html')



if __name__ == '__main__':
    app.debug = True
    app.run()