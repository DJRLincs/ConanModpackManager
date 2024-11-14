# ConanModpackManager by DJRLincs

**ConanModpackManager** is a simple, flexible script for managing multiple mod configurations in Conan Exiles. It allows players and server admins to easily switch between mod collections, automatically updating the `modlist.txt` with the correct paths and selected modpacks.

## Features

- **Switch Between Modpacks**: Quickly change mod collections by selecting the desired modpack configuration.
- **Automatic Path Configuration**: Updates mod paths in `modlist.txt` based on the selected modpack.
- **Configurable Installation Directory**: Remembers the Conan Exiles installation directory for future use.
- **User-Friendly**: Console-based prompts guide you through each step of the setup and modpack selection.

## Requirements

- **Python**: Make sure Python 3.x is installed on your system.
- **Conan Exiles**: Ensure Conan Exiles is installed and that you know its installation path.

## Installation

1. **Download the zip**:
   https://github.com/DJRLincs/ConanModpackManager/releases
   
2. **Put it into a folder**:
   find the folder you want to use it in and unzip
   
3. **Run the Script**:
   run the .bat file.
   

## Usage

1. **First Run**:
   - The script will prompt you to enter your Conan Exiles installation directory. This will be saved in a `config.json` file so you don’t need to enter it again.
   - After creating the modpacks folder, run the script a second time to set up your modlist files.

2. **Selecting a Modpack**:
   - Place your modpack `.txt` files in the `ConanSandbox/Mods/modpacks` folder. Each file should list the mods you want in the modpack.
   - Run the script and select the desired modpack by entering its corresponding number.
   - The `modlist.txt` file in the `ConanSandbox/Mods` folder will be updated with the correct mod paths based on your selected modpack.

3. **Switching Modpacks**:
   - Rerun the script and select a different modpack to switch configurations easily.

## Configuration

The `config.json` file stores the Conan Exiles installation directory you provide during the first run. If you need to change the directory, delete `config.json` and rerun the script to re-enter the directory.

## Example

1. **Running the Script**:
   ```plaintext
   ConanModpackSelector by DJRLincs
   ***Warning***
   Please note that this script will overwrite your modlist.txt file in the main ConanSandbox/Mods folder.
   It does not download the workshop items for you.
   
   **If this is the first time you are running this script, you will need to run it again after it creates the modpack
   folder in your Mods directory and places the modlist files in the modpack folder.**
   
   Press Enter to continue...
   ```
   
2. **Selecting a Modpack**:
   ```plaintext
   Available modpacks:
   1. PVE_Setup
   2. PVP_Setup
   Enter the number of the modpack you want to use: 1
   Modlist.txt has been updated with the correct workshop content directory.
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! If you’d like to improve this script, please fork the repository and submit a pull request.

## Disclaimer
This script does not handle the download or installation of mods. Ensure you have all necessary mods downloaded in your Steam Workshop content folder.
