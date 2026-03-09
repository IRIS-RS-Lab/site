---
title: "Spatial--Temporal Approach and Dataset for Enhancing Cloud Detection in Sentinel-2 Imagery: A Case Study in China"
date: 2024-03-01
summary: "Published in Remote Sensing."
authors: ["Gong, Chengjuan", "Yin, Ranyu", "Long, Tengfei", "Jiao, Weili", "He, Guojin", "Wang, Guizhou"]
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
Clouds often cause challenges during the application of optical satellite images. Masking clouds and cloud shadows is a crucial step in the image preprocessing workflow. The absence of a thermal band in products of the Sentinel-2 series complicates cloud detection. Additionally, most existing cloud detection methods provide binary results (cloud or non-cloud), which lack information on thin clouds and cloud shadows. This study attempted to use end-to-end supervised spatial--temporal deep learning (STDL) models to enhance cloud detection in Sentinel-2 imagery for China. To support this workflow, a new dataset for time-series cloud detection featuring high-quality labels for thin clouds and haze was constructed through time-series interpretation. A classification system consisting of six categories was employed to obtain more detailed results and reduce intra-class variance. Considering the balance of accuracy and computational efficiency, we constructed four STDL models based on shared-weight convolution modules and different classification modules (dense, long short-term memory (LSTM), bidirectional LSTM (Bi-LSTM), and transformer). The results indicated that spatial and temporal features were crucial for high-quality cloud detection. The STDL models with simple architectures that were trained on our dataset achieved excellent accuracy performance and detailed detection of clouds and cloud shadows, although only four bands with a resolution of 10 m were used. The STDL models that used the Bi-LSTM and that used the transformer as the classifier showed high and close overall accuracies. While the transformer classifier exhibited slightly lower accuracy than that of Bi-LSTM, it offered greater computational efficiency. Comparative experiments also demonstrated that the usable data labels and cloud detection results obtained with our workflow outperformed the results of the existing s2cloudless, MAJA, and CS+ methods.

## 引用格式
```bibtex
@article{gongSpatialTemporalApproach2024,
  title={Spatial--Temporal Approach and Dataset for Enhancing Cloud Detection in Sentinel-2 Imagery: A Case Study in China},
  author={Gong, Chengjuan and Yin, Ranyu and Long, Tengfei and Jiao, Weili and He, Guojin and Wang, Guizhou},
  journal={Remote Sensing},
  year={2024}
}
```
-->
