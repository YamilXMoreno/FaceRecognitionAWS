import boto3

s3 = boto3.resource('s3')

images = [
    ('image1.jpg', 'Johnny Depp'),
    ('image2.jpg', 'Johnny Depp'),
    ('image3.jpg', 'Michael Jackson'),
    ('image4.jpg', 'Michael Jackson'),
    ('image5.jpg', 'Bill Gates'),
    ('image6.jpg', 'Bill Gates'),
    ('image7.jpg', 'Elon Musk'),
    ('image8.jpg', 'Elon Musk'),
    ('image9.jpg', 'Leonardo DiCaprio'),
    ('image10.jpg', 'Leonardo DiCaprio'),
    ('image11.jpg', 'Sundar Pichai')
    ('image12.jpg', 'Sundar Pichai')
]

for image in images:
    file = open(image[0], 'rb')
    object = s3.Object('famouspersons-faces', 'index/' + image[0])
    ret = object.put(Body=file, Metadata={'FullName': image[1]})
