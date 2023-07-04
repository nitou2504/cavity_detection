# Cavity Detection

Cavity Detection is a machine learning project aimed at detecting caries on regions of interest (ROIs) in periapical dental radiographs. This repository contains a collection of Jupyter notebooks that implement different strategies for training Convolutional Neural Network (CNN) and Deep Convolutional Neural Network (DCNN) models. The project focuses on two main preprocessing techniques applied to the images: Gauss noise padding and ROI area expansion.

## Table of Contents
- [Preprocessing](#preprocessing)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [ROC Analysis](#roc-analysis)
- [Window Prediction](#window-prediction)
- [Patch Prediction](#patch-prediction)

## Preprocessing
The preprocessing notebook in this project downloads the dataset from Roboflow and extracts ROIs for both the training and test splits. Two different preprocessing techniques are employed:
1. Gauss Noise Padding: When an ROI does not meet the standard size or aspect ratio (100 x 100 px), gauss noise padding is added to adjust its dimensions.
2. ROI Area Expansion: In this approach, the ROI area is expanded on the original image to incorporate more surrounding details of the caries.

## Model Training
The model_train notebook implements the training pipeline for the CNN and DCNN models. The training is performed using a 3 times 10-fold scheme, ensuring robustness and comprehensive evaluation. The trained models are saved for subsequent analysis.

## Model Evaluation
The train_model_evaluation notebook is used to analyze the results of the trained models. It provides a detailed evaluation of the performance metrics and allows for further investigation and analysis.

## ROC Analysis
The roc notebook conducts a Receiver Operating Characteristic (ROC) analysis on the trained models. It plots the ROC curves and calculates the corresponding Area Under the Curve (AUC) scores, providing insights into the models' discrimination abilities.

## Window Prediction
The window_prediction notebook presents an approach to assess the viability of the proposed method in real-world scenarios. It takes a whole image as input and generates a heatmap of prediction values. This is achieved by making predictions on patches throughout the entire image, as the model's original input size is 100 x 100 px.

## Patch Prediction
The patch_prediction notebooks contain experiments to test individual patch predictions. These notebooks provide a way to assess the accuracy and reliability of predictions on smaller regions of interest within the dental radiographs.

## Conclusion
The Cavity Detection project offers a comprehensive pipeline for training CNN and DCNN models to detect caries on ROIs in periapical dental radiographs. By employing various preprocessing techniques and evaluating the models' performance, the project aims to provide valuable insights into the detection of dental caries, with the potential for real-world application.

Please refer to the individual notebooks for more detailed information on each step of the pipeline and for code implementation.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). 
