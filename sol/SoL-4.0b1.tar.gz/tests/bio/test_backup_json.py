# -*- coding: utf-8 -*-
# :Project:   SoL -- Backup tests
# :Created:   sab 07 lug 2018 12:38:57 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2018 Lele Gaifax
#

from test_backup import full_backup_restore


def test_full_backup_restore_json(session, tmpdir):
    full_backup_restore(session, tmpdir, 'json')
