def unixTott2k(unix_sec: int, micro_sec: int) -> int:

	# Desending order offset times.  Mapping between unix time and TT2000
	# proceeds at constant rate of 1e9 to 1 after each leap second.  The
	# Each line in the chart below represents the instant in time *after*
	# each leap second.  Prior to 1972-01-01 the rate of UNIX ticks to
	# TT2000 ticks is not 1e9, but some other value that I don't know.
	
	nOffsets = 29
	offsets = [
		[ 1483228800 ,  536500869184000000 ], # 2017-01-01    0 
		[ 1435708800 ,  488980868184000000 ], # 2015-07-01    1
		[ 1341100800 ,  394372867184000000 ], # 2012-07-01    2
		[ 1230768000 ,  284040066184000000 ], # 2009-01-01    3
		[ 1136073600 ,  189345665184000000 ], # 2006-01-01    4
		[  915148800 ,  -31579135816000000 ], # 1999-01-01    5
		[  867715200 ,  -79012736816000000 ], # 1997-07-01    6
		[  820454400 , -126273537816000000 ], # 1996-01-01    7
		[  773020800 , -173707138816000000 ], # 1994-07-01    8
		[  741484800 , -205243139816000000 ], # 1993-07-01    9
		[  709948800 , -236779140816000000 ], # 1992-07-01   10
		[  662688000 , -284039941816000000 ], # 1991-01-01   11
		[  631152000 , -315575942816000000 ], # 1990-01-01   12
		[  567993600 , -378734343816000000 ], # 1988-01-01   13
		[  489024000 , -457703944816000000 ], # 1985-07-01   14
		[  425865600 , -520862345816000000 ], # 1983-07-01   15
		[  394329600 , -552398346816000000 ], # 1982-07-01   16
		[  362793600 , -583934347816000000 ], # 1981-07-01   17
		[  315532800 , -631195148816000000 ], # 1980-01-01   18
		[  283996800 , -662731149816000000 ], # 1979-01-01   19
		[  252460800 , -694267150816000000 ], # 1978-01-01   20
		[  220924800 , -725803151816000000 ], # 1977-01-01   21
		[  189302400 , -757425552816000000 ], # 1976-01-01   22
		[  157766400 , -788961553816000000 ], # 1975-01-01   23
		[  126230400 , -820497554816000000 ], # 1974-01-01   24
		[   94694400 , -852033555816000000 ], # 1973-01-01   25
		[   78796800 , -867931156816000000 ], # 1972-07-01   26
		[   63072000 , -883655957816000000 ], # 1972-01-01   27
		# Mapping is not linear for dates below Jan. 1st, 1972. The actual 
		# mapping is:
		#[          0 , -946727959814622001 ] # 1970-01-01   28
		# but we want a constant slope of 1e9, so using this value instead:
		[          0 , -946727958816000000 ] # 1970-01-01    28
	]

	i=0
	for x in range(0, nOffsets):
		i = x
		if(unix_sec >= offsets[i][0]): 
			break

	tt2k = 0
	if( i >= nOffsets ):
		# Handle negative times, since I guess that's a thing for really bad packets
		assert(unix_sec <= 0, "Time handling logic error")

		# Leap seconds weren't a thing before 1970, use whole unix time
		tt2k = unix_sec*1000000000 + offsets[nOffsets-1][1]
	
	else:
		tt2k = (unix_sec - offsets[i][0])*1000000000 + offsets[i][1]
	

	tt2k += micro_sec * 1000
	return tt2k

