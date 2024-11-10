import os
import subprocess
import argparse

from utils import create_c_project_structure, create_ml_project_structure, create_shortcut

def cli():
    parser = argparse.ArgumentParser(description="Generate an ML project structure.")
    parser.add_argument("project_path", type=str, help="Path where the project will be created.")
    parser.add_argument("--git", action="store_true", help="Initialize a Git repository in the project directory.")
    parser.add_argument("--extra_dirs", type=str, nargs="*", default=[], help="Additional directories to create.")
    parser.add_argument("--extra_files", type=str, nargs="*", default=[], help="Additional files to create.")
    parser.add_argument("--alias_name", type=str, default="mlproj", help="Name of the alias for the project directory.")
    parser.add_argument("--headers", type=str, nargs="*", default=[], help="Additional files to create.")
    parser.add_argument("--lang", type=str, default="py", help="Specify project type: py, c, cpp, ml")
    args = parser.parse_args()

    # Create project structure
    if args.lang == "ml":
        create_ml_project_structure(
            project_path=args.project_path,
            init_git=args.git,
            extra_dirs=args.extra_dirs,
            extra_files=args.extra_files
        )
    elif args.lang == "c":
        create_c_project_structure(
            project_path=args.project_path,
            init_git=args.git,
            extra_dirs=args.extra_dirs,
            extra_files=args.extra_files,
            headers=args.headers
        )
    
    if args.alias_name:
        create_shortcut(args.project_path, alias_name=args.alias_name)

if __name__ == "__main__":
    cli()
