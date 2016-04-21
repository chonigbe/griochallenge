# griochallenge
Grio Challenge code so people can see it 


There are three languages I considered for the challenge. Python: fast programming time, many good packages filled with functionality. Java: also great API, faster than python but more upfront coding time. PHP: built in well-formed URL functionality. Javascript: whould translate quickly and easily to a UI. 

Because the challenged specified that the input file might be huge, but also might need to be flexible but quick to write, I chose python. 

Questions: does it actually need to go line by line or would an output file also suffice?
base code:
For(all the lines in the file) {
	read one line of input file
	for (all the words in the line) {
		take each word, check if it is a 
		1. url (verfication, ignore lat longs in a url regex: http:// or https:// + domain (white list characters?) + . + small number of address characters + and infinite number of /text/text/text) (before you start writing you have to figure out what this is going to involve)
		2. lat long (do verification to make sure) regex that handles [+lat+,+long+] and then verify that it's actually a place and then print out its place then print out it. 
		3. Check and see if it has an odd number of characters, if it does, reverse it. 
		4. If it has an even number of characters, just print it out. 
	}
}
Things I am assuming: 
1. That anything that is not a url and not a lat long is treated as a word, including numbers, dates etc since there was no specific instuction about what to do with them.
2. That when you said print out, you meant print to the console. The code is written so that if this requirement changed, it would be a very isolated fix. 
3. That the lat longs need verfication so we don't get back weird stuff from google (see what kind of weird stuff you can get back, its in the api just go look at it) 
4. Assumtions made about urls:
right now it just takes off anything that has those two string in front of it
5. When reversing strings, I kept the end punctuation at the end but did not count punctionation when handling the length of the word

Known bugs:
1. Punctation checks do not handle spanish upsidedown exclaimation points
2. More clarity needed about hypened words, under scores between words, apostrophes. 

how to do this work: 
0. take in an input file and print out what is given line by lineX
1. reversing and not revesing normal words testX
2. verfication of urls using a regex. test throughly, dont forget large inputsX
3. verfication of lat long using a regex. test throughly, dont forget large inputsX
3. Print out the changed url
3.5 Regression testingX
4. learn how to connect to a url http://docs.oracle.com/javase/tutorial/networking/urls/connecting.html
5. properly form urls
6. https://developers.google.com/maps/documentation/geocoding/intro
6. parse the xml you get back either by a home grown solution or use: https://github.com/FasterXML/jackson
7. print out the properly formed address after the lat,long

extra stuff:
8. verify URL is real. // not sure how important this is, that's why it's at the end. 
9. have multiple input methods, either console or direct input. 
10. put a basic ui on top of the backend, or at least make it easy to do this. It's pretty easy as is?
