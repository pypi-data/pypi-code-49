"DB API Exceptions"

import re
import functools
import teradatasql

class BaseException(Exception):
	def __init__(self, sqlcode, sqltext, version=None, component=None, session=None, orig_text=None):
		super().__init__()
		self.sqlcode, self.sqltext, self.version, self.component, self.session, self.orig_text = sqlcode, sqltext, version, component, session, orig_text

	def __str__(self):
		if self.sqlcode is None:
			return self.sqltext
		return f'[{self.sqlcode}] {self.sqltext}'

class Warning(BaseException): pass
class Error(BaseException): pass
class InterfaceError(Error): pass
class DatabaseError(Error): pass
class DataError(DatabaseError): pass
class OperationalError(DatabaseError): pass
class IntegrityError(DatabaseError): pass
class NotSupportedError(DatabaseError): pass
class InternalError(DatabaseError): pass
class ProgrammingError(DatabaseError): pass

def fix_excp(fn):
	"Wrapper that fixes DB API exceptions raised during a function call"

	@functools.wraps(fn)
	def wrapper(*args, **kwargs):
		try:
			_err = None
			return fn(*args, **kwargs)
		except teradatasql.OperationalError as _oe:
			_err = _oe

		err_text = str(_err).split('\n')[0]
		m = re.match(r'\[Version (.*?)\] \[Session (\d+)\] \[(.*?)\] (?:\[Error (\d+)\] )?(.*)', err_text)
		if not m:
			raise _err

		version, session, component, sqlcode, sqltext = m.groups()
		if session:
			session = int(session)
		if sqlcode:
			sqlcode = int(sqlcode)
		err_class = InterfaceError if component == 'Teradata SQL Driver' else error2ex.get(sqlcode, ProgrammingError)

		raise err_class(sqlcode, sqltext, version=version, component=component, session=session, orig_text=err_text)

	return wrapper

