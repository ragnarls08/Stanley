echo 'OK'
grep 'OOOOOOk' 'logfile.log'|wc -l
echo 'long'
grep 'LLLLLLong' 'logfile.log'|wc -l
echo 'short'
grep 'SSSSSShort' 'logfile.log'|wc -l
echo 'HTTP403'
grep 'HTTP Error 403' 'logfile.log'|wc -l
