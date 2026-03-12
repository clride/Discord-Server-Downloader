import os
import argparse

from dotenv import load_dotenv
from src.downloader import DiscordDownloader

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
                        prog='Discord Server Downloader',
                        description='Dowloads your discord servers and channels',
                        epilog='')

    parser.add_argument('-d', '--download-path', type=str, help='Custom download path')
    parser.add_argument('-t', '--token', type=str, help='Discord bot token')

    args = parser.parse_args()

    args.download_path = args.download_path if args.download_path else None
    args.token = args.token if args.token else None

    key = args.token or os.getenv("DISCORD_BOT_TOKEN")

    if not key:
        print("[ERROR] No token provided. Use the -t [TOKEN] argument or provide it via .env file.")
        exit()

    loggeduser = os.getlogin()

    if os.name == 'nt':  # Windows
        path = f"C:\\Users\\{loggeduser}\\Downloads"
    elif os.name == 'posix':  # Linux or macOS
        path = f"/home/{loggeduser}/Downloads"

    if not args.download_path:
        print(f"No download path provided, using default: {path}")

    path = args.download_path or path

    downloader = DiscordDownloader(key, path)
    downloader.run()

if __name__ == "__main__":
    main()