## Human Attention Detection

## Version 1.0
Following approval from the original author, partial modifications were implemented to produce Version 1.0.

Key differences include:

1. Fatigue detection now excludes nodding behavior detection, retaining only eye-closure and yawning detection.
2. YoloV5 weights were retrained with increased training iterations.

3. The frontend UI has been modified, streamlining certain functionalities.

## Project Overview
This project focuses on human attention detection, comprising two distinct detection modules: fatigue detection and distraction behavior detection.
The fatigue detection module utilizes Dlib for facial landmark detection. It then assesses eye and mouth opening/closing degrees to determine eye closure or yawning, employing the Perclos model to calculate fatigue levels.
The distraction detection component employs YoloV5 to identify three behaviors: phone use, smoking, and drinking.

## Usage (windows only)
```
uv sync
uv run main.py
```

For demonstration results, watch the video.

[Watch on Bilibili](https://www.bilibili.com/video/BV1MK4y1d7a8/)

All function information is well-documented with comments in the code: 如有疑问请联系 1647790440@qq.com

## Acknowledgments
We extend our sincere gratitude to the original author for their support and assistance. This project is largely based on the source project, and the datasets used were provided by the original author.
