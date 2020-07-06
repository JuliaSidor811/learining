from flask import Flask, request, render_template, redirect, url_for

from forms import TodoForm
from models import TodosDB

app = Flask(__name__)
todos = TodosDB("kodilla.sqlite3")
app.config["SECRET_KEY"] = "nininini"


@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    if request.method == "POST":
        if form.validate_on_submit():
            todos.create(form.data['title'], form.data['description'], form.data['done'])
            todos.save_all()
        return redirect(url_for("todos_list"))
    return render_template("todos.html", form=form, todos=todos.all())


@app.route("/todos/<string:todo_id>/", methods=["GET", "POST"])
def todo_details(todo_id: str):
    todo = todos.get(todo_id)[-1]
    form = TodoForm(data=dict(zip(["title", "description", "done"], todo)))

    if request.method == "POST":
        if form.validate_on_submit() and todo_id == form.data['title']:
            todos.update(todo_id, form.data['description'], form.data['done'])
        return redirect(url_for("todos_list"))
    return render_template("todo.html", form=form, todo_id=todo_id)


if __name__ == "__main__":
    app.run(debug=True)
