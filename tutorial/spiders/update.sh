#/bin/sh
twint -s jetblue --since "$(cat lastupdate)" -pt -o test-cases.csv --csv
echo $(date --rfc-3339=seconds | cut -d- -f1-3) > lastupdate
mv ../fileupdate.py .
python3 filechanger.py

