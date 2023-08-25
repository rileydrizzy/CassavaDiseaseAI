# PROJECT / BUSINESS UNDERSTANDING

***TEMPORARY README***

Cassava is a vital crop for food security in Africa, particularly among smallholder farmers who can grow it in tough conditions. However, viral diseases lead to poor yields. Data science offers a way to detect these diseases effectively. Current disease detection methods rely on labour-intensive and expensive visual inspections by agricultural experts. This is challenging as African farmers often have limited resources. To address this, a dataset of 21,367 labelled images from Uganda is introduced. These images were taken by farmers and annotated by experts. The goal of this project is to classify cassava images into either of the four disease categories or a healthy state, aiding farmers in timely disease identification and crop preservation. After training of the model, the model shall be deployed on the edge where inference would take place. As such constraints such as serving the model as **client-side inference on web browsers and fast inference on the edge device**.

## Project Objectives

1. Classification of Cassava Images into either of the four categories or the fifth as a healthy one
2. Employed tactics for fast inference time and lower power usage
3. Create a web-based application for inference
4. Serve model and deploy the web-based application as client-side inference
