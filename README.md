# Deep Learning for Detecting Amphoras in Ancient Shipwrecks

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tillchen/amphora_object_detection/blob/master/amphora_object_detection.ipynb)

* [Deep Learning for Detecting Amphoras in Ancient Shipwrecks](#deep-learning-for-detecting-amphoras-in-ancient-shipwrecks)
  * [Project Structure](#project-structure)
  * [References](#references)

This repository contains the code, the trained model, and the thesis for "Deep Learning for Detecting Amphoras in Ancient Shipwrecks". The simplest way to view the code and the result is through the `Open in Colab` button at the top.

## Project Structure

* `annotations` stores the `csv` and TensorFlow `record` files, which were converted from `xml` using the scripts in `scripts/preprocessing`. The `label_map.pbtxt` file defines the class, which is `amphora` in our case.
* `images` contains all the training, validation, and test images in the `train`, `val`, and `test` directories respectively. The `xml` files produced by [labelImg](https://github.com/tzutalin/labelImg) are also stored here.
* `models/ssd_resnet50_v1_fpn` stores the `tfevents` files for TensorBoard evaluation. The `pipeline.config` file is the configuration file used for training.
* `pretrained_models/ssd_resnet50_v1_fpn_shared_box_predictor_640x640_coco14_sync_2018_07_03` is the pre-trained model obtained from the [TensorFlow 1 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md).
* `scripts` stores the Python scripts. `preprocessing/xml_to_csv.py` converts the `xml` files in `images` to `csv` files in `annotations`; `preprocessing/generate_tfrecord.py` converts the `csv` files to TensorFlow `record` files in `annotations`. `statistics/count_objects.py` counts the number of objects and computes the train: val ratio from the `xml` files.
* `thesis` has the complete thesis write-up in LaTeX. `Tianyao_Chen_bachelor_thesis.pdf` is the main PDF file.
* `trained_models/ssd_resnet50_v1_fpn.pb` has the exported trained model for inference from this study.

## References

* <https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/tensorflow-1.14/training.html>
* <https://www.dlology.com/blog/how-to-train-an-object-detection-model-easy-for-free/>
* <https://neptune.ai/blog/tensorflow-object-detection-api-best-practices-to-training-evaluation-deployment>
