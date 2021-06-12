from pathlib import Path
import os


# Function to create a new folder
def create_folder(parent_folder, folder_name):
    new_folder = parent_folder / folder_name
    new_folder.mkdir(parents=False, exist_ok=False)

    return new_folder


# Function to create .project file
def create_project_file(parent_folder, project_name):
    from xml.dom import minidom

    root = minidom.Document()

    xml = root.createElement('rootElement')
    root.appendChild(xml)

    xml_str = root.toprettyxml(indent="\t")

    file_name = '.project'
    with open(file_name, 'w') as f:
        f.write(xml_str)


# Create folder structure
def create_ace_structure(component_type):
    # Get path to ACE workspace
    ace_workspace_env_var_key = 'ACE_WORKSPACE'

    try:
        ace_workspace = Path(os.getenv(ace_workspace_env_var_key))
    except TypeError:
        print(f'Error: Please set {ace_workspace_env_var_key} environment variable to point to your ACE workspace '
              f'directory.')
    else:
        # Get project name from either argument or user
        project_name = input('Enter name of project:').lower()

        # Create root folder
        root_folder = ace_workspace / project_name
        root_folder.mkdir(parents=False, exist_ok=False)

        # Create common folder structure
        config_folder = create_folder(root_folder, 'config')
        setup_folder = create_folder(root_folder, 'setup')
        tests_folder = create_folder(root_folder, 'tests')
        source_folder = create_folder(root_folder, 'source')

        if component_type == 'ace_app':
            create_project_file(project_name)


create_ace_structure('ace_app')
