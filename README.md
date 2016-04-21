# griochallenge
Grio Challenge code

##Usage Instructions
In order to run codingchallenge.py without error, the user's computer needs python 2.7, and to have pip installed. The user will run
``` 
pip install requests 
```
if they do not have the python requests package. 

Currently, the implemenation can take in a file in the main method of codingchallenge.py. The file is passed as parameter to the function print_content(File). A file name can also be passed to the function in the python command line using the following sequence:

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
		1. url (verfication, ignore lat longs in a url regex: http:// or https:// + domain (white list characters?) + . + small number of address characters + and infinite number of /text/text/text)
		2. lat long -- regex should handle [+lat+,+long+]. Verify that it's actually a place, and then print out its place then print out it. 
		3. Check and see if it has an odd number of characters, if it does, reverse it. 
		4. If it has an even number of characters, just print it out. 
	}
}
```
Methods are used throughout to make modular, easily testable code. Some of the functions have unit tests, but not all. S


###### Assumptions
1. I assumed that anything that is not a url and not coordinates is treated as a word, including numbers and dates. Since there was no specific instuction about what to do with them, that is how they are handled. 
2. I assumed print out meant printing to the console. The code is written so that if this requirement changed, it would be a very isolated fix. 

4. I assumed that a valid url would have http//: or https//: at the beginning, followed by a string of characters, and at some point a dot.
5. When reversing strings, I kept the end punctuation at the end but did not count punctionation when handling the length of the word
6. When counting the number of characters in a word, I chose to only count alphabetic characters.

###### Outstanding Questions, Bugs and Work

1. Does the actually need to go line by line or would an output file also suffice?
2. That the latitude and longitude inputs need better handling.
3. I did not anticipate dealing with punctation very well. I did not realize it was going to be a blocking point until it was too late. With more time, I would fix how the code treats punctation to handle it in a more streamlined manner.
4. It was unclear how to handle hyphens and apostrophes when the number of characters is odd. The code as is reverses them with the rest of the characters.
5. My code doesn't verify that the latitude and longitude values return a valid address. It also does not return the format given.
6. Characters in other alphabets might not be readable in the current implementation (ex, no crylic letters or chinese characters).
7. The urls could be verified to make sure they are real urls. 
8. It would be nice to have a more user friendly input mechanism. 

##Why Python

There are four languages I considered for the challenge. Python: fast programming time, many packages filled with functionality. Java: also great API, faster than python but more upfront coding time. PHP: built in well-formed URL functionality. Javascript: whould translate quickly and easily to a UI. 

Because the challenged specified that the input file might be huge, but also might need to be flexible but quick to write, I chose python. The robust open source options for python made it an easy language to use for the challenge.