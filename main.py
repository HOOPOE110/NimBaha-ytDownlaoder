import subprocess
from tqdm import tqdm
from playwrightdl import nimbahaurl
import asyncio
from colorama import Fore, Back, Style
import time
import os
import sys
import io

os.system("chcp 65001")  # UTF-8 code page
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def format_id(video_url,option):
    # Build the command to list formats in a machine-readable JSON format
    command = [
        "yt-dlp",
        "--dump-json",
        "--no-warnings",
        video_url
    ]

    try:
        # Run the command and capture the output
        # result = subprocess.run(
        #     command,
        #     capture_output=True,
        #     text=True,
        #     check=True
        # )

        import yt_dlp

        ydl_opts = {
            "quiet": True,  # suppress output
            "no_warnings": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(video_url, download=False)

        # Parse the JSON output
        # video_info = json.load(video_info)
        # print(video_info)
        formats = video_info.get("formats", [])

        # Print the available formats
        tqdm.write(Fore.GREEN + f"Available formats for video: {Style.RESET_ALL} {Fore.MAGENTA} {video_info.get('title')}\n" + Style.RESET_ALL)

        if option == 2 or option == 3:
            tqdm.write(Fore.GREEN + 'Audio_Files: ' + Style.RESET_ALL)
            tqdm.write(Back.LIGHTBLACK_EX +'-------------------------------' + Style.RESET_ALL)
            for f in formats:
                # Check if resolution is available before trying to print it.
                # This prevents the program from crashing if a format doesn't have a resolution.
                if "filesize" in f and f["resolution"] == 'audio only':
                    tqdm.write(
                        f"Format Code: {Fore.MAGENTA} {f['format_id']} {Style.RESET_ALL} , Resolution: {Fore.YELLOW} {f['resolution']} {Style.RESET_ALL} , Quallity : {Fore.BLUE} {f['tbr']} {Style.RESET_ALL} ,Extension: {f['ext']}, {Fore.LIGHTRED_EX} Filesize: {Style.RESET_ALL} {Fore.CYAN} {int(f['filesize']) / 1000000:.2f}MB {Style.RESET_ALL}" if f['filesize'] else 'None')
        if option == 1 or option == 3:
            tqdm.write(Fore.GREEN + 'Video_Files: ' + Style.RESET_ALL)
            tqdm.write(Back.LIGHTBLACK_EX +'-------------------------------' + Style.RESET_ALL)
            for f in formats:
                if "filesize" in f and f["resolution"] != 'audio only':
                    tqdm.write(
                        f"Format Code: {Fore.MAGENTA} {f['format_id']} {Style.RESET_ALL} , Resolution: {Fore.YELLOW} {f['resolution']} {Style.RESET_ALL} , Quallity : {Fore.BLUE} {f['tbr']} {Style.RESET_ALL} ,Extension: {f['ext']}, {Fore.LIGHTRED_EX} Filesize: {Style.RESET_ALL} {Fore.CYAN} {int(f['filesize']) / 1000000:.2f}MB {Style.RESET_ALL}" if f['filesize'] else 'None')



    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"Stderr: {e.stderr}")
        return 'error'
    except FileNotFoundError:
        print("Error: 'yt-dlp' command not found. Make sure it's installed and in your system's PATH.")
        return 'error'
    finally:
        return video_info

def get_url(vidid,audid,video_info):
    # Build the command to list formats in a machine-readable JSON format
    # command = [
    #     "yt-dlp",
    #     "--dump-json",
    #     "--no-warnings",
    #     video_url
    # ]

    try:
    #     # Run the command and capture the output
    #     result = subprocess.run(
    #         command,
    #         capture_output=True,
    #         text=True,
    #         check=True
    #     )

        # Parse the JSON output
        # video_info = json.loads(result.stdout)
        # print(video_info)
        formats = video_info.get("formats", [])

        # Print the available formats
        print(f"Gathering URL for video: '{video_info.get('title')}' , Video_ID : {vidid} and Audio_ID : {audid}\n")
        for f in formats:
            # Check if resolution is available before trying to print it.
            # This prevents the program from crashing if a format doesn't have a resolution.
            if f['format_id'] == vidid or f['format_id'] == audid :
                print(Fore.CYAN + 'Selected Option --------------->' + Style.RESET_ALL)
                print(
                    f"Format Code: {f['format_id']}, Resolution: {f['resolution']}, Quallity : {f['tbr']} Extension: {f['ext']}, Filesize: {int(f['filesize']) / 1000000 if f['filesize'] is not None else 'None'}MB")
            # else:
            #     print(f"Format Code: {f['format_id']}, Extension: {f['ext']}, Note: {f['format_note']}")

            if f['format_id'] == vidid:
                vid_url = f['url']
                vid_ext = f['ext']
                title = video_info.get('title')

            if f['format_id'] == audid:
                aud_url = f['url']
                aud_ext = f['ext']

        return vid_url , aud_url , vid_ext, aud_ext , title
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"Stderr: {e.stderr}")
        vid_url = None
        return vid_url
    except FileNotFoundError:
        print("Error: 'yt-dlp' command not found. Make sure it's installed and in your system's PATH.")
        vid_url = None
        return vid_url


