import click
import toml
import ast
import os
import re


def get_setup_metadata(setup_content):
    metadata = {}
    pattern = r"(\b\w+\b)\s*=\s*(['\"])(.*?)\2"
    matches = re.findall(pattern, setup_content)
    for match in matches:
        key = match[0]
        value = match[2]
        metadata[key] = value
    return metadata


def convert_setup_to_toml(setup_path):
    # Read setup.py
    with open(setup_path, 'r') as setup_file:
        setup_content = setup_file.read()

    # Get metadata from setup.py
    setup_metadata = get_setup_metadata(setup_content)

    # Generate pyproject.toml content
    pyproject_content = {
        'build-system': {
            'requires': ['setuptools', 'wheel'],
            'build-backend': 'setuptools.build_meta',
        },
        'tool': {
            'setuptools': setup_metadata
        }
    }

    # Write to pyproject.toml in the same directory as setup.py
    output_path = os.path.join(os.path.dirname(setup_path), 'pyproject.toml')
    with open(output_path, 'w') as toml_file:
        toml.dump(pyproject_content, toml_file)

    return output_path


def find_setup_files(directory):
    setup_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'setup.py':
                setup_files.append(os.path.join(root, file))
    return setup_files


@click.command()
@click.option('--directory', '-d', default='.', help='Directory to search for setup.py files')
def migrate_setup_to_toml(directory):
    breakpoint()
    setup_files = find_setup_files(directory)
    if not setup_files:
        click.echo("No setup.py files found in the specified directory or its subdirectories.")
        return

    for setup_file in setup_files:
        pyproject_toml_path = convert_setup_to_toml(setup_file)
        click.echo(f'Migration successful! pyproject.toml file created at: {pyproject_toml_path}')


if __name__ == '__main__':
    migrate_setup_to_toml()
