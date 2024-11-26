import subprocess
import sys

def install_packages(section):
    """
    Install dependencies required for a specific notebook section.
    
    Args:
        section (str): The name of the section (e.g., "section0", "section1").
    """
    # Define dependencies for each section
    dependencies = {
        "section0": ["pyarrow"],                # Add dependencies for section0
        "section1": ["matplotlib", "seaborn"],  # Add dependencies for section1
        "section2": ["scikit-learn"],           # Add dependencies for section2
        "section3": ["scipy", "numpy"],         # Add dependencies for section3
        "section4": ["transformers"],           # Add dependencies for section4
    }

    # Check if the section exists in the dependencies dictionary
    if section not in dependencies:
        print(f"Section '{section}' not found. No packages to install.")
        return

    # Get the packages for the section
    packages = dependencies[section]

    print(f"Installing packages for {section}: {', '.join(packages)}")

    # Install each package
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed: {package}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing package {package}: {e}")
            sys.exit(1)

if __name__ == "__main__":
    # Check if a section name is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python install_dependencies.py <section_name>")
        sys.exit(1)

    # Get the section name from command-line arguments
    section_name = sys.argv[1]
    install_packages(section_name)
