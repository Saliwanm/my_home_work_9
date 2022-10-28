from app import app
from models.models import Plant
from flask import render_template, request, redirect


@app.route('/add-plant')
def add_plant():
    return render_template("add_plant.html")


@app.route('/plant-info/<int:id>')
def plant_info(id):
    info = Plant.get_by_id_site(id)
    infoplant = Plant.get_plant_by_id_site(id)
    return render_template("plant_info.html", info=info, infoplant=infoplant)


@app.route('/save-plant', methods=['POST'])
def save_plant():
    name = request.form.get('name')
    location = request.form.get('location')
    plant = Plant(name, location)
    plant.save()
    return redirect('/')


@app.route('/delete-plant/<int:id>')
def delete_plant(id):
    Plant.delete(id)
    return redirect('/')