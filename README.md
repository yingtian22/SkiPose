### 🎥 Example

<p align="center">
  <img src="Gifs/example.gif" width="1000" alt="example gif">
</p>

<!-- <p align="center">
  <img src="Gifs/output2.gif" width="220" alt="Original video">
  <img src="Gifs/AlphaPose_output2.gif" width="220" alt="2D keypoints">
  <img src="Gifs/X3D2.gif" width="220" alt="3D keypoints">
</p> -->

# Dataset Description

This dataset is a motion capture record of a skier's dynamic movements, collected using an Inertial Measurement Unit (IMU).  
Each sample is time-sequenced and associated with a specific timestamp `t` (in seconds).

At each timestamp, the dataset contains **10–20 anatomical keypoints**, representing major joints or body segments, such as:

- Ankles  
- Knees  
- Shoulders  
- Wrists  

---

## Data Format

For each **keypoint** at a given timestamp, two components are provided:

1. **3D Position Coordinates**  
   - A triplet `(x, y, z)`  
   - Units: meters  
   - Represents the spatial position of the keypoint in 3D space.

2. **Orientation Quaternion**  
   - A normalized 4D vector `(q_w, q_x, q_y, q_z)`  
   - Encodes the rotational pose of the keypoint.  
   - Quaternions are used to:  
     - Avoid gimbal lock  
     - Enable smooth and robust orientation interpolation  
   - Normalization condition:  
     \[
     q_w^2 + q_x^2 + q_y^2 + q_z^2 \approx 1
     \]

---

## Hierarchical Structure

The data is organized per timestamp. Conceptually, each time step `t` looks like this:

```text
t |
  (x1, y1, z1), (q_w1, q_x1, q_y1, q_z1) |
  (x2, y2, z2), (q_w2, q_x2, q_y2, q_z2) |
  ...
```

- `t` – timestamp in seconds  
- Each `|` separates **individual keypoints** at the same timestamp  
- Each time step (i.e., each `t` block) forms one sequential data unit in the time series

---

## Extended Pose Data (2D / 3D)

In addition to IMU-based 3D position and orientation data, we further process the collected data using vision-based pose estimation pipelines to obtain both 2D and 3D human pose representations. This enables multi-modal fusion and more intuitive visualizations.

### 2D Pose Data (AlphaPose)

We use [AlphaPose](https://github.com/MVIG-SJTU/AlphaPose) to perform 2D human pose estimation on the original video and obtain frame-wise 2D keypoints. The related results are stored in the `Videos` folder:

- `Videos/AlphaPose_output.mp4`  
  - A video where 2D skeletons are overlaid on the original footage.  
- `Videos/alphapose-results.json`  
  - Stores the 2D keypoint detection results for each frame, typically including:  
    - Keypoint pixel coordinates in the image plane `(u, v)`  
    - The corresponding detection confidence scores  
  - This file can be used for 2D pose analysis, alignment with IMU data, or as input to 3D pose lifting models (such as MotionBERT).

### 3D Pose Data (MotionBERT)

Based on the 2D pose results, we apply [MotionBERT](https://github.com/Walter0807/MotionBERT) to reconstruct 3D human pose sequences. The outputs are also stored in the `Videos` folder:

- `Videos/X3D.mp4`  
  - A visualization video showing the reconstructed 3D skeleton evolving over time, which helps to intuitively understand the spatial trajectory and rhythm of the skiing motion.  
- `Videos/X3D.npy`  
  - A NumPy binary file containing the 3D joint coordinate sequences.  
  - The data is typically organized as a tensor with shape similar to `T × J × 3`:  
    - `T`: number of time steps (frames)  
    - `J`: number of joints  
    - `3`: 3D coordinates `(x, y, z)` of each joint (in meters or a normalized unit, depending on the configuration described in the code/documentation)  

By combining IMU-derived **3D position + quaternion orientation** with vision-derived **2D / 3D pose data**, researchers can:

- Perform multi-sensor fusion (IMU + RGB video)  
- Compare sensor-based and vision-based pose estimation performance  
- Build more robust models for skiing action recognition, movement quality assessment, and performance analysis  

---

## Intended Use Cases

This dataset is designed for research and development in:

- **Motion analysis**  
- **Pose estimation**  
- **Biomechanics and joint kinematics**  
- **Human activity recognition**  
- **Injury prevention systems**  
- **Sports performance analysis and optimization**

By providing **3D position** and **orientation** for each keypoint, together with vision pipeline outputs of **2D / 3D pose**, this dataset enables:

- Detailed analysis of whole-body motion patterns  
- Evaluation of algorithms in **dynamic, real-world skiing scenarios**  
- Training and validation of machine learning models that require positional, rotational, and vision-based pose information  

## Acknowledgement

This project has benefited from the following work, and we sincerely thank all contributors:  
- [AlphaPose](https://github.com/MVIG-SJTU/AlphaPose)  
- [MotionBERT](https://github.com/Walter0807/MotionBERT)  

We gratefully appreciate their open-source contributions!
