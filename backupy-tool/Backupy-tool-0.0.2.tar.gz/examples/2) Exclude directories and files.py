from Backupy import Backupy

backup = Backupy()
backup.add_directory(
    directory='/var/www/html/assets/',
    exclude={
        'images',
        'fonts/images',
        '*/sass/*m*.sass',
        'logs/log.txt'
    }
)
backup.start()
