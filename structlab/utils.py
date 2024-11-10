import os
import subprocess

def create_ml_project_structure(project_path, init_git=False, extra_dirs=None, extra_files=None):
    """
    Create a structured directory for a new ML project.
    
    Parameters:
        project_path (str): The root directory path for the new project.
        init_git (bool): Whether to initialize a Git repository in the project directory.
        extra_dirs (list): Additional directories to create within the project.
        extra_files (list): Additional files to create within the project.
    """
    # Basic ML project structure
    dirs = [
        "data/raw",       # Raw data files
        "data/processed", # Processed data
        "data/external",  # External data sources
        "notebooks",      # Jupyter notebooks
        "scripts",        # Python scripts for data processing or modeling
        "models",         # Model storage
        "reports",        # Reports and summaries
        "src",            # Source code directory
        "src/utils",      # Utility functions
        "src/configs",    # Configuration files
        "tests",          # Unit and integration tests
        "references"      # Documentation and references
    ]
    
    # Add user-defined extra directories
    if extra_dirs:
        dirs.extend(extra_dirs)
    
    # Define some default files
    files = [
        ".gitignore",     # Git ignore file
        "README.md",      # Project README
        "requirements.txt",  # Dependencies
        "setup.py",       # Setup file for package
        "src/__init__.py" # Init for package structure
    ]
    
    # Add user-defined extra files
    if extra_files:
        files.extend(extra_files)

    # Create the main project directory
    os.makedirs(project_path, exist_ok=True)
    
    # Create all directories
    for dir_path in dirs:
        os.makedirs(os.path.join(project_path, dir_path), exist_ok=True)
    
    # Create all files
    for file_path in files:
        with open(os.path.join(project_path, file_path), 'w') as f:
            pass 

    # Initialize Git if requested
    if init_git:
        subprocess.run(["git", "init", project_path], check=True)
        print(f"Initialized an empty Git repository in {project_path}")

    print(f"Project structure created at {project_path}")

def create_c_project_structure(project_path, init_git=False, extra_dirs=None, extra_files=None, headers=None):
    
    # Basic C project structure
    dirs = [
        "src",          # Source files
        "include",      # Header files
        "lib",          # External libraries (if needed)
        "tests",        # Test files
        "build",        # Compiled output (generated files)
        "docs"          # Documentation files
    ]
    
    # Add user-defined extra directories
    if extra_dirs:
        dirs.extend(extra_dirs)
    
    # Define some default files
    files = [
        ".gitignore",     # Git ignore file
        "README.md",   # Project README
    ]
    
    # Add user-defined extra files
    if extra_files:
        files.extend(extra_files)
        
    if headers:
        for header in headers:
            files.append(f"include/{header}.h")
            files.append(f"tests/test_{header}.c")

    # Create the main project directory
    os.makedirs(project_path, exist_ok=True)
    
    # Create all directories
    for dir_path in dirs:
        os.makedirs(os.path.join(project_path, dir_path), exist_ok=True)
    
    # Create all files
    for file_path in files:
        with open(os.path.join(project_path, file_path), 'w') as f:
            pass 
        
    with open(os.path.join(project_path, "Makefile"), 'w') as f:
        f.write(generate_makefile_content())
    # Initialize Git if requested
    if init_git:
        subprocess.run(["git", "init", project_path], check=True)
        print(f"Initialized an empty Git repository in {project_path}")

    print(f"Project structure created at {project_path}")

def create_shortcut(project_path, alias_name="mlproj"):
    """
    Create a shortcut command or alias for the project directory.
    
    Parameters:
        project_path (str): The root directory path for the new project.
        alias_name (str): The name of the alias command.
    """
    # Define the alias command
    alias_command = f"alias {alias_name}='cd {project_path}'"

    # Add alias to .bashrc or .zshrc
    shell_config_path = os.path.expanduser("~/.bashrc")
    if os.path.exists(os.path.expanduser("~/.zshrc")):
        shell_config_path = os.path.expanduser("~/.zshrc")
    
    with open(shell_config_path, 'a') as shell_config:
        shell_config.write(f"\n# Alias for ML project\n{alias_command}\n")

    print(f"Alias '{alias_name}' added. Reload your shell or source {shell_config_path} to use it.")

def generate_makefile_content():
    """
    Generate the content of a Makefile for a C project.
    
    Returns:
        str: Content of the Makefile.
    """
    makefile_content = """# Compiler
CC = gcc
CFLAGS = -Wall -Iinclude

# Directories
SRC_DIR = src
BUILD_DIR = build
TEST_DIR = tests

# Source files and object files
SRC_FILES = $(wildcard $(SRC_DIR)/*.c)
OBJ_FILES = $(patsubst $(SRC_DIR)/%.c, $(BUILD_DIR)/%.o, $(SRC_FILES))
TEST_FILES = $(wildcard $(TEST_DIR)/*.c)

# Output binary
TARGET = $(BUILD_DIR)/my_c_project

# Build target
$(TARGET): $(OBJ_FILES)
\t$(CC) $(CFLAGS) -o $@ $^

# Compile source files into object files
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c | $(BUILD_DIR)
\t$(CC) $(CFLAGS) -c $< -o $@

# Create build directory if it doesn't exist
$(BUILD_DIR):
\tmkdir -p $(BUILD_DIR)

# Run tests
test: $(TARGET)
\t@for test_file in $(TEST_FILES); do \\
\t\t$(CC) $(CFLAGS) $$test_file $(OBJ_FILES) -o $(BUILD_DIR)/$$(basename $$test_file); \\
\t\t./$(BUILD_DIR)/$$(basename $$test_file); \\
\tdone

# Clean up build artifacts
clean:
\trm -rf $(BUILD_DIR)

# Phony targets
.PHONY: all test clean
"""
    return makefile_content