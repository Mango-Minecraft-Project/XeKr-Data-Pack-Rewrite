import json
import os
import re


with open('./src/generator/initial datapack/data.json', mode='rb') as file:
    data = json.load(file)


const_regex = r'%(.+)%'

def create_file_tree(dir_tree: dict | list, const: dict[str, str], content: dict ,now: str = './src'):
    for sub_data in dir_tree:
        if isinstance(sub_data, dict):
            for folder_name, subdir in sub_data.items():
                if re.match(const_regex, folder_name):
                    folder_name = const[folder_name[1:-1]]
                path = f'{now}/{folder_name}'
                if not os.path.isdir(path):
                    os.mkdir(path)
                create_file_tree(subdir, const, content, path)
        else:
            with open(f'{now}/{sub_data}', 'w') as file:
                json.dump(content[sub_data], file, indent=2)

create_file_tree(data['tree'], data['const'], data['content'])