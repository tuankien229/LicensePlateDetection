# LicensePlateDetection
https://drive.google.com/drive/folders/1zOF_6BOatU0tfNNcETWkn3DCMeuL51Ne?usp=sharing

In this project i will introduce you how to use transfer learning in License plate detection.
We have here a raw data about image that take in Vietnam parking garage, this data only have data about motobike license plate in Vietnam.
![0000_00532_b](https://user-images.githubusercontent.com/68015472/154191791-a43410f4-27fe-4d00-810e-377026272bc1.jpg)


![0000_02187_b](https://user-images.githubusercontent.com/68015472/154191802-cbb14c4d-6151-4ca5-8675-d928a7a97071.jpg)


![0006_05286_b](https://user-images.githubusercontent.com/68015472/154191905-6c0fd80f-724a-42a6-9ece-772c9ee69c69.jpg)

# To do list:
1. Before you run this file you must argumentation image data first because we need more and more data about what we want the machine to learn. For argumentation, I have a file name 'Agumentation_image.py', so you can run it with a dataset I have uploaded in google drive folder 'darknet/data/' name 'Save_image'.

![0](https://user-images.githubusercontent.com/68015472/154191746-4be532b8-504a-40c5-8202-70c94ae1cf77.jpg)



![1](https://user-images.githubusercontent.com/68015472/154191757-a3b9aa58-932a-41ee-80a3-1e02ec18daec.jpg)


![3](https://user-images.githubusercontent.com/68015472/154191765-b836b4d9-5888-4ed6-b4a4-f663bcf45cda.jpg)

3. After argumentation, you need to label the raw data by LabelImg to detect where is your license and save the label by Yolo format

[0.txt](https://github.com/tuankien229/LicensePlateDetection/files/8076528/0.txt)

[1.txt](https://github.com/tuankien229/LicensePlateDetection/files/8076530/1.txt)

[2.txt](https://github.com/tuankien229/LicensePlateDetection/files/8076532/2.txt)

5. When we have the Yolo file, data argument, and upload to the drive for training in collab you can run this file for training and see the result.

![image](https://user-images.githubusercontent.com/68015472/154190420-82923026-1b36-4375-be0b-4b5d7f985d6c.png)
