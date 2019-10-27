#/bin/sh
twint -s jetblue --since "$(cat lastupdate)" -pt -o test-cases.csv --csv
echo $(date --rfc-3339=seconds | cut -d- -f1-3) > lastupdate
mv ../fileupdate.py .
python3 filechanger.py

echo "<!DOCTYPE HTML>" > ../../web/words.html
echo "<head><title> Most Associated Words </title>
<link href="https://fonts.googleapis.com/css?family=Staatliches&display=swap" rel="stylesheet">
  <link rel = "stylesheet" href="../../web/style.css"> <head>" >> ../../web/words.html
echo "<body>" >> ../../web/words.html
cat Wordreview.csv >> ../../web/words.html
echo "</body>" >> ../../web/words.html
