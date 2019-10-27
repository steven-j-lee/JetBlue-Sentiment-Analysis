#/bin/sh

mv filereader.py ..
rm aquote.json
scrapy crawl aqual -o aquote.json
twint -s jetblue --since "2014-10-26 20:30:15" -pt -o test-cases.csv --csv
mv ../filereader.py .
python3 filereader.py

