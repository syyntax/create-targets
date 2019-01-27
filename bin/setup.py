import os
import shutil

# Setup the man page
src = os.path.dirname(os.path.abspath(__file__))
dst = '/usr/share/man/man8'

shutil.copyfile('{}'.format(os.path.abspath(os.path.join(src, '..', 'data', 'create-targets.8'))),
                '/usr/share/man/man8/create-targets.8')
os.system('gzip -f /usr/share/man/man8/create-targets.8')
shutil.copyfile('{}/create-targets.py'.format(src), '/usr/local/bin/create-targets')
os.system('sudo chmod +x /usr/local/bin/create-targets')

print("Complete.\n")
