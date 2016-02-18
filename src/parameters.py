import getpass
uname = getpass.getuser()

if uname == 'psilentp':
    params = {"root_dir":"""FlyDB/""",
          "platform_paths":{"darwin":"/Volumes/FlyDataC/",
                            "linux2":"/media/FlyDataC/",
                            "win32":"F:\\"}}
else:
    params = {"root_dir":"""FlyDB/""",
              "platform_paths":{"darwin":"/Volumes/FlyDataC/",
                               "linux2":"/media/%s/FlyDataC/"%(uname),
                                "win32":"F:\\"}}
