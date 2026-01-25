import argparse

def main(navall_filepath, out_dir):
    # Check if NAVAll file exists
    try:
        with open(navall_filepath, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"NAVAll file not found: {navall_filepath}")
        return

    # Create output directory if it doesn't exist
    import os
    os.makedirs(out_dir, exist_ok=True)

    # Parse the NAVAll file and create a mapping of scheme codes to scheme names
    scheme_mappings = {}
    for line in lines[1:]:  # Skip header line
        parts = line.strip().split(';')
        if len(parts) >= 2:
            scheme_code = parts[0].strip()
            scheme_name = parts[3].strip()
            scheme_mappings[scheme_code] = scheme_name

    # dump dict to JSON file
    import json
    json_filepath = os.path.join(out_dir, "scheme_mappings.json")
    with open(json_filepath, 'w') as json_file:
        json.dump(scheme_mappings, json_file, indent=4)
    print(f"Scheme mappings saved to {json_filepath}")

if __name__ == "__main__":
    # Use argparse to handle command-line args
    parser = argparse.ArgumentParser(description="Mutual Fund Scheme Code Data Handling")
    parser.add_argument("-N", "--navall-filepath", type=str, help="Filepath containing NAVAll data", default="NAVAll.TXT")
    parser.add_argument("-O", "--out-dir", type=str, help="Directory to store output file", default="./")
    args = parser.parse_args()
    
    main(args.navall_filepath, args.out_dir)