import os
from pytube import Search
from spotify_api import Song
from pathlib import Path

def downlaod_playlist(playlist, outdir):
    for song in playlist:
        search_term = str(song)

        response = Search(search_term).results

        video = response[0].streams.filter(abr='160kbps').last()

        out_file = video.download(output_path=outdir)
        base, _ = os.path.splitext(out_file)
        new_file = Path(f"{base}.mp3")
        os.rename(out_file, new_file)

        if new_file.exists():
            print(f"Downloaded: {search_term}")
        else:
            print("ERROR: failed to download '{search_term}'")


s = Song('Northern Attitude (with Hozier)', ['Noah Kahan', 'Hozier'])

downlaod_playlist([s], '.')
