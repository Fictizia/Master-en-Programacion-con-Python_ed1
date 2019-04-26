import pkgutil
import exercises
print(f'List of my exercises:')
for _, name, is_package in pkgutil.iter_modules(exercises.__path__):
    if name != '__main__':
        print(f'\t{name} (is package: {is_package})')
