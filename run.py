from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        context = request.form['context']
        question = request.form['question']
    
        return render_template('output.html', context=context, question=question)

    return render_template('index.html')


if __name__ == "__main__":
    app.run()
