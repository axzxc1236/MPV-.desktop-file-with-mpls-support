# MPV .desktop file with mpls support
MPV doesn't open .mpls file  
I need MPV to play mpls file  
So I created an desktop file with workaround discussed at https://github.com/mpv-player/mpv/issues/1982

# Requirements
1. Python 3
2. MPV
3. Set mpv-mpls-workaround-patched.desktop as the default file association for .mpls file

# How to apply (for Ubuntu users)
1. [Download this repository](https://github.com/axzxc1236/MPV-.desktop-file-with-mpls-support/archive/master.zip)
2. Extract to `~/.local/mpv-mpls-workaround` (not hard requirement but recommended)
3. Open `~/.local/mpv-mpls-workaround`
4. copy `mpv-mpls-workaround-patched.desktop` to `~/.local/share/applications`
5. Set `<localized mpv name> (Patched to play .mpls file)` as Default application ([screenshot](https://i.imgur.com/3zCRX32.png)) (You can see [Open files with other applications](https://help.ubuntu.com/stable/ubuntu-help/files-open.html.en) if you have no clue how to do it)
6. Try it, it should work
