(by Grok)

# binds_parser
Reads ED aka Elite Dangerous keyboard, HOTAS, HOTA binds file and generates a CSV file 

# How to Use the Script

Prerequisites:Ensure you have Python installed (version 3.6 or higher recommended). You can download it from python.org.
No additional libraries are required, as the script uses standard Python modules (xml.etree.ElementTree and csv).

The script works with any Elite Dangerous .binds file structure.

# Run the Script:

Open a terminal or command prompt.

Navigate to the directory containing the script using cd /path/to/directory.

Run the script with: 
```
$ python parse_binds.py SOLCustom.binds output.csv
```
Include the path to your .binds file (e.g., MyCustom.binds or /path/to/EDdirectory/MyCustom.binds).

Include the desired output CSV file name (e.g., keybinds.csv). If you don’t specify .csv, it will be added automatically.

Output:The script generates a CSV file (e.g., keybinds.csv) in the same directory as the script.

The CSV will contain columns: Action, Device, Input, and Notes, similar to the table I provided earlier.

Open the CSV in spreadsheet software (e.g., LibreOffice) or a text editor to view the keybind mappings.

# Features 

The ScriptParses XML Structure: Extracts all actions with assigned bindings (Primary, Secondary, or Axis) from the .binds file.

Handles Modifiers: Captures modifier keys (e.g., LeftControl, LeftAlt) for keyboard bindings.

Includes Notes: Adds details like "Inverted", "Deadzone", "Toggle", "Hold", "Secondary binding", and context (e.g., SRV, MultiCrew, On-Foot).

Filters Unmapped Actions: Skips actions with {NoDevice} and empty keys to keep the output concise.

Flexible Output: Writes to a CSV file that’s easy to read and manipulate.

Error Handling: Includes basic error handling for invalid XML or file issues.

# Example Usage

If your .binds file is located at /home/yourname/blah/Custom.binds and you want to output to keybinds.csv 

Run the script: 
```
python parse_binds.py SOLCustom.binds output.csv
```

The script will create keybinds.csv in the same directory as the script, containing the keybind table.

# Customization Options

If you want to modify the script for specific needs, here are some suggestions:

Filter by Context: Add a filter to include only specific contexts (e.g., only SRV bindings). Modify the if device and input_key block to check for specific action suffixes (e.g., _Buggy).

Sort Output: Sort the keybinds list by Action, Device, or Input before writing to CSV using sorted(keybinds, key=lambda x: x['Device']).

Different Output Format: Change the output to JSON or plain text by modifying the write section (e.g., use json.dump for JSON).

Command-Line Arguments: Replace the input() prompts with command-line arguments using argparse for automation.

Let me know if you need help running the script, want a modified version (e.g., with filtering or a different output format), or need assistance with Python setup!

