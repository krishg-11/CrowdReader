import boto3
import os

def getFrequency(img):
    emotions = ['HAPPY', 'ANGRY', 'SAD', 'SURPRISED','DISGUSTED', 'CONFUSED']
    frequency = [0,0,0,0,0,0]

    client = boto3.client('rekognition',
        aws_access_key_id = 'your access key',
        aws_secret_access_key = 'your secret access key'
    )

    with open(img, "rb") as image:
      f = image.read()

    response = client.detect_faces(
        Image={
            'Bytes': f
        },
        Attributes=[
            'ALL',
        ]
    )
    os.remove(img)
    for face in response['FaceDetails']:
        maxe = ''
        maxc = 0
        for emote in face['Emotions']:
            if emote['Confidence'] > maxc and emote['Type'] != 'CALM':
                maxe = emote['Type']
                maxc = emote['Confidence']
        frequency[emotions.index(maxe)]+=1
    return frequency
