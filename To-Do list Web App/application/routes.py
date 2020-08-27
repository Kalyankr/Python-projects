from application import app, db
from flask import Flask, render_template, redirect, url_for, flash, get_flashed_messages
from application import forms, models

# from models import Task

# from models import Task
from datetime import datetime


@app.route("/")
@app.route("/index")
def index():
    tasks = models.Task.query.all()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = models.Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash("Task added successfully")
        return redirect(url_for("index"))
    return render_template("add.html", form=form)


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    task = models.Task.query.get(task_id)
    form = forms.AddTaskForm()
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash("Task Updated Scuccessfully")
            return redirect(url_for("index"))
        form.title.data = task.title
        return render_template("edit.html", form=form, task_id=task_id)
    else:
        flash("Task not Found!!!")
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["GET", "POST"])
def delete(task_id):
    task = models.Task.query.get(task_id)
    form = forms.DeleteTask()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("Task Deleted Scuccessfully")
            return redirect(url_for("index"))
        return render_template("delete.html", form=form, title=task.title, task_id=task_id)
    else:
        flash("Task not Found!!!")
    return redirect(url_for("index"))

