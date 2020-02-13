from flask import request
from flask_restplus import Resource

from api.status_dto import StatusDTO
from extensions import db
from model.status import Status
from serializer.status_schema import StatusSchema

namespace = StatusDTO.namespace


@namespace.route('/')
class ListStatus(Resource):

    @namespace.doc(params={
        'date': 'status date',
        'type': 'status type'
    })
    @namespace.doc('get all statuses')
    def get(self):
        """
        Returns list of statuses
        """
        data = request.args
        results = []

        if 'date' in request.args and 'type' in request.args:
            date = data['date']
            type = data['type']
            statuses = Status.query.filter_by(Status.date == date) \
                .filter_by(Status.type == type) \
                .all()
        elif 'date' in request.args:
            date = data['date']
            statuses = Status.query.filter(Status.date == date).all()
        else:
            statuses = Status.query.all()

        for status in statuses:
            result = StatusSchema().dump(status)
            results.append(result)
        return results


@namespace.route('/add')
class AddStatus(Resource):
    @namespace.response(201, 'Status successfully added')
    @namespace.doc('add new status')
    def post(self):
        """
        Creates a new status
        """
        data = request.json
        status = Status(
            type=data['type'],
            date=data['date'],
            date_created=data['date_created'],
            date_modified=data['date_modified'],
            hours=data['hours'],
            comment=data['comment'],
            is_all_day=data['is_all_day'],
            user_id=data['user_id']
        )
        db.session.add(status)
        db.session.commit()

@namespace.route('/own')
class MyListStatus(Resource):

    @namespace.doc('get own statuses')
    def get(self):
        """Returns list of my statuses"""
        results = []
        statuses = Status.query.all()

        for status in statuses:
            result = StatusSchema().dump(status)
            results.append(result)
        return results


@namespace.route('/<int:id>')
@namespace.param('id', 'The status identifier')
@namespace.response(404, 'Status not found')
class ItemStatus(Resource):

    @namespace.doc('get status by id')
    def get(self, id):
        """
        Returns a status
        """
        status = Status.query.filter_by(_id=id).first()

        if not status:
            return "not"
        else:
            return  StatusSchema().dump(status)
