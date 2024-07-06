import click
from utils.api import get_robot_data, get_trust_score
from utils.contract import get_contract_data

@click.group()
def cli():
    pass

@cli.command()
@click.argument('robot_id')
def interact(robot_id):
    """Interact with the robot and get trust score"""
    try:
        robot_data = get_robot_data(robot_id)
        click.echo(f"Robot Data: {robot_data}")

        contract_address = "0xYourContractAddress"
        abi = [...]  # Replace with your contract ABI
        contract_data = get_contract_data(contract_address, abi, 'yourFunctionName', robot_id)
        click.echo(f"Smart Contract Data: {contract_data}")

        trust_score_data = {
            'robot_data': robot_data,
            'contract_data': contract_data
        }
        trust_score = get_trust_score(trust_score_data)
        click.echo(f"Trust Score: {trust_score}")

    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    cli()
