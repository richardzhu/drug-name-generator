# Generating Drug Names with a RNN

## Summary

TL;DR -- I made [a bot that tweets drug names](https://twitter.com/DrugNameBot)!

Coming up with names for things is an art. For products that might bring in tens or hundreds of
millions of dollars in revenue in a single year, it's also a high-stakes game. Some drugs 
have the potential to bring in billions of dollars in a single year, so it makes sense to 
spend a lot of time thinking about the name -- the main way any customers are going to think
about your drug.

Even though we mostly know OTC drugs with cool, alien-sounding names like 
_Tylenol_, _Viagra_, and _Oxycontin_,
a prescription drug actually has *three* names!
There's the chemical name (derived from the compound structure), the generic name
(non-proprietary, assigned so everyone worldwide calls it the same name), and the brand/trade name
(proprietary to one pharma company marketing the drug in one specific region).

As an example, consider _Viagra_.
* IUPAC chemical name: `5-{2-Ethoxy-5-[(4-methylpiperazin-1-yl)sulfonyl]phenyl}-1-methyl-3-propyl-1,6-dihydro-7H-pyrazolo[4,3-d]pyrimidin-7-one`
* Generic name: `sildenafil`
* Brand/trade name: `Viagra`

Generic and brand names seem to have significant structure to them because generic names all have common suffixes,
used to denote the mechanism/type of compound, and brand names are supposed to sound "euphonious" and "evocative" for marketing
purposes. I decided to take a quick foray into NLP by generating drug names via a RNN. Conveniently, the FDA
has released a database of most drugs approved since 1939, which you can download
[here](https://www.fda.gov/Drugs/InformationOnDrugs/ucm079750.htm).

Here were the notebooks I used, and the steps they perform:
* `clean-drug-name-data.ipynb`: Loading + filtering data, cleaning out simple words and idiosyncratic occurrences of punctuation and other characters
* `proto-textgenrnn`: Training a `textgenrnn` on the data, generating lots of drug names, and saving them to a file.

There's also extra code here to run a Twitter bot that tweets out new drug names.

## Deploy steps

Spin up a GCE instance and run `./sync-to-dev.sh`.

Then in the instance, run `./install_requirements.sh`.
