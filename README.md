# LoLTrainer

Description
-----------
Free open source [League of Legends](https://www.leagueoflegends.com/) trainer made by 
exploiting images recognition.
This software is strongly dependent on 
[League of Legends Fandom Wiki](https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki) for what concerns
**images** and **stats**.

LoLTrainer Purpose
------------------
The main reason behind this project is that I didn't want to use League of Legends official
[API](https://developer.riotgames.com/) (for obvious reasons). In addition, I'm having a 
lot of fun!

Installation
------------
To do, I guess I'll simply create an .exe.


How to Use
----------
To do.

# Recognition Process

## Items

The procedure is very simple and straightforward. With the installer, we download all the 
*items images* from [League of Legends Fandom Wiki](https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki). 
Thankfully, League of Legends has a solid structure overall, no exception for the items
images that are exactly ```40x40```.

Those images are then used as **testers** for the ones acquired by screen capture. 
The comparison between the images is performed once they have been thresholded into binary 
images; the reason is that by doing this we can actually count the number of pixels with 
value "1" after the one-to-one image difference, thus a fairly good **similarity score**.

In addition, a binary comparison is much faster than a more complex method that takes into
account all the gray levels (or worse, all the values of an RGB image).

Of course, all the images are treated as [numpy.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
objects.

The threshold value is found by applying **Otsu's Method**, which is optimal for
global thresholding.

Below we can see practically what is happening.

| Doran's Blade, Default      | Doran's Blade, Default Threshold | Doran's Blade, Screenshot     | Doran's Blade, Screnshot Threshold |
| :---:        |    :----:   |          :---: | :---: |
| <img src="https://user-images.githubusercontent.com/79590448/169715691-6a5993fb-724d-46a2-b44a-f32563a5b4cf.png" width="420">      | <img src="https://user-images.githubusercontent.com/79590448/169715725-5a126fce-96cf-4f1f-8d10-4a82ff6ce924.png" width="420">       | <img src="https://user-images.githubusercontent.com/79590448/169715751-062bdd4c-829f-48d8-834b-02f314dba956.png" width="420">   | <img src="https://user-images.githubusercontent.com/79590448/169715755-80acc1c1-76ce-4776-86d5-edb4031a4d52.png" width="420"> |

The items recognition starts by considering all 6 item boxes separately, comparing each
single one with all the images stored in */Images/Items* folder. A **score vector** is
created for every box and we select as recognized item the one associated to the
**minimum score value**.
Clearly, if this value is too high (*meaning higher than a certain value, like 0.3*), it
simply says that no item is found. This covers the case in which we do have an *empty
box*, so no item carried.

Once we determined what item is being hold, an item ```LoLItems()``` is created and 
stored inside the champion object ```LoLChampions()```.

In principle, we could ask directly when all the pixels match, but the problem arises with 
the screenshot acquisition, which produces an image a bit different from the *default* one, 
as we can see. However, this difference is so small that can easily be compensated with 
the *score parameter*.

## Scoreboard
Similarly to what we has been done with the items, the Trainer recognizes if the **scoreboard** is open if it manages to find a known pattern, namely a *"sword icon"*. <img style="float: right; padding-left: 10px; padding-top: 10px;" src="https://user-images.githubusercontent.com/79590448/172323572-4de4844d-ac97-431c-b20f-5396287e3302.png" width="170">

The reason why that icon has been chosen is simply because empirically I noticed that from the total screen capture, once *thresholded*, that was the most robust reoccurring structure in the scoreboard. In the image we see the chosen pattern, which has a 20x20 format. Once we are able to recognize exactly where that pattern is located, we can **infer** the position of the total scoreboard thanks its relative position with the *sword icon*.

The recognition process in this case requires a bit more time consuming, since it has to count the *number of different pixels* in every (20x20) portion of the toatal image - starting from the top left corner - compared to the *sword icon*. However, it stops immediately once it is able to find a pattern that is **similar enough** (the threshold can be changed); the good thing is that the sword icon pattern is so robust to the point where we can set the threshold to a value which basically always finds the correct match. The result is shown below.

<img style="float: center; padding-top: 10px; padding-bottom: 20px;" src="https://user-images.githubusercontent.com/79590448/172334207-38a7f3e6-04ff-42ce-a176-a0dabbbe8183.png" width="700"> 


# Citing

If you enjoyed using **LoLTrainer**, please consider sharing it! (I Guess it will take a 
while before you'll enjoy using it :D)
```
@software{LoLTrainer,
  author       = {Stefano Bianchi},
  title        = {LoLTrainer, A very intelligent League of Legend coach},
  year         = 2022,
  url          = {https://github.com/Stefano314/LoLTrainer}
}
```
