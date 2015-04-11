import click
import datetime

import age


SECONDS = 'seconds' 
MINUTES = 'minutes' 
HOURS = 'hours' 
DAYS = 'days' 
WEEKS = 'weeks' 
YEARS = 'years'


DATE_SPLIT_CHAR = '-'
def validateDate(ctx, param, value):
    try:
        args = [int(arg) for arg in value.strip().lower().split(DATE_SPLIT_CHAR, 3) if arg.isnumeric()]
        validated = datetime.date(*args)
        return validated
    except ValueError:
        raise click.BadParameter("\nPlease format your date as 'yyyy-mm-dd'.")
    except:
        raise


TIME_SPLIT_CHAR = ':'
def validateTime(ctx, param, value):
    try:
        args = [int(arg) for arg in value.strip().lower().split(TIME_SPLIT_CHAR, 3) if arg.isnumeric()]
        validated = datetime.time(*args)
        return validated
    except ValueError:
        raise click.BadParameter("\nPlease format your time as 'hh:mm:ss'.")
    except:
        raise


def validateUnit(ctx, param, value):
    try:
        validated = value.strip().lower()
        if validated in age.Age.units:
            click.echo(validated)
            return validated
        else:
            return SECONDS
    except:
        raise


@click.group()
@click.version_option()
def cli():
    ''' This tool calculates your age in seconds
    '''
    pass


@cli.command()
@click.argument('date', callback=validateDate)
@click.option('--time', callback=validateTime, default='0:0:0')
@click.option('--unit', callback=validateUnit, default=SECONDS)
def report(date, time, unit):
    age_user = age.Age(date, time)
    if unit != SECONDS:
        age_user.unit = unit
        click.echo(age_user.get())
    else:
        click.echo(age_user.get())
