import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, destination_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Check if destination directory exists; if not, create it
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)

        # Check if the file already exists in the destination directory
        if os.path.exists(destination_file):
            # Append a timestamp to the filename to ensure uniqueness
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            name, ext = os.path.splitext(filename)
            destination_file = os.path.join(destination_dir, f"{name}_{timestamp}{ext}")

        # Copy the file to the destination directory
        try:
            shutil.copy2(source_file, destination_file)
            print(f"Copied '{filename}' to '{destination_file}'")
        except Exception as e:
            print(f"Error copying '{filename}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)