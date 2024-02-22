# import click
# import toml
# import json
# import ast
#
#
# def get_dependencies_from_setup(setup_content):
#     dependencies = []
#     try:
#         tree = ast.parse(setup_content)
#         for node in tree.body:
#             if isinstance(node, ast.Assign):
#                 for target in node.targets:
#                     if isinstance(target, ast.Name) and target.id == "install_requires":
#                         if isinstance(node.value, ast.List):
#                             dependencies = [
#                                 elt.s
#                                 for elt in node.value.elts
#                                 if isinstance(elt, ast.Str)
#                             ]
#                         break
#     except SyntaxError:
#         pass
#     return dependencies
#
#
# @click.command()
# @click.option("--setup-path", "-s", help="Path to the setup.py file")
# @click.option("--output-path", "-o", help="Path to save the pyproject.toml file")
# @click.option("--project-name", "-n", help="Name of the project in pyproject.toml")
# @click.option(
#     "--project-version", "-v", help="Version of the project in pyproject.toml"
# )
# @click.option(
#     "--additional-metadata",
#     "-m",
#     help="Additional metadata for pyproject.toml in JSON format",
# )
# def migrate_setup_to_toml(
#     setup_path, output_path, project_name, project_version, additional_metadata
# ):
#     if not all([setup_path, output_path, project_name, project_version]):
#         click.echo(
#             "Please provide setup-path, output-path, project-name, and project-version."
#         )
#         return
#
#     with open(setup_path, "r") as setup_file:
#         setup_content = setup_file.read()
#
#     setup_dependencies = get_dependencies_from_setup(setup_content)
#     print(setup_dependencies)
#
#     pyproject_content = {
#         "tool": {
#             "poetry": {
#                 "name": project_name,
#                 "version": project_version,
#             }
#         }
#     }
#
#     if "install_requires" in pyproject_content["tool"]["poetry"]:
#         for dep in setup_dependencies:
#             if dep in pyproject_content["tool"]["poetry"]["install_requires"]:
#                 pyproject_content["tool"]["poetry"]["install_requires"].remove(dep)
#
#     if additional_metadata:
#         additional_metadata_dict = json.loads(additional_metadata)
#         pyproject_content["tool"]["poetry"].update(additional_metadata_dict)
#
#     with open(output_path, "w") as toml_file:
#         toml.dump(pyproject_content, toml_file)
#
#     click.echo("Migration successful!")
#
#
# if __name__ == "__main__":
#     migrate_setup_to_toml()
