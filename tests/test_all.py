"""Test all functions in the veleslibrary package."""

import importlib.util
import inspect
import os
import pytest
import veleslibrary


def get_package_path(package_name):
    """
    Dynamically locate the path of a Python package.

    :param package_name: The name of the Python package (e.g., "veleslibrary").
    :return: The absolute path to the package directory.
    """
    spec = importlib.util.find_spec(package_name)
    if not spec or not spec.submodule_search_locations:
        raise ImportError(f"Cannot find package {package_name}")
    return os.path.abspath(spec.submodule_search_locations[0])


def collect_function_paths_from_package(package_name):
    """
    Collect full paths (e.g., veleslibrary.questionnaires.rses) of all functions in the given package.

    :param package_name: The top-level name of the package (e.g., "veleslibrary").
    :return: A list of full paths to functions in the package.
    """
    package_path = get_package_path(package_name)
    function_paths = []

    for root, _, files in os.walk(package_path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                module_path = os.path.join(root, file)
                relative_path = os.path.relpath(module_path, package_path)
                module_name = os.path.splitext(relative_path.replace(os.sep, "."))[0]

                # Construct the full module name
                full_module_name = f"{package_name}.{module_name}"

                # Dynamically load the module
                try:
                    spec = importlib.util.spec_from_file_location(
                        full_module_name, module_path
                    )
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                except Exception as e:  # pylint: disable=broad-except
                    print(f"Failed to load module {full_module_name}: {e}")
                    continue

                # Collect functions defined in the module
                for name in inspect.getmembers(module, inspect.isfunction):
                    function_paths.append(f"{full_module_name}.{name[0]}")
    function_paths = [
        ".".join(path.split(".")[:-2] + path.split(".")[-1:]) for path in function_paths
    ]
    return function_paths


def test_all():
    """
    Dynamically import all functions in the veleslibrary package and run them.
    """
    veleslibrary_functions = [
        f"{func}()" for func in collect_function_paths_from_package("veleslibrary")
    ]
    for func in veleslibrary_functions:
        try:
            eval(func, {"veleslibrary": veleslibrary})  # pylint: disable=eval-used
        except Exception as e:  # pylint: disable=broad-except
            pytest.fail(f"Function {func} raised an exception: {e}")
