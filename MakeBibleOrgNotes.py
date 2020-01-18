#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Create files and structure for Bible Notes

In a directory, create a set of files, one per Bible book. In each file, insert
some basic Org info in the header, and create the main strucutre, with a top
level org-mode heading for each chapter of the book.

These files will be used for storing notes on the Bible.
"""
# Author: Andy Holt
# Date: Fri 14 Sep 2018 19:15
# Usage: Run once, then it won't really be useful again.

import os

# list of books of the Bible, with the number of chapters in the book
books_chapters_list = [['Genesis', 50], ['Exodus', 40], ['Leviticus', 27],
                       ['Numbers', 36], ['Deuteronomy', 34], ['Joshua', 24],
                       ['Judges', 21], ['Ruth', 4], ['1 Samuel', 31],
                       ['2 Samuel', 24], ['1 Kings', 22], ['2 Kings', 25],
                       ['1 Chronicles', 29], ['2 Chronicles', 36], ['Ezra', 10],
                       ['Nehemiah', 13], ['Esther', 10], ['Job', 42],
                       ['Psalms', 150], ['Proverbs', 31], ['Ecclesiastes', 12],
                       ['Song of Songs', 8], ['Isaiah', 66], ['Jeremiah', 52],
                       ['Lamentations', 5], ['Ezekiel', 48], ['Daniel', 12],
                       ['Hosea', 14], ['Joel', 3], ['Amos', 9], ['Obadiah', 1],
                       ['Jonah', 4], ['Micah', 7], ['Nahum', 3],
                       ['Habakkuk', 3], ['Zephaniah', 3], ['Haggai', 2],
                       ['Zechariah', 14], ['Malachi', 4],
                       ['Matthew', 28], ['Mark', 16], ['Luke', 24],
                       ['John', 21], ['Acts', 28], ['Romans', 16],
                       ['1 Corinthians', 16], ['2 Corinthians', 13],
                       ['Galatians', 6], ['Ephesians', 6], ['Philippians', 4],
                       ['Colossians', 4], ['1 Thessalonians', 5],
                       ['2 Thessalonians', 3], ['1 Timothy', 6],
                       ['2 Timothy', 4], ['Titus', 3], ['Philemon', 1],
                       ['Hebrews', 13], ['James', 5], ['1 Peter', 5],
                       ['2 Peter', 3], ['1 John', 5], ['2 John', 1],
                       ['3 John', 1], ['Jude', 1], ['Revelation', 22]]

# Loop through the books. `enumerate` function gives index and contents
for bk_index, book in enumerate(books_chapters_list):
    file_name = book[0].replace(' ', '') + '.org'
    file_contents = "#+TITLE: Notes on %s\n" % book[0]
    file_contents+="#+STARTUP: content\n\n"
    file_contents+="* %s introductory matters\n" % book[0]
    for ch in range(book[1]):
        file_contents+="* %s %d\n" % (book[0], ch+1)
    with open(file_name, 'w') as f:
        f.write(file_contents.encode('utf8'))
    
