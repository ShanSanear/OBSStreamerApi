# OBSStreamerAPI
Simple API for helping streaming remotely by combining usage of Discord, OBS, Youtube and local storage

### discord.py
- [ ] run discord  
- [ ] check if discord is running  
- [ ] check if user is connected (albeit, that may be tricky - maybe do this from Discord bot side?)

### storage.py
- [ ] rename last stored file (which is expected to be stream file)
  - [ ] make sure this won't be performed if stream is running
  - [ ] some sort of naming convention MUST be taken into account
- [ ] list all files stored, to make it possible to check if actual expected file is actually there
- [ ] move file to subfolder

### youtube.py
- [ ] rename last stream on channel (no way to change it automatically from OBS WebSocket API - at least for now)
  - [ ] as per storage, naming convetion must be taken into account

### obs.py
- [ ] make it possible to change scenes
- [ ] make it possible to list scenes
- [x] check if obs is running