# import os
# import re
#
#
# def rename_one_piece_episodes(folder_path):
#     """
#     Renames One Piece episode files in a given folder to a new format.
#     Example: "[@AniPlus] One Piece - 1080p هاردساب - Ep884" becomes "One Piece - Ep884"
#     """
#     # Check if the provided path is a valid directory
#     if not os.path.isdir(folder_path):
#         print(f"Error: Folder not found at '{folder_path}'")
#         return
#
#     print(f"Scanning folder: '{folder_path}'")
#
#     # Get all files in the directory
#     try:
#         files = os.listdir(folder_path)
#     except OSError as e:
#         print(f"Error accessing folder contents: {e}")
#         return
#
#     # Sort files to process them in order (optional, but good for consistency)
#     files.sort()
#
#     count = 0
#     # Iterate over each file in the directory
#     for filename in files:
#         # Construct the full path for the old file
#         old_file_path = os.path.join(folder_path, filename)
#
#         # Check if it's actually a file (and not a subdirectory)
#         if os.path.isfile(old_file_path):
#             # Regex to find the episode number.
#             # This regex looks for "Ep" or "Episode" (case-insensitive)
#             # followed by optional space/dot, and then one or more digits.
#             # It captures the digits in group 1.
#             match = re.search(r'[Ee]p(?:isode)?[\s.]*(\d+)', filename)
#
#             if match:
#                 episode_number = match.group(1) # The captured digits
#
#                 # Construct the new filename based on the desired format "One Piece - Ep[number]"
#                 # We use the extracted episode_number directly.
#                 new_filename_base = f"One Piece - Ep{episode_number}"
#
#                 # Get the original file extension (e.g., '.mp4', '.mkv')
#                 _, file_extension = os.path.splitext(filename)
#
#                 # Construct the full new file path with the original extension
#                 new_file_path = os.path.join(folder_path, new_filename_base + file_extension)
#
#                 # Rename the file if the new name is different from the old one
#                 if old_file_path != new_file_path:
#                     try:
#                         os.rename(old_file_path, new_file_path)
#                         print(f"Renamed: '{filename}' -> '{new_filename_base + file_extension}'")
#                         count += 1
#                     except OSError as e:
#                         print(f"Error renaming '{filename}' to '{new_filename_base + file_extension}': {e}")
#                 # else:
#                 #     print(f"Skipping '{filename}': Already in the correct format.")
#             # else:
#                 # Uncomment the line below if you want to see which files are skipped because they don't match the pattern
#                 # print(f"Skipping '{filename}': Pattern not found.")
#
#
#     # Print a summary message
#     if count > 0:
#         print(f"\nSuccessfully renamed {count} files.")
#     else:
#         print(
#             "\nNo files were renamed. Please ensure:")
#         print(f"- The folder path is correct: '{folder_path}'")
#         print("- Files in the folder contain episode numbers in a recognizable format (e.g., 'Ep884', 'Episode 884').")
#         print("- You have the necessary permissions to rename files in that folder.")
#
#
# # --- Configuration ---
# # !!! IMPORTANT: Replace this with the actual path to your One Piece episodes folder !!!
# # Use a raw string (r"...") for Windows paths to handle backslashes correctly.
# # Example for Windows: folder_path = r"C:\Users\ASUS\Desktop\test NAME"
# # Example for macOS/Linux: folder_path = "/Users/YourUsername/Videos/One Piece"
# folder_path = r"E:\Hard,Movie\ONE PICE"
# # --- End Configuration ---
#
# # Run the renaming function with the specified folder path
# rename_one_piece_episodes(folder_path)
#######################################################
import os
import re


def rename_one_piece_episodes(folder_path):
    # Regex که هم قسمت‌های با Ep و هم قسمت‌هایی که فقط شماره دارند را پیدا می‌کند
    # این regex سعی می‌کند عدد را بعد از "One Piece" یا بعد از "Ep" پیدا کند.
    pattern = re.compile(r'One Piece.*?([Ee]p)?[\s-]*(\d+).*?$', re.IGNORECASE)

    for filename in os.listdir(folder_path):
        match = pattern.search(filename)
        if match:
            episode_number_str = match.group(2)

            if episode_number_str:
                try:
                    episode_number = int(episode_number_str)

                    # فرمت دهی شماره قسمت: اگر کمتر از 1000 بود، سه رقمی با صفر پر می شود.
                    # اعداد بزرگتر از 999 (مثل 1141) همانطور نمایش داده می شوند.
                    if episode_number < 1000:
                        formatted_episode_number = f"{episode_number:03d}"
                    else:
                        formatted_episode_number = str(episode_number)

                    # استخراج پسوند فایل
                    file_base, file_extension = os.path.splitext(filename)

                    # ساخت نام جدید فایل
                    new_filename = f"One Piece - Ep{formatted_episode_number}{file_extension}"

                    old_file_path = os.path.join(folder_path, filename)
                    new_file_path = os.path.join(folder_path, new_filename)

                    # اطمینان از اینکه نام جدید با نام فعلی متفاوت است تا از تغییر نام بی مورد جلوگیری شود
                    if filename != new_filename:
                        print(f"تغییر نام: '{filename}' به '{new_filename}'")
                        os.rename(old_file_path, new_file_path)
                    else:
                        print(f"نام فایل '{filename}' از قبل درست است.")

                except ValueError:
                    print(f"خطا: شماره قسمت '{episode_number_str}' در فایل '{filename}' قابل تبدیل به عدد نیست.")
                except Exception as e:
                    print(f"خطا در پردازش فایل '{filename}': {e}")
            else:
                print(f"شماره قسمتی در الگوی نام فایل '{filename}' یافت نشد.")
        else:
            # اگر فایلی با الگوی مورد نظر مطابقت نداشت، آن را نادیده می گیریم یا پیام می دهیم
            print(f"فایل '{filename}' با الگوی مورد نظر مطابقت ندارد و تغییر نام داده نشد.")


# مسیر پوشه را اینجا قرار دهید
folder_to_process = r"E:\Hard,Movie\ONE PICE"
rename_one_piece_episodes(folder_to_process)






















