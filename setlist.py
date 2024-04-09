from repertorio import Repertorio

api = Repertorio('API key')

ArtistSearch = input("Which artist would you like to search for ?")

Artist = api.artists(artistName=ArtistSearch, sort='relevance')
#Setlist = api.setlists(artistName=ArtistSearch, year='2024')

print(Artist)

print("------")

#print(Setlist)
