all: evalb

evalb: evalb.c
#	gcc -Wall -g -o evalb evalb.c
#	g++ -Wall -g -o evalb evalb.cpp -fpermissive
	g++ -w -g -o evalb evalb.cpp -fpermissive

