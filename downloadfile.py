import requests
from tqdm import tqdm

def dl(url,ext,name):
    filename = f"{name}.{ext}"  # specify name and extension

    response = requests.get(url, stream=True)
    response.raise_for_status()  # ensure the request was successful

    # Get total file size (in bytes)
    total_size = int(response.headers.get('content-length', 0))

    with open(filename, "wb") as f, tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as pbar:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            pbar.update(len(chunk))

    print(f"Downloaded as {filename}")

