#!/usr/bin/python

import os
import shutil
import jinja2
import yaml
from datetime import datetime

CONFIG = {}


# Function to copy contents of static folder to public folder
def copy_static_to_public(static_folder, public_folder):
    if not os.path.exists(public_folder):
        os.makedirs(public_folder)

    for item in os.listdir(static_folder):
        s = os.path.join(static_folder, item)
        d = os.path.join(public_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

if __name__ == "__main__":

    # Load the configuration file
    with open('config.yaml', 'r') as config_file:
        CONFIG = yaml.safe_load(config_file)

    output_dir = 'public'
    os.makedirs(output_dir, exist_ok=True)

    # Set up the Jinja2 environment
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

    # Render each template and save the output
    for template_name, template_config in CONFIG['templates'].items():
        template = env.get_template(template_config.get('template', f'{template_name}.html'))
        html = template.render(
                **CONFIG.get('default', {}),
                **template_config.get('context', {}),
                version=datetime.now().strftime("%Y-%m-%d %H:%M")
            )
        output_file = f"{template_name}.html"
        with open(os.path.join(output_dir, output_file), 'w') as f:
            f.write(html)

    copy_static_to_public('static', output_dir)

    print("Static pages generated successfully!")
