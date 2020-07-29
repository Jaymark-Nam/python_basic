

#Finding the organization code. By Jae Mark Nam

import re

x = 'From stephen.marquard@hamell.ac.za Sat Jan  5 09:14:16 2008'

y = re.findall('^From.+@(\S+)', x)

z = y[0].split('.')

w = z[0]

print(w)