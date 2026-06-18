# TalkBackAssistant

Python voice-assistant experiment with speech/audio assets and a Windows setup helper.

## Status

Legacy Python project. Kept as an early assistant/automation experiment.

## Contents

- `OnlyCode/TalkBackAssistant.py` - main assistant script
- `OnlyCode/requirements.txt` - Python dependencies
- `OnlyCode/start.mp3` and `OnlyCode/over.mp3` - audio cues
- `Utils/Setup.bat` - Windows setup helper
- `Utils/PyAudio-*.whl` - bundled PyAudio wheel for Windows

## Setup

```bash
cd OnlyCode
pip install -r requirements.txt
python TalkBackAssistant.py
```

## Note

This project targets an older Windows/Python setup. If you revive it, start by updating dependencies and removing bundled binary wheels where possible.
