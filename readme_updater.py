from datetime import datetime
import re

def generate():
    with open("./README.md") as f:
        readme_content = f.read()
    
    readme_replacement = f'Updated: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
    new_readme = re.sub('Updated: .*', readme_replacement, readme_content)

    with open("./README.md", "w") as f:
        f.write(new_readme)

generate()
