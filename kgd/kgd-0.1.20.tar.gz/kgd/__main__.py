import sys
from collections import deque
from os.path import basename

from box import Box
from tqdm import tqdm

import kgd.constants as cnst

from kgd.cli import parse_args
from kgd.common import ParseFilesManager
from kgd.api import KgdTaxPaymentParser
from kgd.utils import is_server_up


def print_loading():
    print('There could be parsed BINs.')
    print('It may take some time. Building list ...')


def print_status_map():
    print('> rqe - count of BINs we got KGD API error with. Those BINs are not supposed to be reprocessed.')
    print('> rse - count of occurrences when we got bad response(KGD requests count limitation, ')
    print('html or some other trash not xml formatted). Those BINs are supposed to be reprocessed.')
    print('> se - count of occurrences when we failed(connection, network, 500, etc ). ')
    print(' Those BINs are supposed to be reprocessed. ')
    print('> s - count of BINs we successfully processed')
    print('> R - indicates reprocessing')
    print('>> All these indicators are actual for only this launch!')


def main():
    args = parse_args()
    p = Box(vars(args))

    if not is_server_up(KgdTaxPaymentParser.host):
        print('Address is unreachable. Exiting...')
        sys.exit()

    fm = ParseFilesManager(p.fpath)
    parser = KgdTaxPaymentParser(p.token, p.timeout)

    print_loading()
    bins = deque(fm.load_ids())

    print_status_map()
    with tqdm(total=fm.all_count) as pbar:
        pbar.update(fm.prs_count)

        while bins:
            incr = 1
            r = False

            if parser.failed:
                _bin = parser.failed.popleft()
                incr = 0
                r = True
            else:
                _bin = bins.popleft()

            status = parser.status(parser.stat, _bin,
                                   basename(fm.curr_file), r)
            pbar.set_description(status)
            try:

                parser.process_id(_bin, p.date_range,
                                  fm.curr_file, fm.parsed_file)
            except Exception as e:
                print(e)
                sys.exit()
            # pbar.set_description(status)
            pbar.update(incr)


    # try:
    #     from kgd.core import main
    #     exit_status = main()
    #     if exit_status == 2:
    #         print(cnst.NO_BINS)
    #     elif exit_status == 3:
    #         print(cnst.TOO_MANY_FAILS)
    #     elif exit_status == 4:
    #         print(cnst.SRV_IS_DOWN)
    # except KeyboardInterrupt:
    #     from kgd.constants import ExitStatus
    #     exit_status = ExitStatus.ERROR_CTRL_C
    #
    # sys.exit(exit_status)


if __name__ == "__main__":
    main()
