import importlib
import pkgutil


def import_all_models():
    package_name = __name__

    for _, module_name, _ in pkgutil.iter_modules(__path__):
        importlib.import_module(f"{package_name}.{module_name}")
