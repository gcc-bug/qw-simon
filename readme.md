# Project Setup Instructions

This project depends on specific Python packages listed in the `requirements.txt` file. To ensure compatibility and manage dependencies effectively, it is recommended to set up a Python virtual environment. Follow these steps to create and activate a virtual environment and install the required packages:

### Step 1: Create the Virtual Environment

Run the following command in your terminal to create a virtual environment named `qw-simon`. This environment will contain all the necessary Python packages for this project.

```bash
python3 -m venv qw-simon
```
### Step 2: Activate the Virtual Environment

Before installing the dependencies, you need to activate the virtual environment. Use the appropriate command below based on your operating system:

On macOS and Linux:
```bash
source qw-simon/bin/activate
```
On Windows:
```bash
qw-simon\Scripts\activate
```
### Step 3: Install Dependencies
With the virtual environment activated, install the required packages by running:

```bash
pip install -r requirements.txt
```
This command will install all the dependencies listed in the requirements.txt file, ensuring that you have the correct versions needed to run the project.

## Deactivating the Virtual Environment
When you are done working on the project, you can deactivate the virtual environment by simply running:
```bash
deactivate
```
This will return your terminal to the normal system environment.

By following these steps, you can set up your project environment quickly and start working on the project in an isolated setting, minimizing potential issues related to package dependencies.