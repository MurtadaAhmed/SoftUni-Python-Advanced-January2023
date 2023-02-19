def add_songs(*args):
  dictionary = {}
  for song_name, lyrics in args:
    if song_name not in dictionary:
      dictionary[song_name] = []
    dictionary[song_name].extend(lyrics)

  songs_as_list = []
  for key, values in dictionary.items():
    songs_as_list.append(f"- {key}")
    if values:
      for value in values:
        songs_as_list.append(value)
        
  return "\n".join(songs_as_list)

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))