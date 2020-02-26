#!/usr/bin/python3
import json
from copy import deepcopy
from pathlib import Path, PurePath
from PyQt5 import QtWidgets

try:
    from ..__db__ import DEFAULT
except ValueError:
    from __db__ import DEFAULT


class Database(dict):
    def __init__(self, path):
        path = Path(path)
        self.path = path
        self.name = path.stem
        self.fields = Fields(self)

        if path.is_file() and path.stat().st_size > 0:
            self._load()
            self._validate()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            default = deepcopy(DEFAULT)
            self.update(default)
            with open(path, "w") as f:
                f.write(json.dumps(self, indent=2, sort_keys=False))
            print(f"Created preferences file for '{self.name}'")

    def _load(self):
        with open(self.path, "r") as f:
            self.update(json.load(f))
        print(f"Loaded {self.name} database")

    def _repair(self, db, default):
        for key in default:
            if isinstance(default[key], dict):
                db.setdefault(key, default[key])
                self._repair(db[key], default[key])
            else:
                db.setdefault(key, default[key])
            if not isinstance(default[key], type(db[key])):
                print(f"Fixed type for '{key}': {type(key)} to {type(default[key])}")
                db[key] = default.get(key)

    def _validate(self):
        old = json.dumps(self, sort_keys=True)
        default = deepcopy(DEFAULT)
        self._repair(self, default)
        new = json.dumps(self, sort_keys=True)
        if not new == old:
            print(f"Repaired missing keys in {self.name} database")
            self.save()

    def reset(self):
        self.clear()
        self.update(DEFAULT)

    def save(self):
        self.fields.save()
        with open(self.path, "w") as f:
            f.write(json.dumps(self, indent=2, sort_keys=False, cls=Encoder))
        print(f"Saved {self.name} database")


class Encoder(json.JSONEncoder):
    def default(self, obj):
        """ Serialize sets and Path objects """
        if isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, (Path, PurePath)):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


class Fields(set):
    def __init__(self, parent):
        self.parent = parent

    def load(self):
        for obj in self:
            value = self.parent["__tracked__"][obj.objectName()]
            if isinstance(obj, QtWidgets.QLineEdit):
                obj.setText(value)
            elif isinstance(obj, QtWidgets.QComboBox):
                obj.setCurrentText(value)
            elif isinstance(obj, (QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
                obj.setPlainText(value)
            elif isinstance(obj, (QtWidgets.QCheckBox, QtWidgets.QRadioButton)):
                obj.setChecked(value)
            elif isinstance(obj, (QtWidgets.QSpinBox, QtWidgets.QDoubleSpinBox)):
                obj.setValue(value)
            else:
                print(f"Could not handle object type {type(obj)}")

    def save(self):
        for obj in self:
            name = obj.objectName()
            if isinstance(obj, QtWidgets.QLineEdit):
                self.parent["__tracked__"][name] = obj.text()
            elif isinstance(obj, QtWidgets.QComboBox):
                self.parent["__tracked__"][name] = obj.currentText()
            elif isinstance(obj, (QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
                self.parent["__tracked__"][name] = obj.toPlainText()
            elif isinstance(obj, (QtWidgets.QCheckBox, QtWidgets.QRadioButton)):
                self.parent["__tracked__"][name] = obj.isChecked()
            elif isinstance(obj, (QtWidgets.QSpinBox, QtWidgets.QDoubleSpinBox)):
                self.parent["__tracked__"][name] = obj.value()

    def track(self, objects: tuple):
        self.update(objects)
        self.load()
