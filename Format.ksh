[ -f final.txt ] && rm -f final.txt
echo "________________________________________________________________" >> final.txt
echo "Location Position Local Time Conditions Temperature Pressure Humidity" >> final.txt
echo "________________________________________________________________" >> final.txt
cat output.txt | while read line
do
	if [ ${#line} -ge 10 ]
	then
		city=`echo $line | cut -d '|' -f1` 
		latlong=`echo $line | cut -d '|' -f2` 
		dt=`echo $line | cut -d '|' -f3` 
		status=`echo $line | cut -d '|' -f4`
		t1=`echo $line | cut -d '|' -f5` 
		p1=`echo $line | cut -d '|' -f6`
		humid=`echo $line | cut -d '|' -f7` 
		temp=`echo $t1 | cut -d ':' -f2 | cut -d ',' -f1`
		pres=`echo $p1 | cut -d ':' -f2 | cut -d ',' -f1`
		echo "$city| $latlong| $dt| $status| $temp| $pres| $humid" >> final.txt
	fi
done
echo "________________________________________________________________" >> final.txt
