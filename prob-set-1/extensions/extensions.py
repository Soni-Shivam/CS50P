x= (input("Enter - ").lower().partition("."))[-1]
if x == 'jpg' or x == 'jpeg':
    print('image/jpeg')
elif x == 'gif':
    print('image/gif')
elif x == 'png':
    print('image/png')
elif x == 'zip':
    print('application/zip')
elif x == 'pdf':
    print('application/pdf')
elif x == 'txt':
    print('text/plain')
else :
    print('application/octet-stream')