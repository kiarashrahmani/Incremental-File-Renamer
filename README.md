# IncrementalFileRenamer

The **IncrementalFileRenamer** script is a Python program designed to simplify the process of renaming files within a specified folder path. It offers a user-friendly way to organize files, particularly images, by renaming them in a sequential manner. This script can be useful for various scenarios where file organization and renaming are required.

## Features

- **Incremental Renaming:** The script iterates through files in the designated folder, starting from a specified start number and ending at a defined end number. It increments the numeric part of filenames while retaining their original file extensions.

- **Image File Handling:** Image files with extensions `.jpg` and `.jpeg` are detected and renamed following the pattern `1.jpg`, `2.jpg`, and so on. Non-image files keep their original extensions intact.

- **Error Management:** The script includes comprehensive error handling to account for potential issues such as missing files or filename conflicts. Informative messages are displayed for each error scenario.

- **Custom Configuration:** Users can easily configure the script by modifying the `folder_path`, `start_number`, and `end_number` parameters. This allows for flexibility in choosing the source folder for renaming and specifying the numeric range for new filenames.

## Usage

1. Ensure you have Python installed on your system.

2. Download or clone the `IncrementalFileRenamer.py` script to your local directory.

3. Open the script in a text editor or integrated development environment (IDE).

4. Modify the `folder_path`, `start_number`, and `end_number` variables according to your requirements.

5. Run the script. It will automatically rename the files within the specified range, adhering to the defined naming pattern.

## Example

Suppose you have a folder named "Images" containing image files and other documents. You want to organize the image files with sequential names while leaving the other files unchanged. By configuring the script with the appropriate parameters, you can easily achieve this organization in no time.

## Contribution

Contributions to the **IncrementalFileRenamer** script are welcome! If you find ways to enhance its functionality or improve the user experience, feel free to fork the repository and submit your changes via a pull request.

## License

This script is provided under the [MIT License](LICENSE). Feel free to use, modify, and distribute it according to the terms of the license.

---
*Author: Kiarash Rahmani*

