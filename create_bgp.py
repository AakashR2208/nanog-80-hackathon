#!/usr/bin/env python3


#Importing all the required modules
try:
	import jinja2
	from jinja2 import Environment, FileSystemLoader
except:
	print('Please install required modules.')

global filelist
filelist=[]

# This function parses a config file to get the parameters and feeds those into a jinja 2 template
# writes the output of that template into a file and returns the filenames.
def get_config(filename):
	try:
		with open(filename) as f:
			data=eval(f.read())
	except:
		print('File not found!')
	
	files={}
	env=Environment(loader=FileSystemLoader('templates'))
	env.trim_blocks=True
	env.lstrip_blocks=True
	env.rstrip_blocks=True
	template=env.get_template('bgp.j2')
	for item in data:
		output=template.render(bgpinfo=data[item])
		filename=item+'_bgpconf.txt'
		f=open(filename,'w')
		f.write(output)
		f.close()
		files[item]=filename
		print('Configs for '+item+' strored in file named '+filename)
		
		
	return files

#Main function
def bgpconf_create():
	files=get_config('bgp_info.txt')
	for i in files.values():
		filelist.append(i)
	return(filelist)

if __name__=='__main__':
	bgpconf_create()
	
