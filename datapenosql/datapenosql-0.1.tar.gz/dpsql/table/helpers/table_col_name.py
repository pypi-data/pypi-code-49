from dpsql.table.model.db_objects import QueryTable, Column


def query_table(table_obj: QueryTable = None) -> str:
    """
    Add selected attribs to the sql query w/o aliases.

    Takes a Column object as as input and inspects if it contains an alias
    or not, added to that it checks if it's a general column for the query or
    it's related to a specific table w/o table alias

    Parameters
    ----------
    table_obj : QueryTable, optional
        QueryTable object that the Column is related to if existed.
        The default is None.

    Returns
    -------
    str
        column strings to be added to select query by the builder.

    """
    if table_obj.alias_ != "":
        table_name = table_obj.alias_ 
    else:
        table_name = table_obj.name_

    return f'{table_name}'


def query_attrib(attrib_obj: Column, table_obj: QueryTable = None) -> str:
    """
    Add selected attribs to the sql query w/o aliases.

    Takes a Column object as as input and inspects if it contains an alias
    or not, added to that it checks if it's a general column for the query or
    it's related to a specific table w/o table alias

    Parameters
    ----------
    attrib_obj : Column
        Column to create select query upon.
        
    table_obj : QueryTable, optional
        QueryTable object that the Column is related to if existed.
        The default is None.

    Returns
    -------
    str
        column strings to be added to select query by the builder.

    """
    if table_obj is None:
        return query_attrib_set_alias(attrib_obj)
    else:
        table_alias = table_obj.alias_ if table_obj.alias_ != "" else ""
        table_name = table_obj.name_
        attrib_name = query_attrib_set_alias(attrib_obj)
        if table_alias != "":
            return f'{table_alias}.{attrib_name}'
        else:
            return f'{table_name}.{attrib_name}'


def query_table_set_alias(table_obj: QueryTable) -> str:
    """
    Add selected tables to the sql query w/o aliases.
    
    Takes a table object as an input and inspects if it contains an alias 
    or not and creates the desired representation accordingly.
    
    Parameters
    ----------
    table_obj : QueryTable
        Table to create select query from.
        
    Returns
    -------
    string
        String representation of the table to be used in the generated Query
    """
    table_alias = table_obj.alias_ if table_obj.alias_ != "" else ""
    table_name = table_obj.name_
    if table_alias != "":
        return f'{table_name} {table_alias}'
    else:
        return table_name


def query_attrib_set_alias(attrib_obj: Column) -> str:
    attrib_alias = attrib_obj.alias_ if attrib_obj.alias_ != "" else ""
    attrib_name = attrib_obj.name_
    if attrib_alias != "":
        return f'{attrib_name} AS {attrib_alias}'
    else:
        return attrib_name
