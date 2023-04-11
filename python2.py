import simple.simple_pb2 as simple_pb2


def addToBinRead(title,content):
    simple_message = simple_pb2.SimpleMessage()
    simple_message.id = 123
    simple_message.is_simple = True
    simple_message.name = title
    sample_list = simple_message.sample_list
    sample_list.append(content)


    with open("simple.bin", "wb") as f:
        print("write as binary")
        bytesAsString = simple_message.SerializeToString()
        f.write(bytesAsString)


    with open("simple.bin", "rb") as f:
        print("read values")
        simple_message_read = simple_pb2.SimpleMessage().FromString(f.read())

    return simple_message_read


simple_message_read = addToBinRead("youself title","your content")

print("Is Simple?: " + str(simple_message.is_simple))
print("Id?: " + str(simple_message.id))
