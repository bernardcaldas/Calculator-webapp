from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print('enter in func')
    num_1 = request.form.get('num_1', type=int)
    num_2 = request.form.get('num_2', type=int)
    operation = request.form.get('operation')
    if(operation == 'Add'):
        result = num_1 + num_2
    elif(operation == 'Sub'):
        result = num_1 - num_2
    elif(operation == 'Mult'):
        result = num_1 * num_2
    elif(operation == 'Div'):
        result = num_1 / num_2
    else:
        result = 'Invalid operation'
    entry = result
    print(request.form)
    #return render_template('index.html')
    #return redirect(request.url)
    #return render_template('result.html', entry=entry)
    #return redirect(url_for('index'))
    #return jsonify(result)
    #return redirect(url_for('success',entry=entry))
    return render_template('result.html', entry=entry)

    
if __name__ == '__main__':
    app.run(debug=True)    