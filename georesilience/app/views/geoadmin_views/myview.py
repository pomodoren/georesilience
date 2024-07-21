import os
from flask import Flask, url_for, redirect, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy

from flask_admin.contrib.geoa import ModelView as MVA
from flask_admin.form import rules


# Create customized model view class
class MyModelView(MVA):

    # scan_delete = False
    page_size = 50
    can_export = True
    # form_excluded_columns = ['id']


class GeoView(MyModelView):
    column_list = ["id", "name", "description", "geometry"]
    # can_edit = False
    # can_create = False
    # can_delete = False


class NonGeoView(MyModelView):
    column_list = ["id", "name", "description"]
