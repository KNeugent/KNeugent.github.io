---
layout: page
title: Computer Science
---

While astronomy research has been my main focus since 2015, I have both BA and MS degrees in computer science and spent a few years working in the field of cyber security before going back to school for astronomy. Here I briefly summarize a few of my more recent astronomy-focused programming projects as well as an overview of my experience working in cyber security.

# Astronomy programming projects

Skills: `Python` `pandas` `NumPy` `scikit-learn` `matplotlib` `jupyter notebooks`

## k-Nearest Neighbor Classifier for Binary Stars

As part of my PhD thesis at the University of Washington, I observationally constrained the binary fraction of red supergiants in the Local Group galaxies of M31, M33, and the Magellanic Clouds. While I discuss the science motivation more [here](https://kathrynneugent.com/astronomy/), one of my favorite parts of this research was building a k-NN classifier to differentiate the single and binary red supergiants from their colors. The code and a more detailed explanation can be [found on github](https://github.com/KNeugent/kNN-BinaryStars).

## Monte Carlo Simulation for Binaries

When observing a binary star system in another galaxy, it can be difficult to determine if the two stars are gravitationally bound or simply just line-of-sight systems. I wrote a Monte Carlo simulation that takes into account the local stellar population density in order to determine the percentage chance that two astronomical objects are line-of-sight binaries as opposed to gravitationally bound. The code and further information can be [found on github](https://github.com/KNeugent/LineOfSightBinaries).

## Combining Stellar Spectra

To better anticipate how a the spectra of a binary star system might appear, I wrote a program that combines the spectra of different types of stars (in my case, red supergiants and OB stars) to produce a single output spectrum. While the programming component of this project wasn't particularly challenging, it was a fun way to combine some observational astronomy, stellar astrophysics, and python programming. More information and the code can be [found on github](https://github.com/KNeugent/BinaryStarSpectraCombine).

# Cyber Security

## DES Animation

As my final project for a network security course in graduate school, I created an animation that shows the various encryption steps for the (now no longer used) Data Encryption Standard (DES). Since I moved the animation from my personal website to YouTube back in 2021, it has received over 10K views and is regularly used to teach undergraduate and graduate students about the basics of DES. A detailed walkthrough of the steps can be found [here in a pdf](/assets/pdf/DESwalkthrough.pdf).

<iframe width="560" height="315" src="https://www.youtube.com/embed/Vcld7CMAnNs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Web Security Penetration Testing

I worked as web application penetration tester at both MITRE as well as the National Renewable Energy Lab (NREL). As a pen tester, I spent the majority of my time assessing the vulnerabilities of data-intensive web applications and databases. I used custom-built scrips and SQL queries as well as network packet sniffers (like `tcpdump` and [Wireshark](https://www.wireshark.org)), as well as vulnerability scanners (primarily [BurpSuite](https://portswigger.net/burp)) and proxies. I also worked with clients to develop and execute security, vulnerability, and performance tests for open source software and web applications. As part of this work, I earned my Certified Information Systems Security Professional [(CISSP)](https://www.isc2.org/Certifications/CISSP) certificate and frequently attended local Open Web Application Security Project [(OWASP)](https://owasp.org) meetings.