while True:
    # print(Fore.GREEN + "Cheking if you have ffmpeg..." + Style.RESET_ALL)
    #
    # import os
    # if not os.path.exists("ffmpeg"):
    #     print(Fore.CYAN + "ffmpeg.exe not found your app files are not complete" + Style.RESET_ALL)
    #     break

    #     from ffmpeg_unarchive import ffmpeg_unarchive
    #     try:
    #         ffmpeg_unarchive()
    #         print("ffmpeg.exe unarchived")
    #     except Exception as e:
    #         print("Error Occurred: ", e)
    #         break

    if not os.path.exists("outputs"):
        os.makedirs("outputs", exist_ok=True)

    print("""⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀ 
⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀ 
⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀ 
⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀ 
⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀ 
⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀Note:⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀ 
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀Turn On VPN⠀⠀⠀⢸⣿⣿⠀⠀ 
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀This is YT⠀⠀⠀⠀⢸⣿⣿⠀⠀ 
⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀Not Aparat⠀⠀⠀⠀⢸⣿⡇⠀⠀ 
⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀ 
⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")


    video_url = input(Fore.GREEN + "Enter video url: " + Style.RESET_ALL)

    print(Fore.CYAN + "1. Video Only " + Style.RESET_ALL)
    print(Fore.CYAN + "2. Audio Only " + Style.RESET_ALL)
    print(Fore.CYAN + "3. Both " + Style.RESET_ALL)
    option = int(input(Fore.GREEN + "Enter Option Number : " + Style.RESET_ALL))
    if option >= 4 or option <= 0:
        print("Invalid Option , Try again")
        time.sleep(5)
        break


    print(Back.MAGENTA + 'Please wait...' + Style.RESET_ALL)


    try:
        video_info = format_id(video_url,option)

        if video_info == 'error':
            print(Fore.RED + "Error occurred. maybe you entered wrong url" + Style.RESET_ALL)
            time.sleep(5)
            break

    except Exception as e:
        print(f"An error occurred. Please try again later. Maybe your IP is Iranian🤡 | {e}")
        time.sleep(5)
        break

    print(Fore.RED + "For Better Performance And Maybe For Getting No Errors , You Can Turn OFF Your VPN Now!" + Style.RESET_ALL)
    print(
        Fore.CYAN + "Choose Both of Your Formats Webm or Video mp4 and Audio m4a For More Efficient Process! " + Style.RESET_ALL)
    if option == 1 or option == 3:
        vidid = input(Fore.GREEN +"Enter your Video Format ID: "+ Style.RESET_ALL)
    if option == 2 or option == 3:
        audid = input(Fore.MAGENTA + "Enter your Audio Format ID: "+ Style.RESET_ALL)
    if option == 2:
        vidid = None
    if option == 1:
        audid = None

    print(Fore.CYAN + 'Please wait again...' + Style.RESET_ALL)


    try:
        vid_url, aud_url , vid_ext , aud_ext , title = get_url(vidid, audid, video_info)

        if not vid_url:
            print(Fore.RED + "Error occurred. try again" + Style.RESET_ALL)
            time.sleep(5)
            break

    except Exception as e:
        print(f"An error occurred. Please try again later. | {e}")
        time.sleep(5)
        break

    print(Fore.YELLOW + 'We are about to generate Nim-Baha Links' + Style.RESET_ALL)
    print(Fore.CYAN + 'Making Nim-baha Links Wait...' + Style.RESET_ALL)

    try:
        if option == 1 or option == 3:
            nvid_url = asyncio.run(nimbahaurl(link=vid_url))
        if option == 2 or option == 3:
            naud_url = asyncio.run(nimbahaurl(link=aud_url))

    except Exception as e:
        print(Fore.RED + f"Error occurred. try again | {e}" + Style.RESET_ALL)
        time.sleep(5)
        break

    print(Fore.YELLOW + 'Nim-Baha Links generated' + Style.RESET_ALL)

    def get_confirm():
        while True:
            choice = input(Fore.CYAN + 'Turn Off your VPN and Enter (Y) to Start Download Process Or Enter (N) to Cancel: ' + Style.RESET_ALL)
            choice = choice.upper()
            if choice in ["Y", "N"]:
                return choice
            else:
                print(Fore.LIGHTRED_EX + "You entered a wrong option. Please enter Y or N." + Style.RESET_ALL)

    confrm = get_confirm()

    if confrm == "N":
        print(Fore.LIGHTRED_EX + "Download cancelled by user." + Style.RESET_ALL)
        time.sleep(5)
        break

    try:
        from downloadfile import dl

        if option == 1:
            dl(nvid_url, vid_ext, f"./outputs/{title}")
            print(
                Fore.GREEN + f"Video Successfully Downloaded in Output Folder| {Style.RESET_ALL} {Fore.YELLOW + title}" + Style.RESET_ALL)
            time.sleep(5)
            break
        if option == 2:
            dl(naud_url, aud_ext, f"./outputs/{title}")
            print(
                Fore.GREEN + f"Audio Successfully Downloaded in Output Folder | {Style.RESET_ALL} {Fore.YELLOW + title}" + Style.RESET_ALL)
            time.sleep(5)
            break


        dl(nvid_url,vid_ext,"video")
        dl(naud_url,aud_ext,"audio")

    except Exception as e:
        print(Fore.RED + f"Error occurred. try again | {e}" + Style.RESET_ALL)
        time.sleep(5)
        break

    try:
        from merging import merge
        merge(aud=f"audio.{aud_ext}", vid=f"video.{vid_ext}",output=f"{title}.mkv")

    except Exception as e:
        print(Fore.RED + f"An Unknown error occurred. | {e}" + Style.RESET_ALL)
        time.sleep(5)
        break


    import os
    files = [f"video.{vid_ext}", f"audio.{aud_ext}"]

    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"{file} deleted successfully!")
        else:
            print(f"{file} does not exist.")

    print(Fore.GREEN + f"Video Successfully Downloaded in Output Folder | {Style.RESET_ALL} {Fore.YELLOW + title}" + Style.RESET_ALL)
    time.sleep(5)
    break