# map commonly encountered errors to exception.
# Note: This list is NOT exhaustive
error2ex = {
	2616: DataError,          # Numeric overflow occurred during computation.
	2617: DataError,          # Overflow occurred computing an expression involving VT_VOTES.VOTE_KEY
	2618: DataError,          # Invalid calculation:  division by zero.
	2620: DataError,          # The format or data contains a bad character.
	2621: DataError,          # Bad character in format or data of TMP_FINAL_ALLOCATION_AVAILABLE_INVENTORY_FACT3.EDA_SYSCODE.
	2631: OperationalError,   # Transaction ABORTed due to deadlock.
	2636: NotSupportedError,  # %TBL must be empty for Fast Loading.
	2640: ProgrammingError,   # Specified table does not exist in %DB.
	2641: InternalError,      # %SP:%TBL was restructured.  Resubmit.
	2644: OperationalError,   # No more room in database %DB.
	2646: OperationalError,   # %SP:No more spool space in %DB.
	2652: OperationalError,   # Operation not allowed: %TBL is being Loaded.
	2662: OperationalError,   # SUBSTR: string subscript out of bounds.
	2663: OperationalError,   # SUBSTR: string subscript out of bounds in %TBL.
	2665: DataError,          # Invalid date.
	2666: DataError,          # Invalid date supplied for X_BREAK_ITEM_EC.ULTIMEDATE.
	2801: IntegrityError,     # %TBL Duplicate unique prime key error in %TBL.
	2803: IntegrityError,     # Secondary index uniqueness violation in %TBL
	2893: DataError,
	3110: OperationalError,   # The transaction was aborted by the user.
	3134: OperationalError,   # The request was aborted by an ABORT SESSION command.
	3149: Warning,            # Warning, For Rule Name 'Warn Adhoc users'
	3151: OperationalError,   # TDWM Throttle violation for Concurrent Queries: %RULE
	3158: Warning,            # Warning, For Rule Name 'Warn Adhoc users'
	3504: ProgrammingError,   # Selected non-aggregate values must be part of the associated group.
	3510: ProgrammingError,   # Too many END TRANSACTION statements.
	3514: OperationalError,   # User-generated transaction ABORT.
	3515: ProgrammingError,   # Duplication of column ZIP_KEY in a table, derived table, view, macro or trigger.
	3518: NotSupportedError,  # Too many columns in a composite index.
	3523: OperationalError,   # The user does not have STATISTICS WITH GRANT OPTION access to %TBL.
	3524: OperationalError,   # The user does not have STATISTICS WITH GRANT OPTION access to database %DB.
	3526: ProgrammingError,   # The specified index does not exist.
	3527: DataError,          # Format string '%FMT' has combination of  numeric, character  and GRAPHIC values.
	3530: DataError,          # Invalid FORMAT string '%FMT'.
	3532: NotSupportedError,  # Conversion between BYTE data and other types is illegal.
	3535: DataError,          # A character string failed conversion to a numeric value.
	3541: ProgrammingError,   # The request to assign new PERMANENT space is invalid.
	3544: ProgrammingError,   # Partial string matching requires character operands.
	3557: NotSupportedError,  # Column %COL is an index column and cannot be dropped.
	3558: NotSupportedError,
	3568: ProgrammingError,   # Cannot nest aggregate operations.
	3569: ProgrammingError,   # Improper use of an aggregate function in a WHERE Clause.
	3574: ProgrammingError,   # Illegal clause or aggregation in a SELECT with no table accessed.
	3585: ProgrammingError,   # USING modifier NOT allowed with DDL.
	3604: IntegrityError,     # Cannot place a null value in a NOT NULL field.
	3607: ProgrammingError,   # Too many expressions in the select list of a subquery.
	3617: ProgrammingError,   # FORMAT 'YYYYMMDD' does not match the datatype.
	3623: NotSupportedError,  # The user cannot use COMPRESS on a primary index column or partitioning expression column.
	3624: Warning,            # There are no statistics defined for the table.
	3625: ProgrammingError,   # GROUP BY and WITH...BY clauses may not contain aggregate functions.
	3631: NotSupportedError,
	3637: ProgrammingError,   # Invalid ORDER BY constant.
	3640: ProgrammingError,   # Comparing BYTE data in column hashvalue with other types is illegal.
	3653: ProgrammingError,   # All select-lists do not contain the same number of expressions.
	3654: ProgrammingError,   # Corresponding select-list expressions are incompatible.
	3662: ProgrammingError,   # Concatenation between BYTE data and other types is illegal.
	3669: OperationalError,   # More than one value was returned by a subquery.
	3704: ProgrammingError,   # %TOK is not a valid Teradata SQL token.
	3706: ProgrammingError,   # Syntax error: UNIQUE Column(s) must be NOT NULL.
	3707: ProgrammingError,   # Syntax error, expected something like an integer or a decimal number or a floating point number...
	3710: InternalError,      # Insufficient memory to parse this request, during queryrewrite phase.
	3722: NotSupportedError,  # Only a COMMIT WORK or null statement is legal after a DDL Statement.
	3731: ProgrammingError,   # The user must use IS NULL or IS NOT NULL to test for NULL values.
	3732: NotSupportedError,
	3733: ProgrammingError,   # The SELECT has more than one WHERE clause.
	3739: ProgrammingError,   # The user must give a data type for %COL.
	3751: ProgrammingError,   # Expected a digit for the exponent.
	3754: ProgrammingError,   # Precision error in FLOAT type constant or during implicit conversions.
	3760: ProgrammingError,   # String not terminated before end of text.
	3771: ProgrammingError,   # Illegal expression in WHEN clause of CASE expression.
	3775: ProgrammingError,   # Invalid hexadecimal constant.
	3776: ProgrammingError,   # Comment not terminated before end of request text.
	3778: ProgrammingError,   # SELECT statement must follow LOCK ROW modifier.
	3779: ProgrammingError,   # Fractional digits must be between 0 and total digit number.
	3781: ProgrammingError,   # No aggregate operation allowed in the search condition for a joined table.
	3782: ProgrammingError,   # Improper column reference in the search condition of a joined table.
	3784: ProgrammingError,   # The number of digits specified must be between 1 and 38.
	3785: ProgrammingError,   # Expected ANY or ALL is missing.
	3798: ProgrammingError,   # A column or character expression is larger than the max size.
	3800: ProgrammingError,   # Datatype Mismatch in THEN/ELSE expression.
	3802: ProgrammingError,   # Database '%DB' does not exist.
	3803: ProgrammingError,   # Table '%TBL' already exists.
	3806: ProgrammingError,   # Table/view/trigger name '%TBL' is ambiguous.
	3807: ProgrammingError,   # %SP:Object '%TBL' does not exist.
	3808: ProgrammingError,   # Database unspecified for '%TBL'.
	3809: ProgrammingError,   # Column '%FOL' is ambiguous.
	3810: InternalError,      # No error text is available
	3811: ProgrammingError,   # Column '%COL' is NOT NULL.  Give the column a value.
	3812: ProgrammingError,   # The positional assignment list has too few values.
	3813: ProgrammingError,   # The positional assignment list has too many values.
	3822: ProgrammingError,   # Cannot resolve column '%COL'. Specify table or view.
	3823: ProgrammingError,   # VIEW '%VIEW' may not be used for Help Index/Constraint/Statistics, Update, Delete or Insert.
	3824: ProgrammingError,   # Macro '%MACRO' does not exist.
	3848: ProgrammingError,   # The ORDER BY clause must contain only integer constants.
	3849: ProgrammingError,   # The ORDER BY clause does not follow the last SELECT.
	3853: InternalError,      # No error text is available
	3854: ProgrammingError,   # '%TBL' is not a view.
	3855: ProgrammingError,   # '%MACRO' is not a macro.
	3861: ProgrammingError,   # Follow table '%TBL' with '.*' or '.columnname'.
	3863: ProgrammingError,   # Duplicate definition of '%TEXT' in NAMED phrase.
	3868: ProgrammingError,   # A table or view without alias appears more than once in FROM clause.
	3870: ProgrammingError,   # Alias name cannot match another table/alias name in FROM clause.
	3883: ProgrammingError,   # Invalid GROUP BY constant.
	3888: ProgrammingError,   # A SELECT for a UNION,INTERSECT or MINUS must reference a table.
	3932: ProgrammingError,   # Only an ET or null statement is legal after a DDL Statement.
	3933: NotSupportedError,  # The Maximum Possible Row Length in the Table is too Large.
	3939: ProgrammingError,   # There is a mismatch between the number of parameters specified and the number of parameters required.
	3990: ProgrammingError,   # Table %TBL is not specified in the FROM clause or already aliased by another name.
	3996: DataError,          # Right truncation of string data.
	5315: OperationalError,   # The user does not have %ACC access to %TBL.
	5325: ProgrammingError,   # Length 0 is not allowed for a CHAR, VARCHAR, BYTE, VARBYTE column.
	5326: ProgrammingError,   # Operand of %FUNC function is not a valid data type or value.
	5327: ProgrammingError,   # %FUNC has been called with wrong data types or values.
	5333: ProgrammingError,   # NO LOG keywords not allowed for permanent table.
	5337: OperationalError,   # Drop Table is not allowed due to materialized temporary tables.
	5340: NotSupportedError,  # Database name, if specified, must be the login user name for a volatile table.
	5355: ProgrammingError,   # The arguments of the CAST function must be of the same character data type.
	5381: ProgrammingError,   # Duplicate column names as result of rename column request.
	5399: ProgrammingError,   # Bad argument type to UPPER or LOWER function.
	5400: ProgrammingError,   # Number of leading digits out of range.
	5401: ProgrammingError,   # Number of fractional digits out of range.
	5404: DataError,          # Datetime field overflow.
	5407: DataError,          # Invalid operation for DateTime or Interval.
	5408: ProgrammingError,   # Invalid operands to %FUNC operator.
	5464: ProgrammingError,   # Error in Join Index DDL, ...
	5466: ProgrammingError,   # Error in Secondary Index DDL, Order by field does not belong to the index.
	5467: ProgrammingError,   # Cannot drop, MLOAD, or RESTORE a table with join or hash indexes.
	5475: ProgrammingError,   # SAMPLE clause not allowed in SET operations.
	5478: ProgrammingError,   # Aggregates are allowed only with Window Functions.
	5479: ProgrammingError,   # Ordered Analytical Functions not allowed in WHERE Clause.
	5480: ProgrammingError,   # Ordered Analytical Functions can not be nested.
	5481: ProgrammingError,   # Ordered Analytical Functions not allowed in GROUP BY Clause.
	5486: ProgrammingError,   # Window size value is not acceptable.
	5488: ProgrammingError,   # SampleId not permitted in GROUP BY Clause.
	5494: ProgrammingError,   # '%TOK' is not a stored procedure.
	5495: ProgrammingError,   # Stored Procedure  '%TOK' does not exist.
	5506: ProgrammingError,   # Column names must be specified when SELECT list contains an unnamed expression.
	5510: OperationalError,
	5531: ProgrammingError,   # Named-list is not supported for arguments of a procedure.
	5542: ProgrammingError,   # Only Select, Insert, Delete or Update statements can be captured.
	5587: ProgrammingError,   # Reference to function 'TIMESTAMPPLUSSECONDS' is not allowed in this context.
	5595: ProgrammingError,   # The privilege is not applicable to a function.
	5612: ProgrammingError,   # A user, database, role, or zone with the specified name already exists.
	5616: ProgrammingError,   # The user is not authorized to grant or revoke role '%ROLE'.
	5623: ProgrammingError,   # User or role '%USER' does not exist.
	5628: ProgrammingError,   # %SP:Column %COL not found in %TBL.
	5653: ProgrammingError,   # Profile '%PROFILE' does not exist.
	5660: ProgrammingError,   # Cannot create index on LOB columns.
	5704: ProgrammingError,   # Cannot BEGIN QUERY LOGGING due to existing rule. Use REPLACE QUERY LOGGING
	5728: IntegrityError,     # Partitioning violation for table %TBL.
	5788: NotSupportedError,
	5876: ProgrammingError,   # Ordered Analytical Functions not allowed in HAVING Clause.
	5878: InternalError,      # No error text is available
	5879: ProgrammingError,   # Invalid Partition field.
	5882: ProgrammingError,   # Invalid SET statement in the triggered action.
	5967: OperationalError,   # The table being dropped has an error table.
	5979: ProgrammingError,   # An error table may be defined for a permanent data table only.
	6706: DataError,          # The string contains an untranslatable character.
	6724: ProgrammingError,   # The object name is too long in NFD/NFC.
	6725: ProgrammingError,   # Object name contains restricted characters.
	6758: ProgrammingError,   # Invalid time.
	6760: ProgrammingError,   # Invalid timestamp.
	6916: ProgrammingError,   # TOP N Syntax error: Top N option is not supported with SAMPLE clause.
	6926: ProgrammingError,   # WITH [RECURSIVE] clause or recursive view is not supported within WITH...
	6956: NotSupportedError,  # Column MKT_KEY has statistics and cannot be dropped or modified.
	6973: ProgrammingError,   # Invalid argument for the BEGIN function. The argument must have a Period data type.
	7453: DataError,          # Interval field overflow.
	7454: DataError,          # DateTime field overflow.
	7487: InternalError,      # %TOK:AMP step failure: Please do not resubmit the last request.
	7504: InternalError,      # in UDF/XSP/UDM SYSLIB.MonitorSQLText: SQLSTATE U0004: MSG3296-PM/PC command processing timed out.
	7547: OperationalError,   # Target row updated by multiple source rows.
	7548: DataError,          # %SP:Invalid JSON data: %MSG.
	7827: NotSupportedError,  # Java SQL Exception SQLSTATE 39001: Invalid SQL state %MSG.
	7828: OperationalError,   # Unexpected Java Exception SQLSTATE 38000: An org.json.JSONException %MSG exception was thrown.
	7972: ProgrammingError,   # Jar '%JAR' does not exist.
	9103: ProgrammingError,   # Invalid Period value constructor. The beginning bound must be less than the ending bound.
	9107: NotSupportedError,
	9134: ProgrammingError,   # YYYY value must be four digits and in the range 1-9999
	9302: ProgrammingError,   # Specified expression for an EXPAND ON clause does not have a PERIOD data type.
	9303: ProgrammingError,   # EXPAND ON clause must not be specified in a query expression with no table references.
	9307: ProgrammingError,   # Invalid use of the expanded column name.
	9473: ProgrammingError,   # Column Partitioning with a Primary AMP Index or a Primary Index has not yet been enabled.
	9563: InternalError,      # Insufficient memory to construct the XML for this request.
	9804: InternalError,      # Response Row size or Constant Row size overflow.
	9881: ProgrammingError,   # Function '%FUNC' called with an invalid number or type of parameters
}
