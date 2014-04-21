pyart
=====

This repository contains some small python programs which convert images to some
artistic representation. 

## asciinator

Converts an image into ascii art. 

### Required python modules

* PIL or pillow
* numpy

### Usage

Convert the script into an executable by
```bash
chmod u+x asciinator.py
```

Basic usage:

```bash
./asciinator.py image_file scale gamma_factor
```
Here the *image_file* denotes the path to your image, *scale* is a scale factor for the image
size (0.5 = half size, 2 = double size, etc.) and *gamma_factor* is a gamma correction factor
for the image intensities. A value of 1 for *gamma_factor* will use the original intensities,
a value >1 will diminish lower intensities and favor high intensities and a value <1 will increase
lower intensities.
 
And an example:

Using this image of Franz Kafka ![Franz Kafka](/examples/kafka.png) and calling
```bash
./asciinator kafka.jpg 1 2
```
leads to
`
                                                          
                               ..     .              .    
                         .... ,;;;. ....    ............  
                        . 5G#####9#####SG:..,.,,,....... .
                  ..   .S##99#99B9B9999999##h::,,,,,.,....
                 ..   G##9999BBBBBBBBBBBB9B999#:,:,,,.....
           .   ......S9BBBBBB&B&B&&&&&&BBBB9BB9s:::::::,,.
                ... #9BBBB&&B&&B&&B&&&&&&BBBBBB9:::;;;,:,,
             ... ..#BBBBB&&BBS359#BB&&&&&&&&&BB99;:ii::,.,
           ... ...hBBB&B&B&BG55GHS9B&&&&&&&B&&&B#S:,i;;:,,
           ..... .9BBBBBH2;sri,i.:5S#SB&&B&B&B&BBB;::;::.,
         ........H9999S:.             ,2G99B&&BB9#i::,,,,,
         ........s99#3               .,:i3M9B&BBBS:;::,,,,
         ......,.,S#GX                ,:ii2#BBBB9r:::,,:;:
      .,......,..,GSi                 .,:;5M9BBB9;:;:i::,,
    . ....,....   3G..,i.            .,:2XhMSB&B;AX::i::,,
     .....,,,.,..  s..:,X2HGMX. ..299#GS9BB9SBB&GGB5;;;;.,
   ........,,..,  ,.   :iXi,hi.  MMrX GH#M5MHGS99MSA;:::,:
    . ... ......,          i.    2M,  .i5r.s5MSB9h5i:::,,:
    . ......,.,,.                2Ai       rM9SB#S:::::.;:
    . .........,:.  ,           .A3s..    ;5S#B9Ss;;;:;:::
     .........,,,,::,,           r23;....i3S#99Mr;i;;;i::;
     .......,,.,,,:::.           :5H3,.,rh#S9,ii;ii;i;;;;,
      . ....,,.,,,,.,,          AHHAr:::h9#92;r;iii;;:;::;
     .  .....,,.,,,,:,           .rrsXs3SS#Bi;i;iii;;;;;:;
     . .,...,..,..,.,,.   ,;sXrs2H##GsX29G#&&si;;;ir;ir;r;
     ............,,,,,,,       :isAX:s2G#BM@&&&X;;i;ii;;i;
    .............,,..,,,..        .ishM9Br5&&&&B95i:r;i;ii
    ... .....  ....,,,,, ....    .:2hG9G::9&&&&&&BB#3,:;;:
     .. .... .......,,:3    ,ssss3MS#X:..9&&&&&BBBBS##Sh:,
 ...  .... ..  ...,5GHHh      .;r2r     2#99&&&BB&9SGMHGMh
      ..... . iMGG#GGHhH       .        HS#99BBB#BGSMMMMhM
       . ..rHSHMSHSHSMHS   ,           AGHSS####H#H55MM33M
     . .XMHhhHGHMSSGMMHS;   .,A       22hGHGSHhMMHHH5hMHM3
      ,hHMMMHGGH#SMGMH#M   i,,MM     H3Hh53HHH5h3hHMhM3h33
     .hMhGHHSGhGHGGG3GSh   i:3h3    M3hhMhMHMM5M3Sh3233M33
     AhMMHHh35MGGMShM#G3   .  .;   H53h2hh3MhMM35#M3hhH552
    iMhMMHGhHSMHHMhMS9SM  ..,rXA  hhh33hH5523MM339Hh5h2525
   ,HMMHM3MhHMMHHhhG#9GM X .;hS3 H3M33Mhhh2Xh55SG3h335h552
   25MMMMh5hH3H3MG3M9BhS   ,A9HSSh55A5HMhMh2559S5325252322
  :5M5h5M2h5h2h3M23SBBhM   ;h##GhhM5XXG3M5H555Sh22555h332A
  2A53h532X55A3h523#&GB.    XrHMSHM2533H3h53A5XM522hhH3522
 i222535AAX2222M52hS93i      AMGSM5A2h32522s52s3AA5h3M2Ass
.rXA33h2AsXXXAX2X2M9A#   .: i3hGGGXA5325h53XrAsMr22SMh2riA
iAMGMMhAXrsssA5AsASHA2    .r525hhhA53M22h3522AhAiA3SH32rXs
A55AssX2AXrsXXXsssSAA,    .5A25hM5A5552AXh2sXh5XXAMH35Xssr
AXXrirssrrrissr;s3SXs;   .5ss2AA5XX2A2XX2srXAXsXX3hh3Asrss
`

