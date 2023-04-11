# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 11:16:14 2023

@author: jhonn
"""

import boto3
from botocore.client import Config
ACCESS_KEY_ID = 'AKIA44LXN5RYCLEO7QID'
ACCESS_SECRET_KEY = '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;;;;'
#BUCKET_NAME = ''
#s3 Connect
s3 = boto3.resource('s3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
"""
listObjSummary = s3.Bucket(BUCKET_NAME).object.all()
for objSum in listObjSummary:
    print('Item:')
    print(objSum.key)
print('Done')
"""

def compare_faces(sourceFile, targetFile):

    client=boto3.client('rekognition')
   
    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')

    response=client.compare_faces(SimilarityThreshold=80,
                                  SourceImage={'Bytes': imageSource.read()},
                                  TargetImage={'Bytes': imageTarget.read()})
    
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + similarity + '% confidence')

    imageSource.close()
    imageTarget.close()     
    return len(response['FaceMatches'])          

def main():
    source_file='source'
    target_file='target'
    face_matches=compare_faces(source_file, target_file)
    print("Face matches: " + str(face_matches))


if __name__ == "__main__":
    main()