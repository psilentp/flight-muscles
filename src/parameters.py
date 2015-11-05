import os
uname = os.getlogin()

params = {"root_dir":"FlyDB/",
	  "platform_paths":{"darwin":"/Volumes/FlyDataC/",
			            "linux2":"/media/%s/FlyDataC/"%(uname)}}
