import eel

@eel.expose
def crypt(string, key):
	res = ''
	for i in range(len(string)):
		res += chr(ord(string[i]) + key)
	eel.display('d_text', res)
@eel.expose
def decrypt(string, key):
	res = ''
	for i in range(len(string)):
		res += chr(ord(string[i]) - key)
	eel.display('e_text', res)

eel.init('web')

eel.start('main.html', size=(700,400))
