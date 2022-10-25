import base64

l = input('Link: ')

link = base64.b64encode(l.encode("utf-8"))

print(link)
print('\nPut it in a file? Then press enter.')
input()
open('link.txt', 'wb').write(link)