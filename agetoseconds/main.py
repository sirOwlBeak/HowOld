
import click

import age


def validateDateParameter(ctx, param, value):
    try:
        validParameter = [int(token) for token in value.lower().strip().split('-')]
        return validParameter
    except ValueError:
        raise click.BadParameter("date should be formatted as YYYY-MM-DD")


def validateTimeParameter(ctx, param, value):
    try:
        validParameter = [int(token) for token in value.lower().strip().split(':')]
        return validParameter
    except ValueError:
        raise click.BadParameter("time should be formatted as hh:mm:ss")


@click.group(options_metavar = "<options>")
@click.version_option()
def cli():
    ''' This tool calculates your age in seconds
    '''
    pass
    

@cli.command(options_metavar = "<options>")
@click.argument("date", callback=validateDateParameter)
@click.option("--time", callback=validateTimeParameter, default="0:0:0")
def birth(date, time):
    year, month, day = date
    hour, minute, second = time
    birth = age.Age()
    birth.set(year, month, day)
    birth.addTime(hour, minute, second)
    click.echo(birth.tick())
    
