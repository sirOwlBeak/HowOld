import click

import age


@click.group(options_metavar = "<options>")
@click.version_option()
@click.pass_context
def cli(ctx):
    ''' This tool calculates your age in seconds
    '''
    ctx.obj = age.Age(1986, 8, 18)
    

@cli.command(options_metavar = "<options>")
@click.argument( 'year',
    type = click.INT,
)
@click.argument( 'month',
    type = click.INT,
)
@click.argument( 'day',
    type = click.INT,
)
@click.option( '--hour', 'hour',
    type = click.INT,
    metavar = "<integer>",
    help = "Specify the hour of birth",
    default = 0,
)
@click.option( '--minute', 'minute',
    type = click.INT,
    metavar = "<integer>",
    help = "Specify the minute of birth",
    default = 0,
)
@click.option( '--second', 'second',
    type = click.INT,
    metavar = "<integer>",
    help = "Specify the second of birth",
    default = 0,
)
@click.option( '--store', '-S', 'savefile',
    type = click.STRING,
    metavar = "<text>",
    help = "Store this date by entering a name or leave blank for standard user",
    default = "_USER",
)
@click.pass_context
def date(ctx, year, month, day, hour, minute, second, savefile):
    ''' Set a new birthday for the calculator to count
        
        Provide a valid 'year', 'month' and 'day' this command to load a 
        new date in memory. The 'year' argument is entered as a four 
        digit number. The 'month' and 'day' arguments are entered with 
        one or two digits.
        
        Optionally, you can specify the time of birth, which will result 
        in a more accurate calculation of your age.
        
        You can store the date with the '-S' switch and an optional 
        name. If no name was specified , the command will store the date
        under the user that is currently logged in.
    '''
    #ctx.obj = age.Age(year, month, day, hour, minute, second)
    click.echo(ctx.obj)


@cli.command(options_metavar = "<options>")
@click.option('-s', 'base', 
    flag_value = "seconds", 
    default = True,
)
@click.option('-m', 'base', 
    flag_value = "minutes",
)
@click.option('-h', 'base', 
    flag_value = "hours",
)
@click.option('-d', 'base', 
    flag_value = "days",
)
@click.option('-w', 'base', 
    flag_value = "weeks",
)
@click.option('-y', 'base', 
    flag_value = "years",
)
@click.option('--load', '-L', 'loadfile', 
    default = "_USER",
)
#@click.pass_context
#def tick(ctx, base, loadfile):
@click.pass_obj
def tick(obj, base, loadfile):
    ''' Calculates a new value of your age in seconds
    '''
    click.echo(obj)
    click.echo(obj.base)
    
