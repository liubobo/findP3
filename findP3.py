#coding=utf-8
#description: https://www.jianshu.com/p/7658f8700a1d
#./findP3.py ipa_path

import os,sys
import json
import getpass 

ipa = sys.argv[1]
des = './cer.zip'
f_name = os.path.basename(ipa).split(".")[0]

def remove_res():
	os.system('rm -r  ./Assets.car')
	os.system('rm -r ./cer.zip'  )
	os.system('rm -r ./Payload'  )

remove_res()
os.system('rm -r ./Assets.json'  )

os.system('cp '+ipa+' ' +des)
os.system('unzip ' +des)
os.chdir('./Payload/'+f_name+'.app')
os.system('cp '+ 'Assets.car' + ' ../../Assets.car'  )
os.chdir('../../')
os.system('xcrun --sdk iphoneos assetutil --info ./Assets.car  > ./Assets.json')

remove_res()

with open('./Assets.json') as f:
	data  = json.loads(f.read())
	hasError = False

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
			hasError = True

	if hasError:
		os.system('open ./Assets.json'  )
	else:
		os.system('rm -r ./Assets.json')

		print '---------没有找到错误图片------\n'*3
		 



