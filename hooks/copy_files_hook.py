"""
Custom MkDocs hook for copying additional files to the site directory.

This hook copies the vendor-finder directory to the site output directory
so that it's accessible at /vendor-finder/ on the deployed website.
"""

import shutil
from pathlib import Path


def on_post_build(config, **kwargs):
    """
    Copy additional files and directories to the site directory after build.

    This runs after MkDocs has built the site, ensuring our additional files
    are included in the final output.

    Args:
        config: The MkDocs configuration object
    """
    # Get the root directory (where mkdocs.yml is located)
    root_dir = Path(config['docs_dir']).parent

    # Get the site directory (output directory)
    site_dir = Path(config['site_dir'])

    # Define files/directories to copy
    files_to_copy = [
        'vendor-finder'
    ]

    for item in files_to_copy:
        source = root_dir / item
        destination = site_dir / item

        if source.exists():
            if source.is_dir():
                # Copy entire directory
                if destination.exists():
                    shutil.rmtree(destination)
                shutil.copytree(source, destination)
                print(f"✓ Copied directory: {item} -> site/{item}")
            else:
                # Copy single file
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)
                print(f"✓ Copied file: {item} -> site/{item}")
        else:
            print(f"⚠ Warning: {item} not found, skipping")