
import click
import shelve
import os
import os.path

import age


'''
    user_data = {
        'age' = None,
        'config' = None
    }

'''

DB_FILEPATH = os.path.join(os.environ['HOME'], '.local', 'applications')
DB_FILENAME = 'howold-userdata.db'


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
@click.option("-d", 'debug', is_flag=True)
@click.version_option()
@click.pass_context
def cli(ctx, debug):
    ''' This tool calculates your age in seconds
    '''
    ctx.obj = {'DEBUG':debug}


def newAge(date_values, time_values=(0,0,0)):
    year, month, day = date_values
    hour, minute, second = time_values
    return age.Age(year, month, day, hour, minute, second)


@cli.command(options_metavar = "<options>")
@click.argument("date", callback=validateDateParameter)
@click.option("--time", callback=validateTimeParameter, default="0:0:0")
@click.option("--save", 'user')
@click.pass_context
def birth(ctx, date, time, user):
    ageObject = newAge(date, time)
    click.echo(ageObject.get())
    if user:
        data = {
            'age' : ageObject,
        }
        filepath = os.path.join(os.getcwd() if ctx.obj['DEBUG'] else DB_FILEPATH, DB_FILENAME)
        db = shelve.open(filepath)
        if db.get(str(user)):
            click.echo('user exists')
            db.get(str(user)).update(data)
        else:
            click.echo('make user')
            db[str(user)] = data
        db.close()
