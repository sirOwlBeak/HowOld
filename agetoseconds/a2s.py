import click

import dt
import calculator

YEAR    = 'Y'
MONTH   = 'M'
WEEK    = 'W'
DAY     = 'D'
HOUR    = 'h'
MINUTE  = 'm'
SECOND  = 's'

def _parse_date(ctx, param, value):
    try:
        value = [int(v) for v in value.split('-')]
        return value
    except ValueError:
        raise click.BadParameter("Please format your date of birth as YYYY-MM-DD, using only positive integer values")
    except AttributeError:
        return

def _parse_time(ctx, param, value):
    try:
        value = [int(v) for v in value.split(':')]
        return value
    except ValueError:
        raise click.BadParameter("Please format your time of birth as hh:mm:ss, using only positive integer values")
    except AttributeError:
        return
        
'''
def _load_birthday(ctx, param, boolean):
    if boolean or ctx.resilient_parsing:
        try:
            user_datetime = dt.loadDatetime()
            return user_datetime
        except IOError:
            raise click.UsageError("Cannot find stored birthday.\nPlease use 'a2s --store --date=YYYY-MM-DD [OPTIONS]' to store a birthday for later use.", ctx)
'''

@click.command()
@click.option('--date', '-d',
    callback=_parse_date,
    help="Format your date of birth as YYYY-MM-DD"
)
@click.option('--time', '-t',
    callback=_parse_time,
    help="Format your time of birth as hh:mm:ss"
)
@click.option('--store', '-s',
    is_flag=True
)
@click.option('--load', '-l',
    is_flag=True,
    ##callback=_load_birthday,
    expose_value=True,
    ##is_eager=True
)
@click.option('--base', '-b',
    type=click.Choice([YEAR, WEEK, DAY, HOUR, MINUTE, SECOND])
)
def cli(date, time, store, base, load):
    '''This command calculates your age in seconds.'''
    year, month, day, hour, minute, second = [0]*6
    user_datetime = None
    if not date and not time:
        click.echo("Nothing to do.\nPlease specify your birthday, use 'a2s --date [OPTIONS]'")
        return
    if date:
        year, month, day = date
    if time:
        hour, minute, second = time
    user_datetime = dt.newDatetime(year, month, day, hour, minute, second)
    result = calculator.calculateSeconds(user_datetime)
    if base:
        click.echo(_conversion(base, result))
    else:
        click.echo(result)

def _conversion(unit, value):
    if unit is YEAR:
        val = calculator.convertToBaseYear(value)
    elif unit is WEEK:
        val = calculator.convertToBaseWeek(value)
    elif unit is DAY:
        val = calculator.convertToBaseDay(value)
    elif unit is HOUR:
        val = calculator.convertToBaseHour(value)
    elif unit is MINUTE:
        val = calculator.convertToBaseMinute(value)
    else:
        raise
    return val
    
