from pathlib import Path
import os

ace_workspace = os.getenv('ACE_WORKSPACE')
ace_workspace = Path(ace_workspace)

def create_ace_structure(component_type):
    if component_type == 'ace_application':
        # Create .project file
        project_folder = Path.