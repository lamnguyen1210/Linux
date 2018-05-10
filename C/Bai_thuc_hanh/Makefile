all: test-mymath

test-mymath: test-mymath.o giaithua.o tongchan.o tongle.o luythua.o
	gcc -o test-mymath test-mymath.o giaithua.o tongchan.o tongle.o luythua.o -lm
test-mymath.o: test-mymath.c mymath.h
	gcc -c test-mymath.c
giaithua.o: giaithua.c mymath.h
	gcc -c giaithua.c
tongchan.o: tongchan.c mymath.h
	gcc -c tongchan.c
luythua.o: luythua.c mymath.h
	gcc -c luythua.c

test:
	./test-mymath

mymath.h:

clean:
	rm -f test-mymath
