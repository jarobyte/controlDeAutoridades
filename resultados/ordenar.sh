ls|egrep "([0-9]+\-[0-9]+)\\)x\\(\\1"|xargs mv -t meta-nodos
ls|egrep "1200000\\)$"|xargs mv -t alfa
ls|egrep "\\(6"|xargs mv -t beta
rm parejas--import_datos_registros.csv--\(300000-360000\)x\(1200000-1700555\) 
rm parejas--import_datos_registros.csv--\(360000-420000\)x\(1200000-1700555\) 
rm parejas--import_datos_registros.csv--\(420000-480000\)x\(1200000-1700555\) 
mv parejas--import_datos_registros.csv--\(* gamma
