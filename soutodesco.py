import os
import sys
import shutil
import datetime

def backup_files(source_dir, dest_dir):
    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist.")
            return

        # Create destination directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)

        # Iterate through files in the source directory
        for filename in os.listdir(source_dir):
            src_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)

            # Append timestamp to the destination file name if it already exists
            if os.path.exists(dest_path):
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                base_name, ext = os.path.splitext(filename)
                new_filename = f"{base_name}_{timestamp}{ext}"
                dest_path = os.path.join(dest_dir, new_filename)

            # Copy the file
            shutil.copy2(src_path, dest_path)
            print(f"Copied '{filename}' to '{dest_path}'")

        print("Backup completed successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)