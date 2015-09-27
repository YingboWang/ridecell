# ridecell

1. anagrams
   
   cd anagrams
   
   nosetests

2. cloneTail
    cd cloneTail

    python cloneTail.py -n 10 words.txt words2.txt
    
    cat words.txt | python cloneTail.py -n 10


    python cloneTail.py --help

    Usage: tail - output the last part of files
    
    if no files are given, read from stdin.

    usage: cloneTail.py  [-q] [-b # | -c # | -n #] [file ...]

    Options:

      -h, --help       show this help message and exit

      -q, --quiet       never output headers giving file names

      -n N, --line=N    get tail line(s) from File

      -b B, --block=B   get tail block(s) from File

      -c C, --bytes=C  output the last K bytes; or use -c +K to output bytes

                       starting with the Kth of each file
