# Efficient-and-Privacy-Preserving-Lane-Change-Scheme-for-Variable-Speed-Driving-Scenario
本项目是论文《[Efficient and Privacy-Preserving Lane Change Decision-Making Scheme for Variable Speed Driving Scenario]》的实验代码，以及部分使用的MPC组件。  
This project is the experimental code of the paper "[Efficient and Privacy-Preserving Lane Change Decision-Making Scheme for Variable Speed Driving Scenario]", and some MPC tools.

---

## 目录 Table of Contents

- [项目目录 Project Directory](#项目目录-project-directory)
- [使用方法 Getting Started](#使用方法-getting-started)
- [项目声明 Project Statement](#项目声明-project-statement)


## 项目目录 Project Directory

本项目包含如下主要文件：

- `argument.py`  
  - 参数配置文件，用于定义实验或运行时的超参数。

- `distancelist.py`  
  - 距离列表相关功能模块，用于计算时间序列与 MPC 计算中的距离度量。

- `getdata.py`  
  - 数据获取与预处理模块，用于读取和处理输入数据集。

- `main.py`  
  - 主程序入口，调用其他模块进行实验或运行推理。

- `mpc_comp.py`  
  - MPC 比较协议测试模块。

- `mpc_multy.py`  
  - MPC 乘法计算测试模块，包含mpc秘密分享，安全加法与乘法操作。

- `sinandcos.py`  
  - MPC 正弦和余弦计算函数。


## 项目声明 Project Statement

1. **项目名称**：Efficient-and-Privacy-Preserving-Lane-Change-Scheme-for-Variable-Speed-Driving-Scenario。 
2. **项目作者**：本项目作者为 Hongyuan Zhang, Anjia Yang*, Member, IEEE, Jian Weng, Member, IEEE, Min-Rong Chen, Yi Liu, and Tengfei Liu。  
3. **作者单位**：Hongyuan Zhang, Anjia Yang, Yi Liu, and Tengfei Liu are with the College of Cyber Security, Jinan University, Guangzhou 510632, China. Jian Weng is with the College of Cyber Security, GuangZhou University, Guangzhou 510006, China. Min-Rong Chen is with School of Computer Science, South China Normal University, Guangzhou 510631, China。  
