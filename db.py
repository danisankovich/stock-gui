# import sqlite3

# cnt = sqlite3.connect("watchlist.dp")
# cnt.execute('''CREATE TABLE watchlist(
#             SYMBOL TEXT);''')

# cnt.execute('''INSERT INTO watchlist(SYMBOL) VALUES('AAPL')''')

# cnt.commit()

# vals = cnt.execute('''SELECT * from watchlist''')

# for i in vals:
#     print(i[0])
