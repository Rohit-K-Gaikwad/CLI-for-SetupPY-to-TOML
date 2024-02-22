import toml
import click
import json


@click.command()
@click.option('--setup-path', '-s', help='Path to the setup.py file')
@click.option('--output-path', '-o', help='Path to the pyproject.toml file')
@click.option('--project-name', '-n', help='Name of the project in pyproject.toml')
@click.option('--project-version', '-v', help='Version of the project in pyproject.toml')
@click.option('--additional-metadata', '-m', help='Additional metadata')
def migrate_setup_to_toml(setup_path, output_path,
                          project_name, project_version,
                          additional_metadata=None):
    if additional_metadata is None:
        additional_metadata = '{"new": "rohit"}'

    with open(setup_path, 'r') as setup_file:
        setup_content = setup_file.read()

    try:
        if additional_metadata:
            additional_metadata_dict = json.loads(additional_metadata)
        else:
            additional_metadata_dict = {}

        pyproject_content = {
            'tool': {
                'poetry': {
                    'name':
                        project_name,
                    'version': project_version,
                    'setup_cont': setup_content,
                    ** additional_metadata_dict
                }
            }
        }

        with open(output_path, 'w') as toml_file:
            toml.dump(pyproject_content, toml_file)

        click.echo('Migration Successful !')
    except json.JSONDecodeError as e:
        click.echo(f"Error decoding JSON: {e}")


if __name__ == '__main__':
    migrate_setup_to_toml()
