import os
import matplotlib.pyplot as plt

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

def plot_and_save(plot_func, 
                  plot_args=None, 
                  directory="plots", 
                  filename="plot", 
                  filetype="png", 
                  overwrite=False, 
                  show_plot=True):
    """
    Wrapper to plot, show, and save a figure.

    Parameters:
    - plot_func (callable): Function to generate the plot.
    - plot_args (dict, optional): Arguments to pass to the `plot_func`.
    - directory (str): Directory to save the plot.
    - filename (str): Name of the file to save (without extension).
    - filetype (str): File type for saving the plot (default: "png").
    - overwrite (bool): Whether to overwrite an existing file.
    - show_plot (bool): Whether to display the plot.

    Returns:
    - filepath (str): The path to the saved file.
    """
    if plot_args is None:
        plot_args = {}

    # Create the plot using the provided function and arguments
    plot_func(**plot_args)

    # Optionally show the plot
    if show_plot:
        plt.show()

    # Save the plot
    fig = plt.gcf()  # Get the current figure
    filepath = save_plot(fig, directory, filename, filetype, overwrite)

    return filepath
