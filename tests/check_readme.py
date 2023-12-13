with open('README.md', 'r') as file:
  contents = file.read()
  if 'Hello world' not in contents:
    raise ValueError('The README has invalid content')
