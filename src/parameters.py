import getpass
uname = getpass.getuser()

params = {"root_dir":"""FlyDB/""",
	  "platform_paths":{"darwin":"/Volumes/FlyDataC/",
			            "linux2":"/media/%s/FlyDataC/"%(uname),
                        "win32":"F:\\"}}
