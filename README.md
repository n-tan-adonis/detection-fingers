# Count Fingers

## Project Overview

### 1 Goal

This is a basic project to detect finger gestures by counting the number of raised fingers. 
You can absolutely use this project to develop more meaningful functions such as detecting the body language of mute people.


### 2 Dependencies

* Python
* Mediapipe
* OpenCV

### 3 Project Structure

* *fingers.py*: is a main program to run

### 4 Theory
<img width="240" alt="finger" src="https://github.com/n-tan-adonis/detection-fingers/assets/127659484/acfcea02-076f-427e-8fff-490a85316214">


* The key point here is that the length from the tip of the finger to the base of the thumb will be longer than the distance from the base of those fingers to the base of the thumb.
* For example, when the index finger is raised, the distance from point 8 to 1 is longer than the distance from 5 to 1. Likewise, when the middle finger is raised, the distance from point 12 to point 1 is also longer. will be longer than the distance from point 9 to point 1.
* As for the thumb, we will compare the distance of the tip of the thumb to point 0 and from point 2 to 0



### 5 Result

* 1 finger

<img width="958" alt="1ngon" src="https://github.com/n-tan-adonis/detection-fingers/assets/127659484/d099a06e-db1d-4587-a984-cafadc5e742a">

* 2 finger

<img width="959" alt="2ngon" src="https://github.com/n-tan-adonis/detection-fingers/assets/127659484/a7af338b-3b49-48a9-ae8d-db95d893def0">

* 3 finger


<img width="959" alt="3ngon" src="https://github.com/n-tan-adonis/detection-fingers/assets/127659484/1ccab5f4-5683-4b67-a6c0-7ca7244a5f59">

* 4 finger

  
<img width="959" alt="4ngon" src="https://github.com/n-tan-adonis/detection-fingers/assets/127659484/91b4631b-4735-40d2-91a7-8cf974ae5775">

* 5 finger

<img width="959" alt="5ngon" src="https://github.com/n-tan-adonis/detection-fingers/assets/127659484/2c8609dc-784c-4627-9337-a66a83ecf3d7">
