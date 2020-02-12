# -*- coding: utf-8 -*-
"""Google Cloud Billing Budgets API."""

from bits.google.services.base import Base
from googleapiclient.discovery import build
from google.auth.transport.requests import AuthorizedSession
from google.cloud.billing_budgets import BudgetServiceClient
# from google.cloud.billing_budgets.types.budget_service import ListBudgetsRequest
from google.protobuf import json_format


class CloudBillingBudgets(Base):
    """CloudBilling class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        self.budgets = build('billingbudgets', 'v1beta1', credentials=credentials)
        self.api_version = 'v1alpha1'
        self.base_url = 'https://billingbudgets.googleapis.com/%s' % (
            self.api_version,
        )
        self.credentials = credentials
        self.requests = AuthorizedSession(self.credentials)

        self.client = BudgetServiceClient()

    def create_budget(self, billingAccountName, body):
        """Create a budget in the given billing account."""
        # params = {
        #     'billingAccountName': billingAccountName,
        #     'body': budgetName,
        # }
        # return self.budgets.budgets().create(**params).execute()
        url = '%s/billingAccounts/%s/budgets' % (
            self.base_url,
            billingAccountName,
        )
        return self.requests.post(url, json=body).json()

    def delete_budget(self, billingAccountName, budgetName):
        """Delete a budget."""
        # params = {
        #     'billingAccountName': billingAccountName,
        #     'budgetName': budgetName,
        # }
        # return self.budgets.budgets().delete(**params).execute()
        url = '%s/billingAccounts/%s/budgets/%s' % (
            self.base_url,
            billingAccountName,
            budgetName,
        )
        return self.requests.delete(url).json()

    def get_budget(self, billing_account_id, budget_id):
        """Return a budget for a given billing account."""
        if 'billingAccounts/' not in billing_account_id:
            billing_account_id = 'billingAccounts/{}'.format(billing_account_id)
        if 'budgets/' not in budget_id:
            budget_id = 'budgets/{}'.format(budget_id)
        name = '{}/{}'.format(billing_account_id, budget_id)
        return self.budgets.billingAccounts().budgets().get(name=name).execute()

    def get_budgets(self, parent):
        """Return a list of budgets for the given billing account."""
        if 'billingAccounts/' not in parent:
            parent = 'billingAccounts/{}'.format(parent)
        budgets = self.budgets.billingAccounts().budgets()
        request = budgets.list(parent=parent)
        return self.get_list_items(budgets, request, 'budgets')

    def list_budgets(self, parent):
        """List budgets for a billing account."""
        if 'billingAccounts/' not in parent:
            parent = 'billingAccounts/{}'.format(parent)
        budgets = []
        for budget in self.client.list_budgets(parent=parent):
            budgets.append(json_format.MessageToDict(budget))
        return budgets

    def update_budget(self, billingAccountName, budgetName, body):
        """Update a budget in the given billing account."""
        # params = {
        #     'billingAccountName': billingAccountName,
        #     'body': budgetName,
        # }
        # return self.budgets.budgets().update(**params).execute()
        url = '%s/billingAccounts/%s/budgets/%s' % (
            self.base_url,
            billingAccountName,
            budgetName,
        )
        # example = {
        #     'budget': {
        #         'displayName': 'My Fancy Budget',
        #         'budgetFilter': {
        #             'projects': [
        #                 'projects/project_id_to_monitor',
        #             ]
        #         },
        #         'amount': {
        #             'specifiedAmount': {
        #                 'units': 500,
        #             }
        #         },
        #         'thresholdRules': {
        #             'thresholdPercent': 1.0,
        #         }
        #     }
        # }
        return self.requests.patch(url, json=body).json()
