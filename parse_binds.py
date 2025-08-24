import xml.etree.ElementTree as ET
import csv
import os
import sys

def parse_binds_file(input_file, output_file):
    # Parse the XML file
    try:
        tree = ET.parse(input_file)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        return

    # List to store the keybind data
    keybinds = []

    # Iterate through all elements in the XML
    for element in root:
        action = element.tag
        notes = []

        # Initialize binding details
        device = ""
        input_key = ""
        is_toggle = False
        is_hold = False
        is_inverted = False
        deadzone = ""
        binding_type = ""  # Primary, Secondary, or Axis
        modifiers = []

        # Check for axis bindings (e.g., <Binding Device="..." Key="...">)
        binding = element.find("Binding")
        if binding is not None:
            device = binding.get("Device", "")
            input_key = binding.get("Key", "")
            binding_type = "Axis"
            # Check for Inverted and Deadzone
            inverted = element.find("Inverted")
            if inverted is not None and inverted.get("Value") == "1":
                is_inverted = True
                notes.append("Inverted")
            deadzone_elem = element.find("Deadzone")
            if deadzone_elem is not None and deadzone_elem.get("Value") != "0.00000000":
                deadzone = f"Deadzone: {float(deadzone_elem.get('Value')):.4f}"
                notes.append(deadzone)

        # Check for Primary and Secondary bindings
        primary = element.find("Primary")
        secondary = element.find("Secondary")
        if primary is not None and primary.get("Device") != "{NoDevice}":
            device = primary.get("Device", "")
            input_key = primary.get("Key", "")
            binding_type = "Primary"
            # Check for modifiers in Primary binding
            for mod in primary.findall("Modifier"):
                mod_device = mod.get("Device", "")
                mod_key = mod.get("Key", "")
                if mod_device and mod_key:
                    modifiers.append(f"{mod_device}: {mod_key}")
            # Check for Hold attribute
            if primary.get("Hold") == "1":
                is_hold = True
                notes.append("Hold")
        elif secondary is not None and secondary.get("Device") != "{NoDevice}":
            device = secondary.get("Device", "")
            input_key = secondary.get("Key", "")
            binding_type = "Secondary"
            notes.append("Secondary binding")
            # Check for modifiers in Secondary binding
            for mod in secondary.findall("Modifier"):
                mod_device = mod.get("Device", "")
                mod_key = mod.get("Key", "")
                if mod_device and mod_key:
                    modifiers.append(f"{mod_device}: {mod_key}")
            # Check for Hold attribute
            if secondary.get("Hold") == "1":
                is_hold = True
                notes.append("Hold")

        # Check for ToggleOn
        toggle = element.find("ToggleOn")
        if toggle is not None and toggle.get("Value") == "1":
            is_toggle = True
            notes.append("Toggle")

        # Add context for specific modes (e.g., Buggy, Humanoid)
        if "Buggy" in action:
            notes.append("SRV")
        elif "MultiCrew" in action:
            notes.append("MultiCrew")
        elif "_Humanoid" in action:
            notes.append("On-Foot")
            
        # Add modifiers to notes if any
        if modifiers:
            notes.append(f"Modifiers: {', '.join(modifiers)}")

        # Only include actions with valid bindings
        if device and input_key:
            keybinds.append({
                "Action": action,
                "Device": device,
                "Input": input_key,
                "Notes": ", ".join(notes) if notes else ""
            })

    # Write to CSV
    try:
        with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Action", "Device", "Input", "Notes"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for bind in keybinds:
                writer.writerow(bind)
        print(f"CSV file successfully written to {output_file}")
    except Exception as e:
        print(f"Error writing CSV file: {e}")

def main():
    inputs = sys.argv
    # Example usage
#    input_file = input("Enter the path to your .binds XML file: ")  # e.g., "SOLCustom.binds"
#    output_file = input("Enter the output CSV file name (e.g., keybinds.csv): ")  # e.g., "keybinds.csv"

#    if len(sys.argv) > 1:   
    input_file = sys.argv[1]  # First argument
    output_file = sys.argv[2]
#    else:   
#    input_file = None  # No argument provided 
 
    # Ensure the output file has a .csv extension
    if not output_file.endswith(".csv"):
        output_file += ".csv"
    
    parse_binds_file(input_file, output_file)

if __name__ == "__main__":
    main()
