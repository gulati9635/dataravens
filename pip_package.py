import subprocess

def install_project_dependencies(requirements_file='dependencies.txt'):
    try:
        with open(requirements_file, 'r') as file:
            requirements = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The '{requirements_file}' file not found.")
        return

    if not requirements:
        print(f"No dependencies found in '{requirements_file}'.")
        return

    for requirement in requirements:
        try:
            subprocess.check_call(['pip', 'install', requirement])
        except subprocess.CalledProcessError as e:
            print(f"Error installing {requirement}: {e}")
        except KeyboardInterrupt:
            print("\nInstallation interrupted by the user.")
            break

    print("All dependencies installed successfully!")

# if __name__ == "__main__":
#     install_project_dependencies()
