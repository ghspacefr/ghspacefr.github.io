import os

def generate_index_page(directory_path, output_file='index.html'):
    # Get a list of all files and directories in the directory
    items = [ f for f in os.listdir(directory_path) if f != "index.html" ]
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en"><head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <title>Directory listing for {directory_path}</title>
    </head>
    <body>
    <h1>Directory listing for {directory_path}</h1>
    <hr>
    <ul>
    <li><a href="../">../</a></li>
    """

    for item in items: 
        html_content += f'<li><a href="{os.path.join("/", directory_path, item)}">{item}</a></li>\n'

    html_content += """
    </ul>
    <hr>
    </body></html>
    """

    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        file.write(html_content)

    print(f"Index page generated successfully: {output_file}")

def generate_index_pages_for_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        # Check if an index.html file already exists
        index_file_path = os.path.join(root, 'index.html')
        generate_index_page(root, index_file_path)
