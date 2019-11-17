rk4.png : segunda_parte.py segunda_parte.dat
	python segunda_parte.py

segunda_parte.dat : segunda_parte.x
	./segunda_parte.x > segunda_parte.dat
	
segunda_parte.x : segunda_parte.cpp
	c++ segunda_parte.cpp -o segunda_parte.x
	
clean:
	rm segunda_parte.x segunda_parte.dat rk4.png