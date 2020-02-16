from lyr.providers import google

def test_google():
    query = "ellie goulding your song"
    expected = """It's a little bit funny,
This feeling inside
I'm not one of those
Who can easily hide
I don't have much money,
But boy if I did
I'd buy a big house where
We both could live
So excuse me forgetting,
But these things I do
See I've forgotten
If they're green or they're blue
Anyway the thing is what I really mean
Your eyes are the sweetest eyes
I've ever seen
And you can tell everybody
This is your song
It may be quite simple,
But now that it's done
I hope you don't mind,
I hope you don't mind
That I put down in words
How wonderful life is
Now you're in the world
If I was a sculptor,
But then again no
Or a girl who makes potions in
A traveling show
I know it's not much, but
It's the best I can do
My gift is my song, and
This one's for you
And you can tell everybody
This is your song
It may be quite simple,
But now that it's done
I hope you don't mind,
I hope you don't mind
That I put down in words
How wonderful life is
Now you're in the world."""
    actual = google.lyrics(query)
    assert actual == expected