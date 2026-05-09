import os
import subprocess
import re

input_dir = "videos"
output_dir = "audios"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if not file.lower().endswith((".mp4", ".mkv", ".avi", ".mov")):
        continue

    try:
        # Extract tutorial number (e.g., 2)
        match_num = re.search(r'Tutorial\s+#(\d+)', file)
        tutorial_number = match_num.group(1) if match_num else "unknown"

        # Extract clean title (after .mp4_)
        title_part = file.split(".mp4_")[-1]

        # Remove everything after double space or " Sigma"
        title = title_part.split("  ")[0].split(" Sigma")[0]

        # Clean invalid filename chars
        title = re.sub(r'[\\/*?:"<>|]', "", title).strip()

        output_file = f"{tutorial_number}_{title}.mp3"

        print(output_file)

        subprocess.run([
            "ffmpeg",
            "-i", os.path.join(input_dir, file),
            "-vn",
            os.path.join(output_dir, output_file)
        ], check=True)

    except Exception as e:
        print(f"Error processing {file}: {e}")