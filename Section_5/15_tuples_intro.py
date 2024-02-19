albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974,),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
        ]

print(len(albums))

# My Solution
for album, (name, artist, year) in enumerate(albums): 
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

# Course solution #1
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

# Course solution #1
for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
