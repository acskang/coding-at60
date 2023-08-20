from pytube import extract
from pytube import YouTube

주소 = "https://www.youtube.com/watch?v=c8yHTlrs9EA&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=48"

비디오_번호 = extract.video_id(주소)

print(비디오_번호)

yt = YouTube(주소)
print(yt.title)