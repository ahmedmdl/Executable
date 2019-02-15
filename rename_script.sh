declare -i i num
i=0
for f in ../Mesh/*.stl
do
   mv -- "$f" "../Mesh/$i.stl"
   i=$i+1
done
