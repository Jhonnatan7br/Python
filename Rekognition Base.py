import boto3
rekognition = boto3.client("rekognition", aws_access_key_id="AKIA44LXN5RYCLEO7QID", aws_secret_access_key="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;;;;")

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
    source_file='sourceFile.jpg'
    target_file='targetFile.jpeg'
    face_matches=compare_faces(source_file, target_file)
    print("Face matches: " + str(face_matches))


if __name__ == "__main__":
    main()