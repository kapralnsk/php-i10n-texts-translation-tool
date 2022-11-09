# php-i10n-texts-translation-tool
Python-based tool to simplify translation of PHP array-based l10n texts. Python because f-you PHP, I'm done with that part of my developer life :upside_down_face:

# Usecase
Given a PHP Associative Array containing l10n texts, we need to translate that texts into a different language, and then pack those texts back into an original data structure.

# Solution
A web-app that using the PHP array source unpacks that into a list of strings, which can be manually fed into translating tool (i.e. Google Translate). Given the original PHP source and translated texts list we then pack translated texts into orginal data structre, and output it as a PHP array.
Manual feeding has to be done because Google Translate API requires signing up and paying from the get-go, and free solutions were broken at the time of developing this.

# Requirements
* PHP runtime (`php-whisperer` depend on it)
* Python 3+

# Other notes
* PHP array to work on has to be stored in a `$data` var in the source.
* If you ever stumble upon this, please keep in mind that this is a quick-n-dirty solution for a very specific problem of a friend of mine. Emphasis on _quick-n-dirty_ :)
