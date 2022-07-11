import click

@click.group()
def cli():
    pass

@click.command()
def createdDB():
    print("created Database")

@click.command()
def deleteDB():
    print("deleted Database") 

cli.add_command(createdDB)
cli.add_command(deleteDB)

@click.command()
@click.option('--count',default=1,help='number of greetings')
@click.argument('name')
def hello(count,name):
    for x in range(count):
        print(f'Hello{name}!')

cli.add_command(createdDB)
cli.add_command(deleteDB)
cli.add_command(hello)        

if __name__ == '__main__':
    cli()
