"""
FyleExtractConnector(): Connection between Fyle and Database
"""

import logging
from os import path
import sqlite3
from typing import List
import pandas as pd


class FyleExtractConnector:
    """
    - Extract Data from Fyle and load to Database
    """

    def __init__(self, fyle_sdk_connection, dbconn):
        self.__dbconn = dbconn
        self.__connection = fyle_sdk_connection
        self.__dbconn.row_factory = sqlite3.Row

        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info('Fyle connection established')

    def create_tables(self):
        """
        Creates DB tables
        :return: None
        """
        basepath = path.dirname(__file__)
        ddl_path = path.join(basepath, 'extract_ddl.sql')
        ddl_sql = open(ddl_path, 'r').read()
        self.__dbconn.executescript(ddl_sql)

    def extract_settlements(self, updated_at: List[str] = None, exported: bool = None) -> List[str]:
        """
        Extract settlements from Fyle
        :param updated_at: Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
        :param exported: True for exported settlements and False for unexported settlements
        :return: List of settlement ids
        """

        self.logger.info('Extracting settlements from Fyle.')

        settlements = self.__connection.Settlements.get_all(updated_at=updated_at, exported=exported)

        df_settlements = pd.DataFrame(settlements)
        self.logger.info('%s settlements extracted.', str(len(df_settlements.index)))

        if settlements:
            df_settlements = df_settlements[[
                'id', 'created_at', 'updated_at', 'opening_date', 'closing_date',
                'employee_id', 'employee_email', 'employee_code', 'creator_employee_id',
                'creator_employee_email', 'creator_employee_code', 'org_id', 'org_name',
                'exported'
            ]]

            df_settlements.to_sql('fyle_extract_settlements', self.__dbconn, if_exists='append', index=False)
            return df_settlements['id'].to_list()

        return []

    def extract_employees(self) -> List[str]:
        """
        Extract employees from Fyle
        :return: List of employee ids
        """

        self.logger.info('Extracting employees from Fyle.')
        employees = self.__connection.Employees.get_all()

        self.logger.info('%s employees extracted.', str(len(employees)))

        if employees:
            df_employees = pd.DataFrame(employees)

            df_employees = df_employees[[
                'id', 'created_at', 'updated_at', 'employee_email', 'employee_code',
                'full_name', 'joining_date', 'location', 'level_id', 'level',
                'business_unit', 'department_id', 'department', 'sub_department',
                'approver1_email', 'approver2_email', 'approver3_email', 'title',
                'branch_ifsc', 'branch_account', 'mobile', 'delegatee_email',
                'default_cost_center_name', 'disabled', 'org_id', 'org_name'
            ]]

            df_employees.to_sql('fyle_extract_employees', self.__dbconn, if_exists='append', index=False)
            return df_employees['id'].to_list()

        return []

    def extract_expenses(self, settlement_ids: List[str] = None, state: List[str] = None,
                         fund_source: List[str] = None, reimbursable: bool = None, updated_at: List[str] = None,
                         exported: bool = None, extract_custom_fields: bool = True, spent_at: List[str] = None, report_ids: List[str] = None) -> List[str]:
        """
        Extract expenses from Fyle
        :param extract_custom_fields: Flag to extract custom fields, true by default
        :param updated_at: Extract expenses in exported_at date range
        :param exported: True for exported expenses and False for unexported expenses
        :param settlement_ids: List of settlement_ids
        :param state: List of expense states
        :param fund_source: List of expense fund_sources
        :param reimbursable: True for reimbursable expenses, False for non reimbursable expenses
        :param spent_at: Extract expenses in spent_at date range
        :param report_ids: List of report_ids
        :return: List of expense ids
        """

        self.logger.info('Extracting expenses from Fyle.')

        expenses = self.__connection.Expenses.get_all(
            settlement_id=settlement_ids,
            state=state,
            updated_at=updated_at,
            fund_source=fund_source,
            exported=exported,
            spent_at=spent_at,
            report_id=report_ids
        )

        if reimbursable is not None:
            expenses = list(filter(lambda expense: expense['reimbursable'], expenses))

        self.logger.info('%s expenses extracted.', str(len(expenses)))

        if expenses:
            df_expenses = pd.DataFrame(expenses)

            df_expenses['approved_by'] = df_expenses['approved_by'].map(lambda expense: expense[0] if expense else None)

            df_expenses = df_expenses[[
                'id', 'employee_id', 'employee_email', 'employee_code', 'spent_at', 'currency',
                'amount', 'foreign_currency', 'foreign_amount', 'purpose', 'project_id', 'project_name',
                'cost_center_id', 'cost_center_name', 'category_id', 'category_code', 'category_name',
                'sub_category', 'settlement_id', 'expense_number', 'claim_number', 'trip_request_id',
                'state', 'report_id', 'fund_source', 'reimbursable', 'created_at', 'updated_at',
                'approved_at', 'settled_at', 'verified', 'verified_at', 'reimbursed_at', 'added_to_report_at',
                'report_submitted_at', 'vendor', 'has_attachments', 'billable', 'exported',
                'approved_by', 'org_id', 'org_name', 'created_by'
            ]]

            df_expenses.to_sql('fyle_extract_expenses', self.__dbconn, if_exists='append', index=False)

            custom_properties = []
            for e in expenses:
                if 'custom_properties' in e and e['custom_properties']:
                    for cp in e['custom_properties']:
                        custom_properties.append({
                            'expense_id': e['id'],
                            'name': cp['name'],
                            'value': cp['value']
                        })

            if extract_custom_fields:
                if custom_properties:
                    df_custom_properties = pd.DataFrame(custom_properties)
                    df_custom_properties.to_sql('fyle_extract_expense_custom_properties', self.__dbconn,
                                                if_exists='append', index=False)

            return df_expenses['id'].to_list()

        return []

    def extract_corporate_credit_card_expenses(self, settlement_ids: List[str] = None, state: List[str] = None,
                                               reimbursement_state: List[str] = None, transaction_type: str = None,
                                               updated_at: List[str] = None, spent_at: List[str] = None,
                                               exported: bool = None, personal: bool = None) -> List[str]:
        """
        Extract corporate credit card expenses from fyle.
        :param settlement_ids: List of settlement_ids
        :param state: state of corporate credit card expense INITIALIZED / IN_PROGRESS / SETTLED
        :param reimbursement_state: state of reimbursement PENDING / COMPLETE
        :param transaction_type: DEBIT / CREDIT
        :param updated_at: Extract expenses in updated_at date range
        :param spent_at: Extract expenses in spent_at date range
        :param exported: True for exported expenses and False for unexported expenses
        :param personal: True for personal expenses and False for company expenses
        :return:
        """

        self.logger.info('Extracting corporate credit card expenses from Fyle.')

        ccc_expenses = self.__connection.CorporateCreditCardExpenses.get_all(
            settlement_id=settlement_ids,
            state=state,
            reimbursement_state=reimbursement_state,
            transaction_type=transaction_type,
            updated_at=updated_at,
            spent_at=spent_at,
            exported=exported,
            personal=personal
        )

        self.logger.info('%s expenses extracted.', str(len(ccc_expenses)))

        if ccc_expenses:
            df_ccc_expenses = pd.DataFrame(ccc_expenses)

            df_ccc_expenses = df_ccc_expenses[[
                'id', 'employee_email', 'org_user_id', 'org_id', 'org_name', 'created_at', 'updated_at', 'spent_at',
                'amount', 'currency', 'foreign_amount', 'foreign_currency', 'vendor', 'description', 'settlement_id',
                'corporate_credit_card_account_number', 'personal', 'expense_id', 'reimbursement_state', 'state',
                'transaction_type', 'exported', 'exported_at'
            ]]

            df_ccc_expenses.to_sql('fyle_extract_corporate_credit_card_expenses', self.__dbconn, if_exists='append',
                                   index=False)

            return df_ccc_expenses['id'].to_list()

        return []

    def extract_attachments(self, expense_ids: List[str]) -> List[str]:
        """
        Extract attachments from Fyle
        :param expense_ids: List of Expense Ids
        :return: List of expense ids for which attachments were downloaded
        """
        attachments = []

        self.logger.info('Extracting attachments from Fyle')

        if expense_ids:
            for expense_id in expense_ids:
                attachment = self.__connection.Expenses.get_attachments(expense_id)
                if attachment['data']:
                    attachment = attachment['data'][0]
                    attachment['expense_id'] = expense_id
                    attachments.append(attachment)

            self.logger.info('%s attachments extracted.', str(len(attachments)))

            if attachments:
                df_attachments = pd.DataFrame(attachments)
                df_attachments.to_sql('fyle_extract_attachments', self.__dbconn, if_exists='append', index=False)
                return df_attachments['expense_id'].to_list()

        self.logger.info('0 attachments extracted.')
        return []

    def extract_categories(self) -> List[str]:
        """
        Extract categories from Fyle
        :return: List of category ids
        """
        self.logger.info('Extracting categories from Fyle.')

        categories = self.__connection.Categories.get()['data']

        self.logger.info('%s categories extracted.', str(len(categories)))

        if categories:
            df_categories = pd.DataFrame(categories)

            df_categories = df_categories[[
                'id', 'name', 'code', 'enabled', 'fyle_category', 'sub_category',
                'created_at', 'updated_at', 'org_id', 'org_name'
            ]]

            df_categories.to_sql('fyle_extract_categories', self.__dbconn, if_exists='append', index=False)
            return df_categories['id'].to_list()

        return []

    def extract_projects(self) -> List[str]:
        """
        Extract projects from Fyle
        :return: List of project ids
        """
        self.logger.info('Extracting projects from Fyle.')

        projects = self.__connection.Projects.get()['data']

        self.logger.info('%s projects extracted.', str(len(projects)))

        if projects:
            df_projects = pd.DataFrame(projects)
            df_projects = df_projects[[
                'id', 'name', 'description', 'active', 'approver1_employee_id',
                'approver1_employee_email', 'approver1_employee_code',
                'approver2_employee_id', 'approver2_employee_email',
                'approver2_employee_code', 'org_id', 'code', 'org_name'
            ]]

            df_projects.to_sql('fyle_extract_projects', self.__dbconn, if_exists='append', index=False)
            return df_projects['id'].to_list()

        return []

    def extract_cost_centers(self) -> List[str]:
        """
        Extract cost centers from Fyle
        :return: List of cost center ids
        """
        self.logger.info('Extracting cost centers from Fyle.')

        cost_centers = self.__connection.CostCenters.get(False)['data']

        self.logger.info('%s cost centers extracted.', str(len(cost_centers)))

        if cost_centers:
            df_cost_centers = pd.DataFrame(cost_centers)
            df_cost_centers = df_cost_centers[['id', 'name', 'description', 'code', 'active', 'org_id', 'org_name']]

            df_cost_centers.to_sql('fyle_extract_cost_centers', self.__dbconn, if_exists='append', index=False)
            return df_cost_centers['id'].to_list()

        return []

    def extract_reimbursements(self, state: List[str] = None, updated_at: List[str] = None,
                               exported: bool = None) -> List[str]:
        """
        Extract reimbursements from Fyle
        :param updated_at: Extract expenses within a date range.
        :param state: List of states
        :param exported: True for exported reimbursements and False for unexeported reimbursements
        :return: List of reimbursement ids
        """
        self.logger.info('Extracting reimbursements from Fyle.')
        reimbursements = self.__connection.Reimbursements.get_all(
            updated_at=updated_at,
            exported=exported
        )

        if state:
            reimbursements = list(filter(
                lambda reimbursement: reimbursement['state'] in state,
                reimbursements
            ))

        self.logger.info('%s reimbursements extracted.', str(len(reimbursements)))

        if reimbursements:
            df_reimbursements = pd.DataFrame(reimbursements)

            df_reimbursements = df_reimbursements[[
                'id', 'created_at', 'updated_at', 'employee_id', 'employee_email',
                'employee_code', 'org_id', 'org_name', 'currency', 'amount', 'state',
                'report_ids', 'unique_id', 'purpose', 'settlement_id', 'exported'
            ]]

            df_reimbursements.to_sql('fyle_extract_reimbursements', self.__dbconn, if_exists='append', index=False)
            return df_reimbursements['id'].to_list()

        return []

    def extract_advances(self, settlement_ids: List[str] = None) -> List[str]:
        """
        Extract advances from Fyle
        :param settlement_ids: List of settlement ids
        :return: List of advance ids
        """
        self.logger.info('Extracting advances from Fyle.')
        advances = self.__connection.Advances.get_all(
            settlement_id=settlement_ids
        )

        self.logger.info('%s advances extracted.', str(len(advances)))

        if advances:
            df_advances = pd.DataFrame(advances)

            df_advances = df_advances[[
                'id', 'created_at', 'updated_at', 'employee_id', 'employee_email',
                'employee_code', 'project_id', 'project_name', 'currency', 'amount',
                'purpose', 'issued_at', 'payment_mode', 'original_currency',
                'original_amount', 'reference', 'settlement_id', 'trip_request_id',
                'advance_number', 'advance_request_id', 'settled_at', 'created_by',
                'exported', 'org_id', 'org_name'
            ]]

            df_advances.to_sql('fyle_extract_advances', self.__dbconn, if_exists='append', index=False)
            return df_advances['id'].to_list()

        return []

    def extract_advance_requests(self, state: List[str] = None, updated_at: List[str] = None,
                                 exported: bool = None) -> List[str]:
        """
        Extract advance requests from Fyle
        :param state:
        :param updated_at:
        :param exported:
        :return: List of advance request ids
        """
        self.logger.info('Extracting advance requests from Fyle.')

        advance_requests = self.__connection.AdvanceRequests.get_all(
            state=state,
            updated_at=updated_at,
            exported=exported
        )

        self.logger.info('%s advance requests extracted.', str(len(advance_requests)))

        if advance_requests:
            df_advance_requests = pd.DataFrame(advance_requests)

            if len(df_advance_requests['custom_field_values'].index):
                advance_request_custom_fields = []

                for row in df_advance_requests.to_dict(orient='records'):
                    custom_field = {}
                    custom_fields = row['custom_field_values']
                    custom_field['advance_request_id'] = row['id']

                    if custom_fields:
                        for field in custom_fields:
                            custom_field[field['name']] = field['value']

                        advance_request_custom_fields.append(custom_field)

                df_advance_requests_custom_fields = pd.DataFrame(advance_request_custom_fields)
                df_advance_requests_custom_fields.to_sql(
                    'fyle_extract_advance_request_custom_fields',
                    self.__dbconn,
                    if_exists='replace',
                    index=False
                )

            df_advance_requests = df_advance_requests[[
                'updated_at', 'created_at', 'approved_at', 'id', 'purpose', 'notes',
                'state', 'currency', 'amount', 'advance_id', 'advance_request_number',
                'trip_request_id', 'project_id', 'source', 'is_sent_back', 'is_pulled_back',
                'org_id', 'org_name', 'employee_email', 'employee_name', 'employee_id',
                'exported'
            ]]

            df_advance_requests.to_sql('fyle_extract_advance_requests', self.__dbconn, if_exists='append', index=False)
            return df_advance_requests['id'].to_list()

        return []

    def extract_reports(self, updated_at: List[str] = None, exported: bool = None) -> List[str]:
        """
        Extract reports from Fyle
        :param updated_at: Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
        :param exported: True for exported reports and False for unexported reports
        :return: List of report ids
        """
        self.logger.info('Extracting reports from Fyle.')

        reports = self.__connection.Reports.get_all(
            updated_at=updated_at,
            exported=exported
        )

        self.logger.info('%s reports extracted.', str(len(reports)))

        if reports:
            df_reports = pd.DataFrame(reports)

            df_reports['approved_by'] = df_reports['approved_by'].map(lambda report: report[0] if report else None)

            df_reports = df_reports[[
                'id', 'employee_id', 'employee_email', 'employee_code', 'state',
                'amount', 'purpose', 'claim_number', 'created_at', 'updated_at', 'approved_at',
                'reimbursed_at', 'trip_request_id', 'settlement_id', 'org_id', 'org_name', "verified",
                "exported", "approved_by", "created_by", "settled_at"
            ]]

            df_reports.to_sql('fyle_extract_reports', self.__dbconn, if_exists='append', index=False)
            return df_reports['id'].to_list()

        return []
