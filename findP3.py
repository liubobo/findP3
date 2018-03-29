#description: https://www.jianshu.com/p/7658f8700a1d
#put ipa and f.py in desktop
#excute path is desttop

ipa = './BaoXianBang.ipa'
des = './cer.zip'

import os
import json
import getpass 

os.system('rm -r ./Assets.car'  )
os.system('rm -r ./Assets.json'  )
os.system('rm -r ./cer.zip'  )
os.system('rm -r ./Payload'  )

os.system('cp '+ipa+' ' +des)
os.system('unzip ' +des)
os.chdir('./Payload/BaoXianBang.app')
os.system('cp '+ 'Assets.car' + ' ~/Desktop/Assets.car'  )
os.system('xcrun --sdk iphoneos assetutil --info ~/Desktop/Assets.car  > ~/Desktop/Assets.json')

os.system('rm -r ~/Desktop/Assets.car'  )
os.system('rm -r ~/Desktop/cer.zip'  )
os.system('rm -r ~/Desktop/Payload'  )

os.chdir('/Users/'+getpass.getuser()+'/Desktop/')
with open('./Assets.json') as f:
	data  = json.loads(f.read())
	for dict in data:
		is_error_pic = False
		if dict.has_key('Encoding'):
			if dict['Encoding'] == 'ARGB-16':
				is_error_pic = True
		if dict.has_key('DisplayGamut'):
			 if dict['DisplayGamut'] == 'P3':
			 	is_error_pic = True

		if is_error_pic:
			print  'error pic------------->'+ dict['RenditionName']

os.system('open ~/Desktop/Assets.json'  )
