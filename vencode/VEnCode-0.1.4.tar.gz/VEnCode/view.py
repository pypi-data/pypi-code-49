#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
view.py: Objects that build from the main VEnCode project objects, comprising many of those objects
together in a functional way.
"""


import os
import sys

import pandas as pd
import sqlite3

import VEnCode.utils.sqlite_utils as sq
import VEnCode.utils.dir_and_file_handling as directory_handlers

# TODO: A class that inputs one or several VEnCodes and has functions to view several VEnCodes, or to output a file.


class VencodeContainer:
    def __init__(self, vencodes):
        conn = sq.create_connection_memory()

        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS data (
                                                id integer PRIMARY KEY,
                                                Algorithm text NOT NULL,
                                                Number_of_RE integer,
                                                end_date text
                                            ); """

        sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS vencodes (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            priority integer,
                                            status_id integer NOT NULL,
                                            project_id integer NOT NULL,
                                            begin_date text NOT NULL,
                                            end_date text NOT NULL,
                                            FOREIGN KEY (project_id) REFERENCES projects (id)
                                        );"""
        sq.create_table(conn, sql_create_projects_table)
        sq.create_table(conn, sql_create_tasks_table)
        with conn:
            # create a new project
            project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
            project_id = sq.create_project(conn, project)

            # tasks
            task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
            task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

            # create tasks
            sq.create_task(conn, task_1)
            sq.create_task(conn, task_2)
        c = conn.cursor()
        c.execute("SELECT * FROM data WHERE id=1")
        rows = c.fetchall()

        if not isinstance(vencodes, list):
            vencodes = [vencodes]
        for vencode in vencodes:
            pass
        conn.close()

if __name__== "__main__":
    a = VencodeContainer("A")
    print(a)