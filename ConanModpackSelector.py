import os
import shutil
import re
import json
import subprocess

config_path = "config.json"
steamcmd_dir = "steamcmd"
steamcmd_executable = os.path.join(steamcmd_dir, "steamcmd.exe")

def save_config(conan_dir):
    with open(config_path, "w") as config_file:
        json.dump({"conan_dir": conan_dir}, config_file)

def load_config():
    if os.path.exists(config_path):
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            return config.get("conan_dir")
    return None

def download_steamcmd():
    if not os.path.exists(steamcmd_dir):
        os.makedirs(steamcmd_dir)
    if not os.path.isfile(steamcmd_executable):
        print("Downloading SteamCMD...")
        url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip"
        zip_path = os.path.join(steamcmd_dir, "steamcmd.zip")
        os.system(f"curl -o {zip_path} {url}")
        shutil.unpack_archive(zip_path, steamcmd_dir)
        os.remove(zip_path)
        print("SteamCMD downloaded.")

def download_mod(mod_id):
    print(f"Downloading mod with ID: {mod_id}")
    subprocess.run([steamcmd_executable, "+login", "anonymous", "+workshop_download_item", "440900", mod_id, "+quit"])

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

# Extract mod IDs from modlist.txt, only capturing the digits after "440900/" or "440900\"
mod_ids = re.findall(r"440900[\\/](\d+)", content)

# Prompt user to decide whether to download mods or not
download_choice = input("Do you want to download the mods via SteamCMD? (yes/no): ").strip().lower()

# Download SteamCMD and mods only if the user chose to download
if download_choice == "yes":
    download_steamcmd()
    for mod_id in mod_ids:
        mod_path = os.path.join(workshop_content_dir, mod_id)
        if not os.path.exists(mod_path):
            download_mod(mod_id)
        else:
            print(f"Mod {mod_id} already downloaded; skipping download.")
    print("All listed mods have been downloaded and configured.")
else:
    print("Mod download skipped. Mods listed in the modlist.txt file have been configured.")
