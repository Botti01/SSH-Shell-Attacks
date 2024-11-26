import subprocess
import sys
import re
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

def format_section(section):
    """
    Format a section string into a more readable format.

    Converts strings like "section2" into "Section 2".

    Args:
        section (str): The name of the section (e.g., "section1", "section2").

    Returns:
        str: The formatted section name with proper capitalization and spacing.
    """
    import re

    match = re.match(r"(section)(\d+)", section, re.IGNORECASE)
    if match:
        word, number = match.groups()
        return f"{word.capitalize()} {number}"
    return section

def install_packages(section):
    """
    Install dependencies required for a specific section based on requirements.txt.

    Args:
        section (str): The name of the section (e.g., "common", "section0").
    """
    requirements_file = "../requirements.txt"
    
    # Read the requirements file and parse sections
    try:
        with open(requirements_file, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(Fore.RED + f"Error: {requirements_file} not found.")
        sys.exit(1)
    
    # Extract dependencies for the specified section
    in_section = False
    packages = []
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            # Detect section headers
            in_section = section in line
        elif in_section and line and not line.startswith("#"):
            # Add non-comment lines within the section
            packages.append(line)
            
    section = format_section(section)

    if not packages:
        print(Fore.YELLOW + f"No dependencies found for section '{section}'.")
        return
    
    print(Fore.BLUE + f"Installing {section} packages: {', '.join(packages)}")

    # Install packages using pip
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(Fore.GREEN + f"Successfully installed: {package}")
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"Error installing package {package}: {e}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python install_dependencies.py <section_name>")
        sys.exit(1)

    section_name = sys.argv[1]
    # print(Fore.MAGENTA + "Installing common dependencies...")
    install_packages("common")
    # print(Fore.MAGENTA + f"Installing dependencies for section: {section_name}...")
    install_packages(section_name)
