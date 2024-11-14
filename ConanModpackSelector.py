import os
import shutil
import re
import json

config_path = "config.json"

def save_config(conan_dir):
    with open(config_path, "w") as config_file:
        json.dump({"conan_dir": conan_dir}, config_file)

def load_config():
    if os.path.exists(config_path):
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            return config.get("conan_dir")
    return None

print("Conan Modpack Selector by DJRLincs\n***Warning***\n")
print("Please note that this script will overwrite your modlist.txt file in the main ConanSandbox/Mods folder.")
print("It does not download the workshop items for you.\n")
print("**If this is the first time you are running this script, you will need to run it again after it creates the modpack")
print("folder in your Mods directory and places the modlist files in the modpack folder named**\n")
input("Press Enter to continue...")

# Load the Conan Exiles directory from config if it exists; otherwise, prompt the user for it
conan_dir = load_config()
if not conan_dir:
    conan_dir = input("Enter the full Conan Exiles installation directory (e.g., E:\\Program Files (x86)\\Steam\\steamapps\\common\\Conan Exiles): \n")
    save_config(conan_dir)

# Determine the base Steam directory by stripping out everything after "steamapps"
steam_dir = conan_dir.split("common")[0].strip("\\")
workshop_content_dir = os.path.join(steam_dir, "workshop", "content", "440900")

# Normalize the workshop path to use forward slashes
workshop_content_dir = workshop_content_dir.replace("\\", "/")

# Navigate to the Mods folder
mods_dir = os.path.join(conan_dir, "ConanSandbox", "Mods")
modpacks_dir = os.path.join(mods_dir, "modpacks")

# Create the modpacks folder if it doesn't exist
if not os.path.exists(modpacks_dir):
    os.makedirs(modpacks_dir)

# List available modpacks
modpacks = [f for f in os.listdir(modpacks_dir) if f.endswith(".txt")]
print("Available modpacks:")
for i, modpack in enumerate(modpacks):
    print(f"{i+1}. {modpack[:-4]}")

# Prompt the user to select a modpack
selected_index = int(input("Enter the number of the modpack you want to use: "))
selected_modpack = modpacks[selected_index - 1]

# Copy the selected modpack's modlist.txt file to the main Mods folder
src_path = os.path.join(modpacks_dir, selected_modpack)
target_path = os.path.join(mods_dir, "modlist.txt")
shutil.copy(src_path, target_path)

# Read and update the modlist.txt file in the main Mods folder
with open(target_path, "r") as f:
    content = f.read()

# Replace any path prefix before "440900" with the selected workshop content directory
pattern = r".*?[/\\]440900"
content = re.sub(pattern, workshop_content_dir, content)

# Write the updated content back to the modlist.txt file
with open(target_path, "w") as f:
    f.write(content)

print("modlist.txt has been updated for Conan with the correct workshop content directory also put in place.")
