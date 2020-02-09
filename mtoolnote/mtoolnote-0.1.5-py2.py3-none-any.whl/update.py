#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import pandas as pd
from pkg_resources import resource_filename
from sqlalchemy import create_engine
from .models import Base


# @main.command()
def create_db():
    _dbfile = resource_filename(__name__, "data/hmtvar.db")
    engine = create_engine(f"sqlite:///{_dbfile}")

    click.echo(f"Creating {_dbfile}... ", nl=False)
    Base.metadata.create_all(bind=engine)
    click.echo("Done.")


# @main.command()
def update_db():
    _dbfile = resource_filename(__name__, "data/hmtvar.db")
    # _dbtables = resource_dir(__name__, "data/tables")
    engine = create_engine(f"sqlite:///{_dbfile}")

    click.echo("Updating database tables... ")
    sources = ("Main", "CrossRef", "FuncLoci", "Loci", "Plasmy", "Predict",
               "Variab")
    for el in sources:
        _tablefile = resource_filename(__name__, f"data/tables/{el}.csv")
        click.echo(f"\tUpdating {el} table... ", nl=False)
        df = pd.read_csv(_tablefile, na_values="<null>")
        df.reset_index(inplace=True)
        df.rename(columns={"index": "id"}, inplace=True)
        with engine.connect() as conn:
            df.to_sql(name=el, con=conn, index=False, if_exists="replace", index_label="id")
        click.echo("Complete.")

    haplos = (
    "Haplo_A", "Haplo_B", "Haplo_D", "Haplo_G", "Haplo_JT", "Haplo_L0", "Haplo_L1", "Haplo_L2",
    "Haplo_L3_star", "Haplo_L4", "Haplo_L5", "Haplo_L6", "Haplo_M7", "Haplo_M8", "Haplo_M9",
    "Haplo_M_star", "Haplo_N1", "Haplo_N2", "Haplo_N9", "Haplo_N_star", "Haplo_R0", "Haplo_R9",
    "Haplo_R_star", "Haplo_U", "Haplo_X")
    for el in haplos:
        _tablefile = resource_filename(__name__, f"data/tables/{el}.csv")
        click.echo(f"\tUpdating {el} table... ", nl=False)
        df = pd.read_csv(_tablefile, na_values="<null>",
                         names=["position", "freq_A", "freq_C", "freq_G", "freq_T", "freq_gap",
                                "freq_oth"], skiprows=1)
        df.reset_index(inplace=True)
        df.rename(columns={"index": "id"}, inplace=True)
        with engine.connect() as conn:
            df.to_sql(name=el, con=conn, index=False, if_exists="replace", index_label="id")
        click.echo("Complete.")

    click.echo("Done.")
