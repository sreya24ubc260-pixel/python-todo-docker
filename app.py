from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append({"task": task, "done": False})
    return redirect(url_for('home'))

@app.route('/complete/<int:index>')
def complete(index):
    if index < len(tasks):
        tasks[index]['done'] = True
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete(index):
    if index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)