import facial_landmarks as fl

def test_facial_landmarks():

    with open('image_base64.txt', 'r') as file:
        image_base64__ = file.read()
        # image_base64__.replace(" ", "")

    relations_result =fl.facial_landmarks(image_base64__)

    return 0

test_facial_landmarks()