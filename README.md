# RideCell project - Anagram generation and Tail command
## Overview
This is done for RideCell - Senior Backend Engineer, Core Platform candidates. This following is the instruction given at the time when I worked on.

**Problem 1: Anagrams**

Given a string of alphabetic characters, find an anagram that consists of the most space delimited words and an anagram that consists of exactly two space delimited words (if one exists). Valid words are defined as the words in the attached wordlist, and "anagram" as the result of rearranging the letters of a word to produce a new phrase, using all the original letters exactly once. Valid anagrams can contain single character words, but should not consist entirely of single character words. If no anagrams exist with two or more words, the program should print an empty string for both cases.

Example:
For the input word "incredible", the program might produce "bile cinder" as an anagram with just two words, and "ce be dirl in" is one with the maximum of four words.

**Problem 2: Tail**

Write a clone of the tail program available in unix/linux systems but only support a very small subset of the flags/options/features it supports. Pick and choose the complexity/scope based on the time you have and the options you like to support. Support at least the basic functionality you get with no options.


The result cannot be made up of only single character words, it can contain one single character words.

Please add instructions and any libraries we have to use to get things working. Development environments are available for the engineers to test your solutions. 


## Language and Prerequisites
This application is written in Python. Please note this is written based on Python 2.7. This would not work with Python 3. (Note: some functions like xrange are used but those don't exist in Python 3.)

## Installation
You can git clone against https://github.com/recto/anagram_generator.git or download it into your local environment.

## Content
You will find the following in your workspace.
* README.md - this file.
* src/anagram.py - anagram generation application
* src/pytail.py - tail application
* src/resource/word_list.text - dictionary file for anagram generation
* test/test_anagram.py - Test cases for src/anagram.py
* test/test_tail.py - Test cases for src/pytail

## Usage
* Start terminal for Linux/Mac OS X, command prompt for Windows.
* Make sure you have Python 2.7 in your environment. (i.e. check it by python --version)
* Change the directory to **your workspace**/src.

### Anagrams
* Perform 'python anagram.py **input**' whereas **input** is text like 'are', 'nails', and 'incredible'. While 'incredible' is given in the project example, it produces quite long list of anagrams. You probably redirect the output to some file like 'python anagram.py incredible > output.log'.
* Check the output.

### Tail command
* Perform 'python pytail.py -n **number** **filename**'. It supports only -n option so you can specify number of lines to show.
* Check the output.

## Test Cases
Test cases are available at **your workspace**/test directory. You can run it as below: 
* Start terminal for Linux/Mac OS X, command prompt for Windows.
* Make sure you have Python 2.7 in your environment. (i.e. check it by python --version)
* Change the directory to **your workspace**/test.
* Perform 'python test_anagram.py'
* Perform 'python test_tail.py'
* Make sure all test cases pass.
