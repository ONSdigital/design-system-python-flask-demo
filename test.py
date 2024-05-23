import os
scenarios = []
root_directory = 'templates/components'
directories = [name for name in os.listdir(root_directory)]
example_files = [f'components/{directory}/{file}' for directory in directories for file in os.listdir(os.path.join(root_directory, directory)) if not file.startswith('example')]
print(example_files)