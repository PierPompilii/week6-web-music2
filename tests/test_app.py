from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(db_connection, test_web_address, page):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    p_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        "Lateralus",
        "The Hunter"
    ])
    expect(p_tags).to_have_text([
        "Released: 2001",
        "Released: 2011"
    ])
    
# a test to get all the artists
def test_get_artists(db_connection, test_web_address, page):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/artists")
    h2_tags = page.locator("h2")
    p_tags = page.locator("p")
    expect (h2_tags).to_have_text([
        "Tool",
        "Mastodon"
    ])
    expect(p_tags).to_have_text([
        "Genre: Rock",
        "Genre: Rock"
    ])
    
    
def test_get_album_one(db_connection, test_web_address, page):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tags = page.locator("h1")
    p_tags = page.locator("p")
    expect(h1_tags).to_have_text(["Lateralus"])
    expect (p_tags).to_have_text([
        "Released: 2001",
        "Artist: Tool"
    ])
    
    
def test_get_artist_only_one(db_connection, test_web_address, page):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tags = page.locator("h1")
    p_tags = page.locator("p")
    expect(h1_tags).to_have_text(["Tool"])
    expect(p_tags).to_have_text([
        "Genre: Rock"
        "Album: Lateralus"
    ])