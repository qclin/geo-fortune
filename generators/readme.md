to download new language model on the ec2 instance

```
python -m virtualenv .env           # will create directory .env
source .env/bin/activate      # activate virtualenv
pip install spacy             # install stuff
python -m spacy download en   # this should now work as expected
deactivate

```
