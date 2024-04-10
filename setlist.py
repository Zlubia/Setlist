from repertorio import Repertorio

api = Repertorio('')

ArtistName = input("Which artist would you like to search for ?")

ArtistSearch = api.artists(artistName=ArtistName, sort='relevance')


"""----- ADD a validation step here, if the first one in the list is not ok, check the second,etc..."""
Artist = ArtistSearch['artist'][0] #[0] is the first result of the search
ArtistMbid = Artist["mbid"]

print(Artist)

print("------")

Setlist = api.artist_setlists(ArtistMbid)

print(Setlist["setlist"])
