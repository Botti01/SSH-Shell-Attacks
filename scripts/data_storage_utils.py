import os

def save_plot(fig, 
              directory="plots", 
              filename="plot", 
              filetype="png", 
              overwrite=False):
    """
    Save a Matplotlib figure to a specified directory with custom settings.
    
    Parameters:
    - fig (matplotlib.figure.Figure): The Matplotlib figure object to save.
    - directory (str): The name of the directory to save the plot.
    - filename (str): The desired name of the file (without extension).
    - filetype (str): File type for the saved plot ('png', 'jpg', 'jpeg', etc.).
    - overwrite (bool): Whether to overwrite an existing file. Default is False.
    
    Returns:
    - filepath (str): The full path where the file is saved.
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")

    # Build the full file path
    filepath = os.path.join(directory, f"{filename}.{filetype}")

    # Check if file exists and handle overwrite parameter
    if os.path.exists(filepath) and not overwrite:
        print(f"File '{filepath}' already exists. Set overwrite=True to overwrite it.")
        return
    elif os.path.exists(filepath) and overwrite:
        print(f"Overwriting file: '{filepath}'")

    # Save the figure
    fig.savefig(filepath, format=filetype, bbox_inches="tight")
    print(f"Plot saved successfully at: '{filepath}'")

    return filepath
