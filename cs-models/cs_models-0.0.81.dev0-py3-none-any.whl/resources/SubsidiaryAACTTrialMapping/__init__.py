from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import and_
from marshmallow import ValidationError

from ...database import db_session
from ...resources.SubsidiaryAACTTrialMapping.models import (
    SubsidiaryAACTTrialMappingModel,
)
from .schemas import (
    SubsidiaryAACTTrialResourceSchema,
    SubsidiaryAACTTrialQueryParamsSchema,
)
from ...utils.utils import update_model


schema_resource = SubsidiaryAACTTrialResourceSchema()
schema_params = SubsidiaryAACTTrialQueryParamsSchema()


class SubsidiaryAACTTrialMapping(object):
    @staticmethod
    def create(params):
        """
        Args:
            params: dict(SubsidiaryAACTTrialResourceSchema)

        Returns: SubsidiaryAACTTrialResourceSchema

        Raises:
            ValidationError
            SQLAlchemyError
        """
        data, errors = schema_resource.load(params)
        if errors:
            raise ValidationError(errors)
        response = _helper_create(data)
        return response

    @staticmethod
    def read(params):
        """
        Args:
            params: dict(SubsidiaryAACTTrialQueryParamsSchema)

        Returns: List<SubsidiaryAACTTrialResourceSchema>

        Raises:
            ValidationError
        """
        data, errors = schema_params.load(params)
        if errors:
            raise ValidationError(errors)
        subsidiary_aact_trial_query = _build_query(params=data)
        response = schema_resource.dump(
            subsidiary_aact_trial_query, many=True).data
        return response

    @staticmethod
    def one(params):
        """
        Args:
            params: dict(SubsidiaryAACTTrialQueryParamsSchema)

        Returns: SubsidiaryAACTTrialResourceSchema

        Raises:
            ValidationError
        """
        data, errors = schema_params.load(params)
        if errors:
            raise ValidationError(errors)
        subsidiary_aact_trial_query = _build_query(params=data).one()
        response = schema_resource.dump(subsidiary_aact_trial_query).data
        return response

    @staticmethod
    def upsert(params):
        """
        Args:
            params: SubsidiaryAACTTrialResourceSchema

        Returns:
            SubsidiaryAACTTrialResourceSchema

        Raises:
            ValidationError
        """
        data, errors = schema_resource.load(params)
        if errors:
            raise ValidationError(errors)

        try:
            query_params = {
                'nct_id': params['nct_id'],
                'subsidiary_id': params['subsidiary_id'],
            }
            subsidiary_aact_trial_query = _build_query(query_params).one()
            response = _helper_update(data, subsidiary_aact_trial_query)
        except NoResultFound:
            response = _helper_create(data)
        return response


def _helper_create(data):
    new_subsidiary_aact_trial_mapping = SubsidiaryAACTTrialMappingModel(**data)
    try:
        db_session.add(new_subsidiary_aact_trial_mapping)
        db_session.commit()
        subsidiary_aact_trial_mapping_query = db_session.query(
            SubsidiaryAACTTrialMappingModel
        ).get(
            new_subsidiary_aact_trial_mapping.id
        )
        response = schema_resource.dump(
            subsidiary_aact_trial_mapping_query
        ).data
        return response
    except SQLAlchemyError:
        db_session.rollback()
        raise


def _helper_update(data, subsidiary_aact_trial_query):
    data['id'] = subsidiary_aact_trial_query.id
    try:
        update_model(data, subsidiary_aact_trial_query)
        db_session.commit()
        response = schema_resource.dump(subsidiary_aact_trial_query).data
        return response
    except SQLAlchemyError:
        db_session.rollback()
        raise


def _build_query(params):
    q = db_session.query(
        SubsidiaryAACTTrialMappingModel)
    if params.get('id'):
        q = q.filter_by(id=params.get('id'))
    if params.get('nct_id'):
        q = q.filter_by(
            nct_id=params.get('nct_id'))
    if params.get('subsidiary_id'):
        q = q.filter_by(
            subsidiary_id=params.get('subsidiary_id'))
    return q
