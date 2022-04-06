from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
import json

# Flask app and database initialization
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///config.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# DATABASE CODE
class Macro(db.Model): # commands that can be selected
    __tablename__ = "macros"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    cmd = db.Column(db.String)
    priority = db.Column(db.Integer)
    selected = db.Column(db.Boolean)

    def to_json(self):
        return dict(id=self.id, name=self.name, cmd=self.cmd, priority=self.priority, selected=self.selected)


# API CODE
@app.route("/macros")
def get_macros():
    macros = Macro.query.all()
    return {"macros": [macro.to_json() for macro in macros]}


@app.route("/macros/new", methods=["POST"])
def new_macro():
    macro = Macro(name=request.json["name"], cmd=request.json["cmd"], priority=1, selected=False)
    db.session.add(macro)
    db.session.commit()
    return macro.to_json()


@app.route("/macros/delete/<id>", methods=["POST"])
def delete_macro(id):
    macro = Macro.query.get_or_404(id)
    db.session.delete(macro)
    db.session.commit()


@app.route("/macros/set/<id>", methods=["POST"])
def set_macro_attribute(id):
    macro = Macro.query.get_or_404(id)
    if request.json["attribute"] != "id":
        setattr(macro, request.json["attribute"], request.json["value"])
        return {"success": 1}
    else:
        return {"success": 0}


@app.route("/macros/run")
def run_macros():
    macros = [macro for macro in Macro.query.all() if macro.selected]
    # sort and execute macros in ascending order of priority
    for macro in sorted(macros, key=lambda m : m.priority):
        os.system(macro.cmd)
    return {"success": 1}
