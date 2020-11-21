# wordG

A powerful word generator for hackers. Generates passwords with personal information.

## Instalation

```shell
# cloning repo
git clone https://github.com/Samet732/wordG

cd wordG

# installing required modules
python3 -m pip install -r requirements.txt
```

## Usage

input.txt: includes person's personal information

output.txt: output of wordlist

wordlist.txt: if any password in your head, write to this (optional)

> **Warning!** Write informations/passwords as downcase. wordG converts to uppercase automatically.

## Executing

### Without Optional Wordlist

```shell
python3 wordG/src/app.py "input.txt" "output.txt" ""
```

### With Optional Wordlist

```shell
python3 wordG/src/app.py "input.txt" "output.txt" "wordlist.txt"
```

*wordG uses words inside wordlist.txt like as a personal information for generating passwords.*
