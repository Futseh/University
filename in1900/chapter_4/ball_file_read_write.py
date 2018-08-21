# Exercise 4.14 a

from numpy import linspace

def file_read(filename):
	infile = open(filename, 'r')
	data = [line.split() for line in infile]

	t = []

	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j] == 'v0:' or data[i][j] == 't:':
				if data[i][j] == 'v0:':
					v0 = float(data[i][j+1])
			else:
				t.append(float(data[i][j]))

	t.sort(key=float)
	return v0, t

print(file_read('ball.dat'))

# Exercise 4.14 b

def test_file_read():
	v1 = 3

	file = open('ball2.dat', 'w')
	file.write('v0: %.2f\n' % v1)
	file.write('t:\n')

	tt = linspace(0, 1, 26)

	for j in tt:
		file.write('%.7f\n' % j)

	file.close()
	v0, t = file_read('ball2.dat')

	if v0 == v1 and (t-tt).any():
		return 'success'
	else:
		return 'You have failed in life'

print(test_file_read())

# Exercise 4.14 c

# Outputfile is the name of the file the output is going to be written in
# Inputfile is the file which we need to send through the file_read function to get the values
def output_file(outputfile, inputfile):
	v0, t = file_read(inputfile)
	g = 9.81
	y = []

	outfile = open(outputfile, 'w')

	for i in t:
		yt = v0*i - 0.5*g*i**2
		if yt < 0: # Just to check if the height is negative and if it is go out of the loop
			break
		else:
			y.append(yt)

	outfile.write('---------------------\n')
	outfile.write('Time \t\t\t Height \n')

	for i in range(len(y)):
		outfile.write('%.5f \t %.5f \n' % (t[i], y[i]))

	outfile.write('---------------------')
	outfile.close()

output_file('ball3.dat', 'ball2.dat')

"""
Terminal> python3 ball_file_read_write.py
		(3.0, [0.042, 0.0519085, 0.10262264, 0.1117, 0.15592, 0.17383923, 0.2094294, 0.21342619, 0.21385894, 0.27, 0.28075, 0.29584013, 0.3464815, 0.35, 0.36807889, 0.372985, 0.39325246, 0.50620017, 0.528, 0.53012, 0.57681501876, 0.57982969])
		success
"""
