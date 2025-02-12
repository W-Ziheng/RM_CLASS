# RM_CLASS
Welcome to the RM_CLASS repository!

The official training hub for the Algorithm Team of the Fuzhou University `浮舟湿地` for the 2025 season. The `main` branch contains markdown documents and reference solutions for each training session, making it easy to access learning materials and review exercises.

This training program is divided into several key parts, as follows:

---

## 提交作业步骤

### 1. 克隆仓库到本地
首先，确保你已经将该仓库克隆到本地。打开 Git Bash 或其他终端，执行以下命令：

```bash
git clone -b Homework https://github.com/W-Ziheng/RM_CLASS.git
```

> 最好 Fork 我的仓库到自己账户后再 git clone 

### 2. 创建并切换到自己的分支
为了方便管理你的作业，每个成员都需要在自己的分支上进行修改。你可以使用以下命令创建一个新分支并切换过去：

```bash
git checkout -b "your-branch-name"
```

**注意**：请将 `your-branch-name` 替换为你的分支名称，建议使用包含你名字的分支名，比如 `wang-zi-heng-class1`。

### 3. 提交作业文件
在本地分支中进行作业的编写或修改，完成后使用以下命令提交：

```bash
git add .
git commit -m "XXX提交CLASS_1作业"
```

### 4. 推送分支到 GitHub
将本地的修改推送到远程仓库：

```bash
git push origin "your-branch-name"
```

可以直接用 VScode Push 会方便一点

### 5. 提交 Pull Request
1. 登录到 GitHub，进入该仓库页面。
2. 你会看到一个提示，询问是否创建一个新的 Pull Request。
3. 点击 **Compare & Pull Request**。
4. 填写合适的标题和描述，确保描述清晰明了（例如：“XXX提交CLASS_1作业”）。
5. 点击 **Create Pull Request** 提交你的修改。

> 如果是在自己Fork的仓库修改的,需要再Pull Request 到我的仓库内,才会生效
### 6. 等待评审
提交后，组内其他成员或负责人会对你的作业进行评审。如果需要修改，他们会在 Pull Request 下给出反馈。

> The Environment based on Ubuntu22.04 ROS2-Humle

## CLASS_1: Introduction to Linux and ROS2, Basic Programming

- **Initial Setup: Linux and ROS2 Installation**
  - Set up a Linux environment and install ROS2 along with the pre-installed packages for hands-on experience.
  
- **Introduction to Programming Languages**
  - Learn the basics of C++ and Python, essential programming languages for robotics development.
  - Understand Markdown for creating well-structured documentation.

## CLASS_2: Getting Started with Linux, ROS, and Computer Vision

- **Linux Fundamentals**
  - Familiarize yourself with Linux commands and the operating system environment.

- **Introduction to ROS (Robot Operating System)**
  - Install ROS and write your first ROS2 node.
  - Learn about ROS topics, communication mechanisms, messages, and related concepts.

## CLASS 3: Introduction to Computer Vision and Basic Object Detection

- **Installing OpenCV and Setting Up the Environment**
  - Set up OpenCV on your system to begin exploring computer vision techniques.
  - Learn to implement essential functions like reading images, video capture, and basic image manipulation using OpenCV.

- **Basic Color Detection**
  - Implement a real-time color detection system using a webcam.
  - Understand how to process images in different color spaces (e.g., HSV) and apply thresholds to detect specific colors.
  
- **Object Recognition**
  - Develop a simple object recognition system using OpenCV, leveraging techniques such as contour detection and template matching.
  - Learn to identify basic shapes and objects based on color and geometric features.

## CLASS 4: Armor Plate Recognition and SLAM Navigation Simulation

- **Armor Plate Detection with Computer Vision**
  - Using a webcam, implement a system to detect armor plates in real-time by processing video frames.
  - Explore techniques such as edge detection, contour finding, and template matching to identify armor plates in dynamic environments.

- **SLAM Navigation Simulation with ROS**
  - Integrate ROS with OpenCV to simulate robotic navigation using a camera feed.
  - Learn how to implement a simple SLAM (Simultaneous Localization and Mapping) system to create maps of the environment while navigating.
  - Use ROS to control a specified robot chassis and simulate its navigation while scanning for obstacles and mapping the surroundings.

## CLASS 5: YOLOv5 Deployment and Object Detection

- **Deploying YOLOv5 for Object Detection**
  - Learn how to deploy the YOLOv5 deep learning model for object detection.
  - Install necessary dependencies and set up the YOLOv5 environment for real-time object identification in video streams.

- **Training and Fine-tuning YOLOv5**
  - Explore how to fine-tune the YOLOv5 model using custom datasets to detect specific objects relevant to your project (e.g., armor plates, other objects of interest).
  - Learn how to evaluate the model’s performance and improve accuracy by adjusting hyperparameters or augmenting training data.

- **Real-time Object Detection with YOLOv5**
  - Implement real-time object detection with YOLOv5, capturing frames from a camera and running the detection model on each frame to identify and classify objects.

---

If you have any suggestions or questions, please feel free to open an **issue** to initiate a discussion and give me a **STAR** in the top right corner.We will highly appreciate your feedback and collaboration.

---

