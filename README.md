# Welcome to the snippets for STARTHACK2017

##### Tested with python 2.7 and 3.5 on MacOSX and Ubuntu

[logo]:start-hack-2017.jpg

![alt text][logo]

`!!!!!!!!!!!!! ATTENTION - THESE SNIPPETS ARE NOT MADE FOR REAL USAGE!!!!!!!!!!!!!!`

It will develop during starthack2017. Here you can find some hints for:

1. Tinderlike App 
2. How to use the GPU-rig
3. Getting started with tensorflow
4. Sample for speaker recognition (classifier)
5. Sample for speaker recommendation based on classifier
6. Inspiration

These snippets will give you a glimpse of the power of AI. 
For improvement you need to transform it into an online approach like used in recommendation systems (e.g. classic movie database problem). Preprocessing the wav files can improve the result as well. For sure a recommendation system could be also built just based on likes without a feature extracted from the wav.


## 1 Tinderlike App

### General ideas

#### Images vs. Voice

The users should still upload a profile-image. But it will be blurried when swiping. Only audio as well as demographic information (and distance) is given.

On a match (if two fellows like each others voice) the image blur will be reduced a bit.

On every sentence they chat thereafter the blur will be further reduced. This is a good incentive to get to know each other before judging on superficial appearance.

#### Valuable data

The following data is valuable in regards to AI-training:

 - spoken sentences with according high- and / or swiss-german texts to train speech to text and text to speech models
 - usual geolocation of the users (home) in order to determine origins of accents and finetune the respective models

### Design-Resources

There are cool design-resources available to use:

 - Tinder iOS UI Kit - https://www.sketchappsources.com/free-source/2432-tinder-ios-ui-kit-sketch-freebie-resource.html
 - Tinder Android App UI Kit - https://www.sketchappsources.com/free-source/2147-tinder-android-app-ui-kit-sketch-freebie-resource.html

### How the results of this Hackathon are used

Training data that will be collected using results from this Hackathon will be available to everyone who's interested in it - not just Swisscom.

We're believing in opensource and open collaboration to create far more advanced solutions.

### Intersting Repositories

- Sample Swipe - https://github.com/Diolor/Swipecards
- Sample App - https://github.com/akveo/chernika-mobile
- Sample App - https://github.com/matthieu-beteille/gipher

## 2 How to use the GPU-rig

First of all: Make your application or script docker-ready. In fact, make it nvidia-docker-ready:

https://github.com/NVIDIA/nvidia-docker

As soon as you're ready let us know and we'll give you SSH-access onto the machine to execute your docker things.

Note that the data integrity on the GPU-rig is not guaranteed. So everytime you run something on the GPU-rig (for instance creating a model) make sure to download that data onto your local machine after processing.

## 3 Getting started with tensorflow

Everything is very well documented on the tensorflow webpage: https://www.tensorflow.org/get_started/get_started

We recommend the "MNIST For ML Beginners" tutorial.

## 4 Sample for speaker recognition (classifier)

In this example we try to recognize the speaker by a sample. We use in this sample MFCC () as feature. There are many other options to extract features from a speaker.

The MFCC features we extract with <a href="https://github.com/librosa/librosa">librosa</a>

To handle N-dimensional array Objects  this sample contains <a href="http://www.numpy.org/">numpy</a>


## 5 Sample for speaker recommendation based on classifier



## 6 Inspiration
https://github.com/pannous/tensorflow-speech-recognition