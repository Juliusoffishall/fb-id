import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("File").lisensi()
elif 'aarch' in arc:
	__import__("File64").lisensi()
else:
	exit(f' Unknow device machine {arc}')
