"""
A set of functions to handle syntax differences between DBs
"""


def bind_var(var, db='oracle'):
    """Format of named bind variable"""
    if db == 'postgresql':
        return '%({})s'.format(var)
    elif db == 'oracle':
        return ':{}'.format(var)
    else:
        return ':{}'.format(var)


def interval_to_sec(inter_str, db='oracle'):
    """Format time interval to integer number of seconds"""
    if db == 'postgresql':
        return 'extract(epoch from ({}))/3600'.format(inter_str)
    elif db == 'oracle':
        return '({})*60*60*24'.format(inter_str)
    else:
        return '()'.format(inter_str)


def interval_last(inter_value, inter_unit='hour', db='oracle'):
    """
    Format interval like <last N hours/days> depending on DB
    :param inter_value: int
    :param inter_unit: hour|day
    :param db: vendor: postgresql|oracle
    :return:
    """
    if db == 'postgresql':
        return "(now() - interval '{} {}s')".format(inter_value, inter_unit)
    elif db == 'oracle':
        return "cast (sys_extract_utc(systimestamp) - interval '{}' {} as date)".format(inter_value, inter_unit)
    else:
        return ''
