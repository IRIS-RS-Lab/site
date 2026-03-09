---
title: "A Destriping Algorithm for SDGSAT-1 Nighttime Light Images Based on Anomaly Detection and Spectral Similarity Restoration"
date: 2022-11-01
summary: "Published in Remote Sensing."
authors: ["Zhang, Degang", "Cheng, Bo", "Shi, Lu", "Gao, Jie", "Long, Tengfei", "Chen, Bo", "Wang, Guizhou"]
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
Remote sensing nighttime lights (NTLs) offers a unique perspective on human activity, and NTL images are widely used in urbanization monitoring, light pollution, and other human-related research. As one of the payloads of sustainable development science Satellite-1 (SDGSAT-1), the Glimmer Imager (GI) provides a new multi-spectral, high-resolution, global coverage of NTL images. However, during the on-orbit testing of SDGSAT-1, a large number of stripes with bad or corrupted pixels were observed in the L1A GI image, which directly affected the accuracy and availability of data applications. Therefore, we propose a novel destriping algorithm based on anomaly detection and spectral similarity restoration (ADSSR) for the GI image. The ADSSR algorithm mainly consists of three parts: pretreatment, stripe detection, and stripe restoration. In the pretreatment, salt-pepper noise is suppressed by setting a minimum area threshold of the connected components. Then, during stripe detections, the valid pixel number sequence and the total pixel value sequence are analyzed to determine the location of stripes, and the abnormal pixels of each stripe are estimated by a clustering algorithm. Finally, a spectral-similarity-based method is adopted to restore all abnormal pixels of each stripe in the stripe restoration. In this paper, the ADSSR algorithm is compared with three representative destriping algorithms, and the robustness of the ADSSR algorithm is tested on different sizes of GI images. The results show that the ADSSR algorithm performs better than three representative destriping algorithms in terms of visual and quantitative indexes and still maintains outstanding performance and robustness in differently sized GI images.

## 引用格式
```bibtex
@article{zhangDestripingAlgorithmSDGSAT12022,
  title={A Destriping Algorithm for SDGSAT-1 Nighttime Light Images Based on Anomaly Detection and Spectral Similarity Restoration},
  author={Zhang, Degang and Cheng, Bo and Shi, Lu and Gao, Jie and Long, Tengfei and Chen, Bo and Wang, Guizhou},
  journal={Remote Sensing},
  year={2022}
}
```
-->
