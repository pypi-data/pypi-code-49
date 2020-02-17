from datetime import datetime
import re

UNCONVERTED_DATA_REMAINS_REGEX = re.compile(r'^unconverted data remains: (\d+)?([-+]\d{2}:?\d{0,2})?$')


def get_datetime(time_string: str) -> datetime:
    """
    One can't be certain on time format coming in. ISO 8601 can have many forms. This function attempts to support
    the most common ones.
    """
    # Necessary to recognise time strings ending with Z as UTC
    reformatted_time_string = time_string.replace('Z', '+0000')
    # Todo: Generate these formats programmatically
    # Todo: To be fully ISO 8601 compliant, decimal points/commas should be supported at each lowest level,
    #       e.g 2020-01-01T13.5; 2020-01-01T13:30.5; 2020-01-01T13:30:30.5
    #       This is not supported
    for fmt in ('%G-W%V-%uT%H:%M',
                '%G-W%V-%uT%H:%M:%S',
                '%G-W%V-%uT%H:%M:%S.%f',
                '%GW%V%uT%H%M',
                '%GW%V%uT%H%M%S',
                '%GW%V%uT%H%M%S.%f',
                '%Y-%jT%H:%M',
                '%Y-%jT%H:%M:%S',
                '%Y-%jT%H:%M:%S.%f',
                '%Y%jT%H%M',
                '%Y%jT%H%M%S',
                '%Y%jT%H%M%S.%f',
                '%Y-%m-%dT%H:%M',
                '%Y-%m-%dT%H:%M:%S',
                '%Y-%m-%dT%H:%M:%S.%f',
                '%Y%m%dT%H%M',
                '%Y%m%dT%H%M%S',
                '%Y%m%dT%H%M%S.%f'):
        try:
            # For each format, try cast to datetime. If it succeeds it is the datetime wanted
            return datetime.strptime(reformatted_time_string, fmt)
        except ValueError as e:
            uncovered_data = UNCONVERTED_DATA_REMAINS_REGEX.search(str(e))
            # Two reasons for uncovered data, UCT offset and/or more than 6 digits in fraction
            if uncovered_data:
                extra_digits = uncovered_data.group(1)
                uct_offset = uncovered_data.group(2)
                fixed_uct_offset = ''
                if uct_offset:
                    # Note bugs: https://bugs.python.org/issue15873, https://bugs.python.org/issue31800 which means that
                    # UTC offset is not recognised when for e.g. in format +04:00 instead of +0400. This is fixed in
                    # Python 3.7 but we want to support Python 3.6, therefore strip final colon.
                    reformatted_time_string = reformatted_time_string.replace(uct_offset, '')
                    # Ensure of format +0400 for example
                    fixed_uct_offset = uct_offset.replace(':', '').ljust(5, '0')
                if '%f' in fmt and extra_digits:
                    # Strip extra digits from fraction because only 6 are supported by strptime's %f
                    reformatted_time_string = re.sub(rf'{extra_digits}$', '', reformatted_time_string)
                if uct_offset:
                    # Add fixed UTC offset back to string
                    reformatted_time_string += fixed_uct_offset
                    # Modify strptime format to take UTC offset into account
                    fmt = fmt + '%z'
                if uct_offset or ('%f' in fmt and extra_digits):
                    # If either of the above uncovered data conditions occurred, return according to new format
                    try:
                        return datetime.strptime(reformatted_time_string, fmt)
                    except ValueError:
                        pass
    raise ValueError(f'{time_string} does not conform to an ISO 8601 compatible format.')
