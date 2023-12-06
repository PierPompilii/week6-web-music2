import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route("/albums")
def get_albums():
    connection = get_flask_database_connection (app)
    repository = AlbumRepository (connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)

@app.route("/artists")
def get_artists():
    connection = get_flask_database_connection (app)
    repository = ArtistRepository (connection)
    artists = repository.all()
    return render_template("artists/index.html", artists=artists)


@app.route("/albums/<id>")
def get_album_one(id):
    connection = get_flask_database_connection (app)
    repository_album = AlbumRepository(connection)
    repository_artist = ArtistRepository(connection)
    album = repository_album.find(id)
    artist = repository_artist.find(album.artist_id)
    return render_template("albums/find.html", artist=artist, album=album)
    
@app.route("/artists/<id>")
def get_artists_only_one(id):
    connection = get_flask_database_connection (app)
    repository_artist = ArtistRepository(connection)
    repository_album = AlbumRepository(connection)
    artist = repository_artist.find(id)
    albums = []
    for album in repository_album.all():
        if artist.id == album.artist_id:
            albums.append(album)
    
    return render_template("artists/find.html", artist=artist, albums=albums)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
