# -*- coding: utf-8 -*-
"""Google Cloud Billing Budgets API."""

from bits.google.services.base import Base
from googleapiclient.discovery import build
from google.cloud.billing_budgets import BudgetServiceClient
from google.protobuf import json_format


class CloudBillingBudgets(Base):
    """CloudBilling class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        self.budgets = build('billingbudgets', 'v1beta1', credentials=credentials)
        self.api_version = 'v1alpha1'
        self.credentials = credentials
        self.client = BudgetServiceClient()

    def create_budget(self, parent, body):
        """Create a budget in the given billing account."""
        if 'billingAccounts/' not in parent:
            parent = 'billingAccounts/{}'.format(parent)
        params = {
            'parent': parent,
            'body': body,
        }
        return self.budgets.billingAccounts().budgets().create(**params).execute()

    def delete_budget(self, parent, budget_id):
        """Delete a budget."""
        if 'billingAccounts/' not in parent:
            parent = 'billingAccounts/{}'.format(parent)
        if 'budgets/' not in budget_id:
            budget_id = 'budgets/{}'.format(budget_id)
        name = '{}/{}'.format(parent, budget_id)
        return self.budgets.billingAccounts().budgets().delete(name=name).execute()

    def get_budget(self, parent, budget_id):
        """Return a budget for a given billing account."""
        if 'billingAccounts/' not in parent:
            parent = 'billingAccounts/{}'.format(parent)
        if 'budgets/' not in budget_id:
            budget_id = 'budgets/{}'.format(budget_id)
        name = '{}/{}'.format(parent, budget_id)
        return self.budgets.billingAccounts().budgets().get(name=name).execute()

    def get_budgets(self, parent):
        """Return a list of budgets for the given billing account via the API."""
        if 'billingAccounts/' not in parent:
            parent = 'billingAccounts/{}'.format(parent)
        budgets = self.budgets.billingAccounts().budgets()
        request = budgets.list(parent=parent)
        return self.get_list_items(budgets, request, 'budgets')

    def list_budgets(self, parent):
        """Return a list of budgets for the given billing account via the client."""
        if 'billingAccounts/' not in parent:
            parent = 'billingAccounts/{}'.format(parent)
        budgets = []
        for budget in self.client.list_budgets(parent=parent):
            budgets.append(json_format.MessageToDict(budget))
        return budgets

    def update_budget(self, parent, budget_id, body):
        """Update a budget in the given billing account."""
        if 'billingAccounts/' not in parent:
            parent = 'billingAccounts/{}'.format(parent)
        if 'budgets/' not in budget_id:
            budget_id = 'budgets/{}'.format(budget_id)
        name = '{}/{}'.format(parent, budget_id)
        params = {
            'name': name,
            'body': body,
        }
        return self.budgets.billingAccounts().budgets().get(**params).execute()
