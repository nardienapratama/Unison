# from flask import render_template
from flask import Blueprint, jsonify, request
from .import db
from .models import PracticeRecord
from datetime import datetime
import json

main = Blueprint('main', __name__)

# @main.route('/')
# @main.route('/index')
# def index():
    # return render_template('app.js', title="Title")

@main.route('/add_practicerecord', methods=['POST'])
def add_practiceRecord():
    practiceRecord_data = request.get_json()

    #practiceRecord_data['date'] is the string value of the datetime.
    #in order to save in DB you must create datetime object like this:

    datetime_new = datetime.strptime(practiceRecord_data['date'], '%Y-%m-%d')
    created_new = datetime.strptime(practiceRecord_data['created'], '%Y-%m-%dT%H:%M:%S.%f')
    updated_new = datetime.strptime(practiceRecord_data['updated'], '%Y-%m-%dT%H:%M:%S.%f')

    # better practice to serialize using .get_delete_out_post - see flask-serialize
    # record_id = request.args.get('record_id')
    # practiceRecord_data = PracticeRecord.get_delete_put_post(record_id)

    new_practiceRecord = PracticeRecord(description=practiceRecord_data['description'], 
                        date=datetime_new, minutes=practiceRecord_data['minutes'],
                        created=created_new, updated=updated_new)

    db.session.add(new_practiceRecord)
    db.session.commit()

    return 'Done', 201

@main.route('/practicerecords')
def practiceRecords():
    #can't send practiceRecords_list directly to jsonify because this is a sqlalchemy query result object
    practiceRecords_list = PracticeRecord.query.all()
    practiceRecords = []

    for record in practiceRecords_list:
        practiceRecords.append({'description': record.description, 'date': record.date, 
        'minutes': record.minutes, 'created': record.created, 'updated': record.updated})
    return jsonify({'practiceRecords': practiceRecords})