all: test-mymath

test-mymath: test-mymath.o libmymath.a
	gcc -o test-mymath test-mymath.o libmymath.a -lm
test-mymath.o: test-mymath.c 
	gcc -c test-mymath.c

test:
	./test-mymath

mymath:
	ar crv mymath.a luythua.o tongchan.o tongle.o giaithua.o

clean:
	rm -f test-mymath
