set terminal pdf
set dummy t, y
set format x "%3.2f" 
set format y "%3.2f" 
set format z "%3.2f" 
unset key
set style increment default
set parametric
set samples 1000, 1000
set style data lines
set style function dots
set xrange [ 0.00000 : 1.00000 ] noreverse nowriteback
set x2range [ * : * ] noreverse writeback
set yrange [ 0.00000 : 1.00000 ] noreverse nowriteback
set y2range [ * : * ] noreverse writeback
set zlabel "rand(n + 2) ->" 
set zlabel  offset character 0, -1, 0 font "" textcolor lt -1 rotate parallel
set zrange [ 0.00000 : 1.00000 ] noreverse nowriteback
set cbrange [ * : * ] noreverse writeback
set rrange [ * : * ] noreverse writeback
plot rand(0), rand(0)
