# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 21:14:28 2023

@author: Kiarash Rahmani
"""

import os

def rename_files(folder_path, start_number, end_number):
    file_list = os.listdir(folder_path)

    for i, filename in enumerate(file_list, start=start_number):
        file_extension = os.path.splitext(filename)[1].lower()

        if file_extension in {'.jpg', '.jpeg'}:
            new_filename = os.path.join(folder_path, f"{i}.jpg")
        else:
            new_filename = os.path.join(folder_path, f"{i}{file_extension}")

        try:
            old_file_path = os.path.join(folder_path, filename)
            os.rename(old_file_path, new_filename)
        except FileNotFoundError:
            print(f"File {old_file_path} not found.")
        except FileExistsError:
            print(f"File {new_filename} already exists.")
        except Exception as e:
            print(f"Error occurred while renaming file {old_file_path}: {e}")

if __name__ == "__main__":
    folder_path = r"C:/Users/Kiarash Rahmani/Desktop/IELTS"
    start_number = 1
    end_number = 50
    rename_files(folder_path, start_number, end_number)
   