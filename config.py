release = '0.1.a'
download_link = 'https://mega.nz/#F!1K4nRaoY!d7xFqXBNo5MC978lcTMfRw'
download_msg = '''
releax %s release is a unstable alpha release, 
and might have serious error and issues which might harm your system,
current release is only avaliable to test under virtual environment
such qemu and virtualbox, releax x.y.a means the alpha release
which targets the developers and beta tester to test and report the
issues, if you are not a beta tester or no experience with any linux
distro then you are not adviced to use it.
please read the handbook to check how to test the current releax %s release
''' % (release,release)

releax_os_define = open('static/data/wiki/releax.define').read()