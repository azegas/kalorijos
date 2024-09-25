# kalorijos

- TODO what is data types in python
- TODO what are data structures in python
- TODO what is numpy
- TODO try to use uncensorised model (from llama page)
- TODO try to load custom model [like such](https://www.youtube.com/watch?v=3BnnsQCmgLo&list=PL8motc6AQftnHhi2X8M3rqEFwERPVup4c&index=6&ab_channel=SamWitteveen)
- TODO how to run this thing in the cloud/faster?
- TODO instead of scraping infro from the site, try to give the html for the ai and let it [pick out headlines for example](https://www.youtube.com/watch?v=k_1pOF1mj8k&list=PL8motc6AQftnHhi2X8M3rqEFwERPVup4c&index=4&ab_channel=SamWitteveen)

## Inspirations 

- [Image recognition](https://www.youtube.com/watch?v=4Jpltb9crPM&t=504s&ab_channel=NeuralNine)
- [Building local "agents"](https://www.youtube.com/watch?v=93-9NHHgn84&t=568s&ab_channel=DavidOndrej)
- [describe images from downloads folder](https://www.youtube.com/watch?v=_TUvb6NtpGA&t=144s&ab_channel=SamWitteveen)
- c[reate a new custom model according to your cursom system configuration file](https://youtu.be/Ox8hhpgrUi0?si=V0mIUm6SvHP2v_8O&t=439)


## Run lokaliai
```
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llava:7b
ollama run llava:7b
/show
/set
/set system "you are a drunk assistant that slurs a lot and speaks rudely"
/save drunk
/load drunk
/bye
ollama list
pip install ollama
curl -o cepelinai.jpg https://ecoangus.lt/wp-content/uploads/2021/01/cepelinai-80268533.jpg
```

It takes about 3-4 minutes to process one images and the results are not so great:

```
(venv-kalorijos) aze@DESKTOP-AUDMJ7D:~/GIT/kalorijos$ python main.py 
 The image shows a dish consisting of two golden-brown potato wedges, likely baked or fried, topped with what appears to be crumbled cheese and finely chopped herbs. The dish is garnished with a dollop of cream or sauce on the side. The wedges are placed on a ceramic plate with visible grain lines, which suggests it could be a handcrafted or artisanal piece. In the background, there's a blurred wooden surface that might be a table, and the focus is clearly on the food in the foreground. There are no texts visible in the image. 
(venv-kalorijos) aze@DESKTOP-AUDMJ7D:~/GIT/kalorijos$ python main.py 
 This is a plate of mixed vegetables including what appears to be shrimp, cucumber, lettuce, tomato, and carrot. It's garnished with herbs and possibly feta cheese or crumbled nuts. The colors suggest it might also have some bell pepper. The dish looks fresh and vibrant, suggesting a healthy and balanced meal. A rough estimate of the calories in this meal would be around 350-450 calories, depending on portion size and any additional dressing or sauce that may not be visible. This assumes an average serving size for shrimp and mixed vegetables. 
(venv-kalorijos) aze@DESKTOP-AUDMJ7D:~/GIT/kalorijos$ python main.py 
 The food appears to be a breakfast cereal, such as oatmeal, with visible flakes and perhaps some nuts or seeds on top. The dish is in a bowl and there are additional flakes spread around it. 
(venv-kalorijos) aze@DESKTOP-AUDMJ7D:~/GIT/kalorijos$ python main.py 
 The image shows a bowl of oatmeal, which appears to be a simple, unflavored preparation. Oatmeal is a common breakfast item made from whole grain oats and water or milk. It's often served with additional ingredients like sugar, cinnamon, butter, or fruit, which would add more calories. The calorie count of the food in the picture would depend on several factors such as the size of the bowl, whether it's made with water or milk, if any sweeteners or fats have been added, and if there are additional ingredients like fruits, nuts, or seeds mixed in.

Without knowing the exact preparation and serving size, it's not possible to provide an accurate calorie count for this bowl of oatmeal. If we consider a basic unsweetened serving of oatmeal made with water or milk, the calories can range from around 150 to 300 per serving, depending on the ingredients and portion size. However, without more information or context, I'm unable to provide a specific calorie count for this image. 
```


