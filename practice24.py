
import re

data = 'Get jaewoonam@gmail.com Tue Win 5 02:13:20'
email = re.findall('\S+@\S+',data)
print(email)