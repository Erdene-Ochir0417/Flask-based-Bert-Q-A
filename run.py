from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/japanese', methods=['GET','POST'])
def japanese():
    if request.method == 'POST':
        context = request.form['context']
        question = request.form['question']
    
        return render_template('japanese_output.html', context=context, question=question)

    return render_template('japanese.html')

@app.route('/english', methods=['GET','POST'])
def english():
    if request.method == 'POST':
        context = request.form['context']
        question = request.form['question']

        return render_template('english_output.html', context=context, question=question)

    return render_template('english.html')

if __name__ == "__main__":
    app.run()
