To add publications to the site, I used a script that will create the markdown files which I uploaded to the _publications directory. I also had to uplod the pdfs to the files directory. I have included the python script used to create the md files which I you can run on the list of references that I downloaded from google scholar. I removed unnecessary fields from the table. You can see the fields that I kept in the file contained in this git called All-citations.csv. Just run the script like this

    python create-publications-file-for-git-pages.py All-citations.csv

This will create an md file for each of the file names contained in the All-citations.csv file. Each of these can be uploaded to the _publications directory and you will need to upload a pdf of and be sure that its named exactly as a the title 

Here is the source of the framework of the website
A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
