import model
from model import Song, LocalCount, GlobalCount, session
import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy import distinct, func
import re
import sys
import json
from pprint import pprint
import pdb

def load_scraped_lyrics_file(filename):
    """Open a file with raw song data. Turn it into a Python object. Return it."""
    file = open(filename)
    song_list = json.load(file)

    lyrics_data = []
    list_of_wordcounts = []

    for song in song_list:
        # makes a dictionary for each song
        song_dict = {}
        song_dict['url'] = song['url']
        song_dict['artist'] = song['artist']
        song_dict['songname'] = song['title']
        if len(song_dict['songname']) > 64:
            break
        else:
            song_dict['lyrics'] = song['lyrics']

        # nests each song dictionary within a larger lyrics_analysis dictionary
        lyrics_data.append(song_dict)

    return lyrics_data, list_of_wordcounts

def load_songs(lyrics_data):
    """
    Add songs to the songs table.
    """
    # i = 0

    # go through each song dictionary and extract data
    for song_dictionary in lyrics_data:
        # if i < 5:
            # check whether the song already exists in the database
        if session.query(Song).filter(Song.url == song_dictionary['url']).first():
            print "%r is already in the database!" % song_dictionary['songname']
        else:
            # let's turn this song... into a Song!
            # make a new row in the songs table
            url = song_dictionary['url']
            artist = song_dictionary['artist']
            songname = song_dictionary['songname']

            new_song = Song(url = url,
                            artist = artist,
                            songname = songname)

            session.add(new_song)
            print "SUCCESS! %r is such a jam." % new_song.songname
                # i += 1
    session.commit()

def load_localcounts(lyrics_data, list_of_wordcounts):
    """
    Adds local wordcounts for each song.
    """
    # i = 0

    for song_dictionary in lyrics_data:
        # if i < 5:
        url = song_dictionary['url']
        # put on your counting shoes
        for k, v in song_dictionary.iteritems():
            lyrics = song_dictionary['lyrics']
            unique_words = {}

            for line in lyrics:
                line = line.lower()
                words = re.findall('\w+', line)

                # unique words for each song
                for word in words:
                    if unique_words.get(word):
                        unique_words[word] += 1
                    else:
                        unique_words[word] = 1

        # make all the localcount rows for that song
        for word, localcount in unique_words.iteritems():
            new_row = LocalCount(song_id = url, term = word, count = localcount)
            print "Adding %r with count of %r" % (new_row.term, new_row.count)
            session.add(new_row)
            # i += 1
        session.commit()
        list_of_wordcounts.append(unique_words)

    return list_of_wordcounts

def load_globalcounts(list_of_wordcounts):
    """
    Adds wordcounts for all unique words. There should only be one row per unique word.
    """
    # i = 0

    for localcount_dict in list_of_wordcounts:
        # if i < 5:
        for word, count in localcount_dict.iteritems():
            item = session.query(GlobalCount).filter(GlobalCount.term == word).first()
            if item:
                print "%r is already in globalcounts. Updating count..." % word
                # update the global count for this word, because we have added new songs with more occurrences of this word
                q = session.query(LocalCount.term, func.sum(LocalCount.count))
                q = q.group_by(LocalCount.term)
                q = q.filter(LocalCount.term == word)
                results = q.all()

                # print "Current count for %r is %d" % (item.term, item.count)
                item.count = results[0][1]
                print "Updating %r's count to %d" % (item.term, item.count)
                session.commit()

            else:
                print "%r not in globalcounts table, creating new row" % word
                qq = session.query(LocalCount.term, func.sum(LocalCount.count))
                qq = qq.group_by(LocalCount.term)
                qq = qq.filter(LocalCount.term == word)
                resultsresults = qq.all()

                countcount = resultsresults[0][1]
                new_row = GlobalCount(term = word, count = countcount)
                session.add(new_row)
                # you must commit before you query the same word/item again!
                session.commit()
            # i += 1

def main():
    # lyrics_data, empty_list_of_wordcounts = load_scraped_lyrics_file("seed_data/taylor_swift_lyrics.json")
    load_songs(lyrics_data)
    list_of_wordcounts = load_localcounts(lyrics_data, empty_list_of_wordcounts)
    load_globalcounts(list_of_wordcounts)

if __name__ == "__main__":
    # call each of the load functions with the session as an argument
    main()