#/bin/sh

mv filereader.py ..
mv filechanger.py ..
rm aquote.json
scrapy crawl aqual -o aquote.json
twint -s jetblue --since "2014-10-26 20:30:15" -pt -o test-cases.csv --csv
echo $(date --rfc-3339=seconds | cut -d- -f1-3) > lastupdate
mv ../filereader.py .
python3 filereader.py
mv filereader.py ..

