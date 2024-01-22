To add publications to the site, I used a script that will create the markdown files which I uploaded to the _publications directory. I also had to uplod the pdfs to the files directory. I have included the python script used to create the md files which I you can run on the list of references that I downloaded from google scholar. I removed unnecessary fields from the table. You can see the fields that I kept in the file contained in this git called All-citations.csv. Just run the script like this

    python create-publications-file-for-git-pages.py All-citations.csv

This will create an md file for each of the file names contained in the All-citations.csv file. Each of these can be uploaded to the _publications directory and you will need to upload a pdf of and be sure that its name matches what you specified in the markdown file. There is an example below

    ---
    title: "Paper Title Number 1"
    collection: publications
    permalink: /publication/2009-10-01-paper-title-number-1
    excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
    date: 2009-10-01
    venue: 'Journal 1'
    paperurl: 'http://academicpages.github.io/files/paper1.pdf'
    citation: 'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
    ---
    This paper is about the number 1. The number 2 is left for future work.

    [Download paper here](http://academicpages.github.io/files/paper1.pdf)

    Recommended citation: Your Name, You. (2009). "Paper Title Number 1." <i>Journal 1</i>. 1(1).

So the pdf that you upload to the files directory should be called paper1.pdf


Here is the source of the framework of the website
A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
