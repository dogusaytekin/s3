import boto3
import json

s3 = boto3.resource('s3')

objectList = list()

print("""
Operations:

1. AWS S3 Bucket Name
2. List Objects
3. Content of Objects
4. Modify Content of Object

Exit with 'q' button.

""")


while True:
    operation = input("Enter Operation Number:")

    if (operation == "q"):
        print("Exiting...")
        break

    elif (operation == "1"):

        # Print out bucket name
        for bucket in s3.buckets.all():
            print(f"My Bucket: {bucket.name}")

    elif (operation == "2"):

        # Print out object list
        my_bucket = s3.Bucket(bucket.name)
        objectList.clear()
        for my_bucket_object in my_bucket.objects.all():
            objectList.append(my_bucket_object.key)
            print(f"My Object List: {my_bucket_object.key}")

    elif (operation == "3"):

        # Print out content of object
        print(f"My Object List: {objectList}") #{my_bucket_object.key} de eklenebilir
        userInput = input("Enter file name:")
        if objectList.__contains__(userInput):
            obj = s3.Object(bucket.name, userInput)
            body = obj.get()['Body'].read()
            print(body.decode("utf-8"))
        else:
            print("The file does not exist")

    elif (operation == "4"):

        # Put object to bucket
        print(f"My Object List: {objectList}") #{my_bucket_object.key} de eklenebilir
        userInput = input("Enter file name:")

        if objectList.__contains__(userInput):

            with open('readfrom.json', 'r') as openfile:

                # Reading from json file
                json_object = json.load(openfile)
                json_object2 = json.dumps(json_object, ensure_ascii=False)

            object = s3.Object(bucket.name, userInput)
            result = object.put(Body=json_object2)
            res = result.get('ResponseMetadata')

            if res.get('HTTPStatusCode') == 200:
                print(f"File Modified Successfully: {object.key}")
            else:
                print('File Not Modified')

        else:
            print("The file does not exist")

    else:
        print("Enter valid Operation Number")



