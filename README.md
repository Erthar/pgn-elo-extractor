# pgn-elo-extractor
A Python script to filter through a PGN dataset and extract games within a specific rating range to a new PGN file.

Primarily used for [Lichess's PGN database](https://database.lichess.org/).

## Usage

```py pgn-elo-extractor.py PATH_TO/PGN_FILE.pgn PATH_TO/NEW_PGN_FILE.pgn MIN_ELO MAX_ELO```

`MIN_ELO` and `MAX_ELO` are optional. Defaults are 600 and 800, respectively.

## Credit

Thanks to u/Nietsoj77 aka "Patzer" for the [original code](https://www.reddit.com/r/learnpython/comments/gmogd0/comment/frwguku/?utm_source=share&utm_medium=web2x&context=3)
