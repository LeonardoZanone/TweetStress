from common import get_current_folder_path, create_folder_structure
from constants import PROCESSED_FILES, RAW_FILES, WRITING_FILES

def create_folders():
    current_path = get_current_folder_path()
    create_folder_structure(f"{current_path}/{WRITING_FILES}")
    create_folder_structure(f"{current_path}/{RAW_FILES}")
    create_folder_structure(f"{current_path}/{PROCESSED_FILES}")

def main():
    print("Creating folder structure")
    create_folders()
    print("Successfully created folders")    

if __name__ == "__main__":
    main()