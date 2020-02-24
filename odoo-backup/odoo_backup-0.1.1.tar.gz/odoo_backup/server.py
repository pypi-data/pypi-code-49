from flask import Flask, send_from_directory
from config import DATA_DIR
import os
from utils import backup_datetime_from_name


def create_server(server_name:str, database: str, file_name: str) -> Flask:
    app = Flask('download_server')

    @app.route('/')
    def download_backup():
        print('downloading', file_name)
        return send_from_directory(
            os.path.join(DATA_DIR, server_name, database),
            file_name,
            as_attachment=True,
            attachment_filename=f'{server_name} - {database} - {backup_datetime_from_name(file_name).date().isoformat()}.zip',
            cache_timeout=0,
        )

    return app
