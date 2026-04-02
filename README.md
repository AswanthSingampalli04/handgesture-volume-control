# HandGesture Volume Control System

I developed this computer vision application to control computer volume using hand gestures - no mouse or keyboard needed! Just show your hand to the webcam and pinch with your thumb and index finger to adjust the sound.

## What It Does

- **Tracks your hand in real-time** using your computer's camera
- **Controls volume** based on how far apart your thumb and index finger are
- **Shows visual feedback** with a volume bar and percentage display
- **Works instantly** - no training required, just run and use

## How I Built It

This project combines several technologies I learned:

- **OpenCV** for capturing and processing video from the webcam
- **MediaPipe** (Google's hand tracking library) to find hand landmarks
- **PyCAW** to control Windows system volume
- **NumPy** for the math calculations

The core idea is simple: measure the distance between your thumb tip and index finger tip, then map that distance to the volume range. Closer fingers = lower volume, wider fingers = higher volume.

## Getting Started

### What You Need
- Python 3.8 or higher
- Windows computer (for audio control)
- Webcam
- Git (if you want to clone the repo)

### Installation Steps

1. **Get the code**:
   ```bash
   git clone <repository-url>
   cd handgesture-volume-control
   ```

2. **Set up Python environment** (recommended but optional):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run it**:
   ```bash
   python main.py
   ```

## Using the App

1. **Start the application** with `python main.py`
2. **Show your hand** to the camera - make sure it's well-lit
3. **Control volume** by adjusting the gap between thumb and index finger:
   - Pinch fingers together for minimum volume
   - Spread fingers apart for maximum volume
4. **Keyboard shortcuts**:
   - Press **ESC**, **Q**, or **X** to exit
   - Press **H** to see help on screen

## Project Files

```
handgesture-volume-control/
├── main.py                 # The main application
├── hand_landmarker.task    # Hand detection model (7.8MB)
├── requirements.txt        # All Python packages needed
├── README.md              # This file
├── LICENSE                # MIT License
├── .gitignore             # Files to ignore in Git
└── DOCUMENTATION.md       # Technical details
```

## Why This Matters for My Studies

This project helped me practice several important computer science concepts:

- **Computer Vision**: Real-time image processing and object detection
- **Machine Learning**: Using pre-trained models (MediaPipe hand detector)
- **System Programming**: Working with Windows APIs for audio control
- **Mathematical Thinking**: Coordinate systems and interpolation
- **Software Engineering**: Clean code, error handling, user experience

## Technical Requirements

- **Windows OS** (required for audio control - PyCAW only works on Windows)
- **Webcam** with decent lighting for best hand detection
- **Python packages** (see requirements.txt for exact versions)

## Challenges I Solved

1. **Hand detection accuracy** - Found the optimal distance range (30-200 pixels) for volume mapping
2. **Real-time performance** - Optimized processing to maintain smooth interaction
3. **Audio integration** - Successfully connected computer vision to system audio controls
4. **User experience** - Added clear visual feedback and intuitive controls

## License

This project is open source under the MIT License - feel free to learn from it, modify it, or use it in your own projects.

---

*Built as a demonstration project for computer science and engineering university applications. This represents my skills in computer vision, machine learning integration, and practical software development.*
