from pathlib import Path

def get_unique_filename(base_path):
    base_path = Path(base_path)
    file_stem = base_path.stem
    file_suffix = base_path.suffix
    directory = base_path.parent
    
    counter = 1
    new_path = base_path
    
    # Loop until a unique filename is found
    while new_path.exists():
        new_path = directory / f"{file_stem}_{counter}{file_suffix}"
        counter += 1
    
    return new_path