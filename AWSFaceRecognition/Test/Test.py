import boto3
import io
from PIL import Image
from botocore.exceptions import BotoCoreError, ClientError

rekognition = boto3.client('rekognition', region_name='us-east-1')
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

image_path = input("Enter path of the image to check: ")

try:
    with Image.open(image_path) as image:
        stream = io.BytesIO()
        image.save(stream, format="JPEG")
        image_binary = stream.getvalue()

    response = rekognition.search_faces_by_image(
        CollectionId='famouspersons',
        Image={'Bytes': image_binary}
    )

    found = False
    for match in response['FaceMatches']:
        print(match['Face']['FaceId'], match['Face']['Confidence'])

        face = dynamodb.get_item(
            TableName='FaceRecognition',
            Key={'RekognitionId': {'S': match['Face']['FaceId']}}
        )

        if 'Item' in FaceRecognition:
            print("Found Person: ", face['Item']['FullName']['S'])
            found = True

    if not found:
        print("Person cannot be recognized")

except FileNotFoundError:
    print("The specified image file was not found. Please check the path and try again.")
except (BotoCoreError, ClientError) as e:
    print(f"An error occurred while interacting with AWS services: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


