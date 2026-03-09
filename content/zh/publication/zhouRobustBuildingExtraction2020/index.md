---
title: "Robust Building Extraction for High Spatial Resolution Remote Sensing Images with Self-Attention Network"
date: 2020-12-01
summary: "Published in Sensors."
authors: ["Zhou, Dengji", "Wang, Guizhou", "He, Guojin", "Long, Tengfei", "Yin, Ranyu", "Zhang, Zhaoming", "Chen, Sibao", "Luo, Bin"]
tags: []
featured: false
# 🔴 核心机制：此行代码会让这篇论文在列表中不可点击。若要为其添加详细页面，请删除这行代码！
external_link: "#no-detail"
links:
  - name: PDF
    url: ""
    icon: hero/document
  - name: Code
    url: ""
    icon: brands/github
---

<!--
================ 详情页隐藏区 ================
如果你删除了上方的 external_link 激活了详情页，
可以取消下方内容的注释，放入你的成果展示。
(若有配图，直接将图片命名为 featured.jpg 放在本文件夹)
==============================================
-->

<!--
## 摘要
Building extraction from high spatial resolution remote sensing images is a hot spot in the field of remote sensing applications and computer vision. This paper presents a semantic segmentation model, which is a supervised method, named Pyramid Self-Attention Network (PISANet). Its structure is simple, because it contains only two parts: one is the backbone of the network, which is used to learn the local features (short distance context information around the pixel) of buildings from the image; the other part is the pyramid self-attention module, which is used to obtain the global features (long distance context information with other pixels in the image) and the comprehensive features (includes color, texture, geometric and high-level semantic feature) of the building. The network is an end-to-end approach. In the training stage, the input is the remote sensing image and corresponding label, and the output is probability map (the probability that each pixel is or is not building). In the prediction stage, the input is the remote sensing image, and the output is the extraction result of the building. The complexity of the network structure was reduced so that it is easy to implement. The proposed PISANet was tested on two datasets. The result shows that the overall accuracy reached 94.50 and 96.15%, the intersection-over-union reached 77.45 and 87.97%, and F1 index reached 87.27 and 93.55%, respectively. In experiments on different datasets, PISANet obtained high overall accuracy, low error rate and improved integrity of individual buildings.

## 引用格式
```bibtex
@article{zhouRobustBuildingExtraction2020,
  title={Robust Building Extraction for High Spatial Resolution Remote Sensing Images with Self-Attention Network},
  author={Zhou, Dengji and Wang, Guizhou and He, Guojin and Long, Tengfei and Yin, Ranyu and Zhang, Zhaoming and Chen, Sibao and Luo, Bin},
  journal={Sensors},
  year={2020}
}
```
-->
