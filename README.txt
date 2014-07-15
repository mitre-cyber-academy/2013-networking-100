Name: Captured Data

Description: You finally got through the firewalls, past the vaulted SSL and into the heart of a protected network.
You believe you have captured some sneakret packets from an inside source. Can you figure out what the data is?

How to Solve: First, reconstruct the web page (and images) from the packet cap. This should give a host of 
images (with random names). Once the page is built, there should be a series of hexagon graphs with an array of
characters beneath. The flag is hidden within the array based on the hexagonal numerical sequence (a generating
function for these (hexNum) has been given in src/genImages.py). If the first 12 (starting at 1) numbers of
the sequence are generated and their position in the array, counting from one is found, the flag is revealed.

What to distribute:
dist/site.pcap

Flag: MCA-53C12E73
