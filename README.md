# Cherries_detection

Real-time detection, segmentation and counting red balls for Eurobot Competition.

Project goals:
For counting red balls (cherries) do the following:
 - Implement classic CV algorithms (Edge detection);
 - Implement classic CV algorithms (Hough Transform);
 - Implement CNNs (Faster R-CNN);
 - Implement CNNs (Yolo v8);
 - Compare results.

**_Edge detection_**
<img width="1218" alt="image" src="https://github.com/aliudvidere/Cherries_detection/assets/114606110/b166b01c-494e-4dc1-b3e0-62ba22614b3b">
This method does not work properly



**_Hough Transfor_**
<img width="1054" alt="image" src="https://github.com/aliudvidere/Cherries_detection/assets/114606110/b7157831-03c8-4d44-9804-c523a6c5474b">
This algorithm works correct, but only with fixed
size of ball and certain position of the camera. In this case we cannot use this approach.



_**Dataset**_
<img width="1162" alt="image" src="https://github.com/aliudvidere/Cherries_detection/assets/114606110/0c44ea21-a0cc-4df5-8adb-29ee0f435b1a">
For networks trainings we use custom dataset, which was annotated using Roboflow.



**_Faster R-CNN_**
<img width="1176" alt="image" src="https://github.com/aliudvidere/Cherries_detection/assets/114606110/6953b22d-fb32-4bce-ac48-edf9776b3e89">



**_YOLO v8_**
<img width="1118" alt="image" src="https://github.com/aliudvidere/Cherries_detection/assets/114606110/deada77b-6b78-495f-bb43-44ddb25f5fc4">
<img width="1012" alt="image" src="https://github.com/aliudvidere/Cherries_detection/assets/114606110/2e1523a5-0889-4f27-a7e6-6c4ec8c0e03e">



**_Results_**
Compare all approaches we decided use YOLO v8 due to:
 - It works properly;
 - It is faster then Faster R-CNN;
 - It can work on week hardware like Raspberry Pi4.

Earlier we planed using electronics for counting cherries, but CV show, that we can do this without vibromotors and complex mechanics.





