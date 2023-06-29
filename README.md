# AI-Justice

AI-Justice is an innovative Python-based project that leverages large language models (LLMs) for automated scoring and evaluation of legal documents. The project initially focuses on equity analysis of renewable energy laws but is designed to be extensible for diverse text analysis applications.

## Project Overview

Energy justice is a critical aspect of the transition to renewable energy. This project uses AI and high-performance computing (HPC) to interpret and score energy laws, based on the scorecard developed by the Initiative for Energy Justice. The aim is to analyze these laws in terms of accessibility, affordability, and environmental impact.

The project also serves as an educational platform for students interested in AI, policy, and HPC. Students can learn how to use LLMs, handle large-scale data, manage job scheduling efficiently, and execute complex parallel computations.

## Learning Objectives
Participants in this project will:

* Learn to use LLMs to evaluate legislation based on predefined scorecards
* Automate the workflow to download, interpret, and score a large number of bills
* Gain experience in handling large-scale data and managing complex parallel computations
* Learn to use HPC for efficient job scheduling, data management, and model training and execution
* Contribute to real-world energy justice initiatives

## Getting Started

### Using the Google Colab Notebook

1. **Access the Notebook:**

    Click on the link to access the [Google Colab notebook](https://colab.research.google.com/drive/1UQVNDa3PKTD5M06EBPqAfz5yA9IZJpjo?usp=sharing):

2. **Copy the Notebook to Your Drive:**

    To be able to edit and save your changes, you need to make a copy of the notebook in your drive. You can do this by clicking on `File > Save a copy in Drive` from the menu.

3. **Run Cells:**

    You can run a cell by clicking on the play button on the left side of the cell or by pressing `Shift + Enter` when the cell is selected.

4. **Edit Cells:**

    You can edit any text or code cell by double clicking on it.

5. **Adding Cells:**

    You can add cells by clicking on `+ Code` or `+ Text` in the upper menu. The new cell will be added below the currently selected cell.

6. **Saving the Notebook:**

    All changes are saved to your copy of the notebook in your Google Drive automatically, you can also click on `File > Save` to save at any time.

7. **Downloading the Notebook:**

    If you want to download the notebook, you can go to `File > Download > Download .ipynb` or `File > Download > Download .py` for a Python script format.

Remember, the notebook runs on a virtual machine in the cloud, so if you close the tab or the browser, all the variables, imported libraries, and functions will be lost. However, the cells' output will be saved, and you can continue from where you left off later by running the necessary cells again.

### Setting Up a Local Virtual Environment and Installing Dependencies

Alternatively, you can run the notebook locally. You need to set up a virtual environment and install the necessary dependencies. Follow the steps below:

1. **Create a virtual environment:**
   
    Create a virtual environment by running the following command in your terminal:

    ```
    python3 -m venv env
    ```

2. **Activate the virtual environment:**

    On macOS and Linux, run:

    ```
    source env/bin/activate
    ```

    On Windows, run:

    ```
    .\env\Scripts\activate
    ```

3. **Install the dependencies:**

    After activating the virtual environment, you can install the required dependencies by running:

    ```
    pip install -r requirements.txt
    ```

    Make sure that the `requirements.txt` file is in your current directory. This file contains a list of all the Python packages that your project depends on.

Now, your virtual environment is ready.

## License

This project is licensed under the Apache2.0 License - see the LICENSE file for details

## Credits

This project's documents were prepared with assistance from GPT-4.
