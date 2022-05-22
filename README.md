# LoLTrainer

Description
-----------
Free open source [League of Legends](https://www.leagueoflegends.com/) trainer made by exploiting images recognition.
This software is strongly dependent on 
[League of Legends Fandom Wiki](https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki) for what concerns
**images** and **stats**.

LoLTrainer Purpose
------------------
The main reason behind this project is that I didn't want to use League of Legends official
[API](https://developer.riotgames.com/) (for obvious reasons). In addition, I'm having a lot of
fun!

Installation
------------
To do, I guess I'll simply create an .exe.


How to Use
----------
To do.

Recognition Process
-------------------
The procedure is very simple and straightforward. With the installer, we download all the *items images* from [League of Legends Fandom Wiki](https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki). 

Those images are then used to as **testers** for the ones acquired by screen capture. The comparison between the images is performed once they have been thresholded into binary images; the reason is that by doing this we can actually count the number of pixels with value "1" after the one-to-one image difference, thus a fairly good **similarity score**.

It's important to notice that the **threshold** procedure is done without finding the best *threshold value*, so this could be improved for example by implementing **Otsus Method**.

Below we can see practically what is happening.

| Doran's Blade, Default      | Doran's Blade, Default Threshold | Doran's Blade, Screenshot     | Doran's Blade, Screnshot Threshold |
| :---:        |    :----:   |          :---: | :---: |
| <img src="https://user-images.githubusercontent.com/79590448/169715691-6a5993fb-724d-46a2-b44a-f32563a5b4cf.png" width="420">      | <img src="https://user-images.githubusercontent.com/79590448/169715725-5a126fce-96cf-4f1f-8d10-4a82ff6ce924.png" width="420">       | <img src="https://user-images.githubusercontent.com/79590448/169715751-062bdd4c-829f-48d8-834b-02f314dba956.png" width="420">   | <img src="https://user-images.githubusercontent.com/79590448/169715755-80acc1c1-76ce-4776-86d5-edb4031a4d52.png" width="420"> |

The *similarity score* has a threshold value, which basically determines when the image analyzed is recognized and so associated to its the default ones.
Once we determined what item is beeing hold, an item ```LoLItems()``` is created and stored inside the champion object ```LoLChampions()```.

In principle we could ask directly when all the pixels match, but the problem arises with the screenshot acquisition, which produces an image a bit different from the *default* one, as we can see. However, this difference is so small that can easily be compensated with the *score parameter*.


Citing
------
If you enjoyed using **LoLTrainer**, please consider sharing it! (I Guess it will take a while before you'll enjoy using it :D)
```
@software{LoLTrainer,
  author       = {Stefano Bianchi},
  title        = {LoLTrainer, A very intelligent League of Legend coach},
  year         = 2022,
  url          = {https://github.com/Stefano314/LoLTrainer}
}
```
