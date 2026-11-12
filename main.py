#pip = python's package installer


import tiktoken

enc=tiktoken.encoding_for_model("gpt-4o")

text="Myself Rakesh Bhandary"

#Encoding
encodedData=enc.encode(text)
print("Encoded Details",encodedData)

#Decoding
tokenData=[5444, 1156, 460, 6861, 71, 418, 5172, 815]
decodedData=enc.decode(tokenData)
print("Decoded Details", decodedData)



