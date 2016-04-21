# griochallenge
Grio Challenge code

##Usage Instructions
In order to run codingchallenge.py without error, the user's computer needs python 2.7, and to have pip installed. The user will run
``` 
pip install requests 
```
if they do not have the python requests package. 

Currently, the implementation can take in a file in the main method of codingchallenge.py. The file is passed as parameter to the function print_content(File). A file name can also be passed to the function in the python command line using the following sequence:

``` 
import codingchallenge
codingchallenge.print_content(<filename>)
``` 

##Overview of Design Decisions

###### Overall Design

The core functionality is handled in the translate_content() method. The original pseudo code is displayed below: 

```
For(all the lines in the file) {
	read one line of input file
	for (all the words in the line) {
		take each word, check if it is a 
		1. url (verification, ignore lat longs in a url regex: http:// or https:// 
			+ domain (whitelist characters?) 
			+ . 
			+ small number of address characters + and infinite number of /text/text/text)
		2. lat long -- regex should handle [+lat+,+long+]. 
				Verify that it's actually a place, and then print out its place then print out it. 
		3. Check and see if it has an odd number of characters, if it does, reverse it. 
		4. If it has an even number of characters, just print it out. 
	}
}
```
Methods are used throughout to make modular, easily testable code. Some of the functions have unit tests, but not all. 

The methodology that I used was to implement one feature until it works the way it’s supposed to, and then implement the next feature. My code searches for even and odd length strings, finds and snips url and finds latitudes and longitudes very well. I could have spent more time adjusting the code to make it work as expected in all cases but there was not enough time. 


###### Assumptions
1. I assumed that anything that is not a url and not coordinates is treated as a word, including numbers and dates. Since there was no specific instruction about what to do with them, that is how they are handled. 
2. I assumed printable meant printing to the console. The code is written so that if this requirement changed, it would be a very isolated fix. 
3. I assumed that a valid url would have http//: or https//: at the beginning, followed by a string of characters, and at some point a dot.
4. When reversing strings, I kept the end punctuation at the end but did not count punctuation when handling the length of the word
5. When counting the number of characters in a word, I chose to only count alphabetic characters.

###### Outstanding Questions, Bugs, and Work

1. Does the actually need print line by line or would an output file also suffice?
2. I did not handle punctuation well. I did not realize it was going to be a blocking point until it was too late. With more time, I would fix how the code treats punctuation to handle it in a more streamlined manner.
3. It was unclear how to handle hyphens and apostrophes when the number of characters is odd. The code as is reverses them with the rest of the characters. I could imagine treating each side of the hyphen as a separate word. 
4. My code doesn't verify that the latitude and longitude values return a valid address. It returns the default address format that the google API provides instead of the one given in the challenge specs. If I had another hour at home, this is what I would fix. 
5. Characters in other alphabets might not be readable in the current implementation (ex, no Cyrillic letters or Chinese characters).
6. The urls could be verified to make sure they are real urls. 
7. It would be nice to have a more user friendly input mechanism. 
8. Some of the code could be more parameter based. With a few more use cases, it would have been easier to write more recyclable code.

##Why Python

There are four languages I considered for the challenge. Python: fast programming time, many packages filled with functionality. Java: also great API, faster than python when running on huge files but more upfront coding time. PHP: built in well-formed URL functionality. Javascript: would translate quickly and easily to a UI. 

Because the challenged specified that the input file might be huge but the code also needed to be flexible. It was easiest for me to use a language I was comfortable with, so I chose python. The robust open source options for python made it an easy language to use for the challenge. There were many things I did not know how to do off the bat, but the online documentation for python is generally very good. Python is also a great middle ground – it would be easy to slap a UI on, or to make calls to a C++ backend. 

I spent about 3 hours writing code but more than that researching and refining the code.
