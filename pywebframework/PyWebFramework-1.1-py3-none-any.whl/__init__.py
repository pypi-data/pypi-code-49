# coding: utf-8

from .core.module import ModuleBase
from .core.task import TaskBase
from .core.page import PageBase
from .core.exception import FailureException, SuccessException
from .core.error import *
from .core.settings import settings
from pyWebFramework.tax_init.TaskTaxInitBase import TaskTaxInitBase
from pyWebFramework.tax_init.PageTaxInitFormBase import PageTaxInitFormBase
from pyWebFramework.tax_init.TaskTaxInitBase import pdf_to_xlsx
from pyWebFramework.dll.IeWebFramework import Download, DownloadWithParam, GetCookie
from pyWebFramework.dll.IeWebFramework import GetOcrCode
from pyWebFramework.dll.IeWebFramework import ErrorCode
from pyWebFramework.dll.IeWebFramework import RunJsException
from pyWebFramework.dll.IeWebFramework import IeCore
from pyWebFramework.dll.IeWebFramework import TaxInitApi, SmsApi

from pyWebFramework.dll.IeWebFramework import test
