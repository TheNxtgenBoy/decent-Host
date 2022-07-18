from requests import session
from random import randint as ri
import tkinter
from tkinter.filedialog import askopenfilename

class Upload():
	def __init__(self):
		tkinter.Tk().withdraw()
		self.session = session()
		self.main_loop()

	def main_loop(self):
		print("""
╔╦╗┌─┐┌─┐┌─┐┌┐┌┌┬┐┬ ┬┌─┐┌─┐┌┬┐
 ║║├┤ │  ├┤ │││ │ ├─┤│ │└─┐ │ 
═╩╝└─┘└─┘└─┘┘└┘ ┴ ┴ ┴└─┘└─┘ ┴  v.Alpha\n\n""")
		while True:
			cmd = input(">> ")
			if cmd.strip().lower() == "upload":
				self.upload()
			if cmd.strip().lower() == "exit":
				break

	def upload(self):
		file_path = askopenfilename()
		if len(file_path) != 0:
			if file_path.split('.')[-1] in ['jpg', 'png']:
				try:
					print('Uploading...\r',end="")
					file = open(file_path, 'rb').read()
					r = self.session.post("https://api.nftport.xyz/v0/files",
					    headers={"Authorization": self.get_api()},
					    files={"file": file}
					).json()['ipfs_url']
					r = self.session.get(f'https://clck.ru/--?url={r}')
					print(f'Uploaded - {r.text}')
				except:
					print('Uploading Error')
			else:
				print('File Format must be jpg or png')

	def get_api(self):
		apis = ['6cc4a588-858e-4b07-b528-0aa77496da07', 'a146349c-90d6-4456-9916-9223c7b72a73', '6ae73c1b-6fbc-4886-a480-4f11b066082e', '7660150c-0eef-4c23-818a-ac178820440a', '7c2cbfca-b32e-4a1f-9ec0-f83d7ea6bf48']
		return apis[ri(0,len(apis)-1)]

if __name__ == "__main__":
	Upload()