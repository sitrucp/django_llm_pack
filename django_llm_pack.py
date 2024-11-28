import os
from datetime import datetime

# Define the extensions to consider as important code files
CODE_EXTENSIONS = {".py", ".html", ".css", ".js", ".ts", ".json", ".md", ".txt"}

# Paths to exclude (commonly ignored in version control)
EXCLUDE_DIRS = {".git", "archive", "migrations", "__pycache__", "venv", "node_modules", "logs", "utils", "account", "allauth", "mfa", "socialaccount", "staticfiles"}

# User-defined paths to exclude
USER_EXCLUDE_PATHS = [
    #r"django_app\pbr\templates\account",
    #r"django_app\pbr\templates\allauth",
    #r"django_app\pbr\templates\mfa",
    #r"django_app\pbr\templates\socialaccount",
    #r"django_app\static",
]

def should_exclude_path(path):
    """
    Check if a given path should be excluded based on user-defined exclusion paths.
    """
    for exclude_path in USER_EXCLUDE_PATHS:
        if exclude_path in path:
            return True
    return False

def list_files(base_path):
    """
    Walk through the Django project directory and return a list of all important files.
    """
    project_files = []
    for root, dirs, files in os.walk(base_path):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        # Exclude based on user-defined paths
        if should_exclude_path(root):
            print(f"Skipping excluded path: {root}")
            continue

        for file in files:
            if any(file.endswith(ext) for ext in CODE_EXTENSIONS):
                project_files.append(os.path.join(root, file))
    return project_files

def pack_files(file_paths, output_file):
    """
    Pack the list of files into a single text file with structure markers.
    """
    with open(output_file, "w", encoding="utf-8") as packed_file:
        # Header Section
        packed_file.write(f"Repopack Django Output File\n")
        packed_file.write(f"Generated on: {datetime.now()}\n\n")
        
        packed_file.write("Repository Structure\n")
        packed_file.write("="*40 + "\n")
        
        for path in file_paths:
            packed_file.write(f"{os.path.relpath(path)}\n")
        packed_file.write("\n")

        # File Content Section
        packed_file.write("="*40 + "\n")
        for path in file_paths:
            packed_file.write(f"File: {os.path.relpath(path)}\n")
            packed_file.write("="*40 + "\n")

            with open(path, "r", encoding="utf-8") as file_content:
                packed_file.write(file_content.read())
            
            packed_file.write("\n" + "="*40 + "\n")

if __name__ == "__main__":
    project_path = input("Enter the path to your Django project: ")
    output_file = "django_code.txt"

    print("Scanning project files...")
    project_files = list_files(project_path)

    print(f"Packing {len(project_files)} files into {output_file}...")
    pack_files(project_files, output_file)

    print(f"Packed repository saved to {output_file}")
