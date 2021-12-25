type_list = [1, 1.1, complex(1, 2), "string", [1, 2, 3], (1, 2, 3), {1, 2, 3}, {"hello": 1, "world": 2},
             True, b'text', bytearray(b"some text"), None]
types = [int, float, complex, str, list, tuple, set, dict, bool, bytes, bytearray, type(None)]
for index, element in enumerate(type_list):
    if type(element) is types[index]:
        print(f"Type is right: {str(type(element))[8:-2]}")
    else:
        print("Wrong type")
