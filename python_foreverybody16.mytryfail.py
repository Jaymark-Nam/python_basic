

import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite') #connect
cur = conn.cursor() #cursor is our handle. open and send SQL's order

cur.execute('DROP TABLE IF EXISTS Counts') #if it exists...

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')  #CREATE TABLE -- org, count   

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    y = re.findall('^From.+@(\S+)', line)
    z = y[0].split('.')
    org = z[0]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()        #grab the first one
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

