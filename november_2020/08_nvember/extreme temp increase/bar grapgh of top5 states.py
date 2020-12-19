Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
Traceback (most recent call last):
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 96, in <module>
    start()
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 71, in start
    index= item_list.index(key)
ValueError: 'book' is not in list
>>> 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
Traceback (most recent call last):
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 96, in <module>
    start()
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 71, in start
    index= [(i, colour.index(item))for i, colour in enumerate(item_list) if item in item_list]
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 71, in <listcomp>
    index= [(i, colour.index(item))for i, colour in enumerate(item_list) if item in item_list]
ValueError: ['B001', 'book', 'Patriot Games', 15.95] is not in list
>>> 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
   item_id category    description  price
0     B001     book  Patriot Games  15.95
1     B002     book         Origin  19.95
3     B003     book    Animal Farm   9.97
4     B004     book          Grant  22.50
9     B005     book  Prairie Fires  18.95
16    B005     book        Ragtime  17.25
26    B006     book   Future Shock   8.95
   item_id category    description  price
0     B001     book  Patriot Games  15.95
1     B002     book         Origin  19.95
3     B003     book    Animal Farm   9.97
4     B004     book          Grant  22.50
9     B005     book  Prairie Fires  18.95
16    B005     book        Ragtime  17.25
26    B006     book   Future Shock   8.95
   item_id category                description   price
2     C001    cloth                Armani Suit  800.00
8     C002    cloth                      Pants   39.95
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
15    C005    cloth             Wrangler Jeans   24.50
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
24    C010    cloth  New Balance Trail Runners   69.95
   item_id category    description  price
0     B001     book  Patriot Games  15.95
1     B002     book         Origin  19.95
3     B003     book    Animal Farm   9.97
4     B004     book          Grant  22.50
9     B005     book  Prairie Fires  18.95
16    B005     book        Ragtime  17.25
26    B006     book   Future Shock   8.95
   item_id category    description  price
0     B001     book  Patriot Games  15.95
1     B002     book         Origin  19.95
3     B003     book    Animal Farm   9.97
4     B004     book          Grant  22.50
9     B005     book  Prairie Fires  18.95
16    B005     book        Ragtime  17.25
26    B006     book   Future Shock   8.95
   item_id category              description   price
5     E001    elect              EyePhone 10  795.00
6     E002    elect  First Alert Smoke Alarm   29.95
10    E003    elect       Sony Prtable Radio   15.00
14    E004    elect                HP Laptop  350.00
22    E005    elect           LinkSys Router   49.95
25    E006    elect   Altec Lansing Speakers  195.95
27    E007    elect               LG 55 UDTV  350.00
28    E008    elect       Dell All-in-One PC  495.00
29    E009    elect    Brother Laser Printer   99.00
   item_id category              description   price
5     E001    elect              EyePhone 10  795.00
6     E002    elect  First Alert Smoke Alarm   29.95
10    E003    elect       Sony Prtable Radio   15.00
14    E004    elect                HP Laptop  350.00
22    E005    elect           LinkSys Router   49.95
25    E006    elect   Altec Lansing Speakers  195.95
27    E007    elect               LG 55 UDTV  350.00
28    E008    elect       Dell All-in-One PC  495.00
29    E009    elect    Brother Laser Printer   99.00
   item_id category             description  price
7     F001     food  Moose Drool Ale 6-pack   9.95
13    F002     food            Jumbo shrimp  12.50
17    F003     food         Fusili - 16 oz.   2.95
23    F004     food              Lamb Chops  21.95
   item_id category                description   price
2     C001    cloth                Armani Suit  800.00
8     C002    cloth                      Pants   39.95
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
15    C005    cloth             Wrangler Jeans   24.50
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
24    C010    cloth  New Balance Trail Runners   69.95
   item_id category    description  price
0     B001     book  Patriot Games  15.95
1     B002     book         Origin  19.95
3     B003     book    Animal Farm   9.97
4     B004     book          Grant  22.50
9     B005     book  Prairie Fires  18.95
16    B005     book        Ragtime  17.25
26    B006     book   Future Shock   8.95
   item_id category              description   price
5     E001    elect              EyePhone 10  795.00
6     E002    elect  First Alert Smoke Alarm   29.95
10    E003    elect       Sony Prtable Radio   15.00
14    E004    elect                HP Laptop  350.00
22    E005    elect           LinkSys Router   49.95
25    E006    elect   Altec Lansing Speakers  195.95
27    E007    elect               LG 55 UDTV  350.00
28    E008    elect       Dell All-in-One PC  495.00
29    E009    elect    Brother Laser Printer   99.00
   item_id category                description   price
2     C001    cloth                Armani Suit  800.00
8     C002    cloth                      Pants   39.95
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
15    C005    cloth             Wrangler Jeans   24.50
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
24    C010    cloth  New Balance Trail Runners   69.95
   item_id category                description   price
2     C001    cloth                Armani Suit  800.00
8     C002    cloth                      Pants   39.95
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
15    C005    cloth             Wrangler Jeans   24.50
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
24    C010    cloth  New Balance Trail Runners   69.95
   item_id category             description  price
7     F001     food  Moose Drool Ale 6-pack   9.95
13    F002     food            Jumbo shrimp  12.50
17    F003     food         Fusili - 16 oz.   2.95
23    F004     food              Lamb Chops  21.95
   item_id category              description   price
5     E001    elect              EyePhone 10  795.00
6     E002    elect  First Alert Smoke Alarm   29.95
10    E003    elect       Sony Prtable Radio   15.00
14    E004    elect                HP Laptop  350.00
22    E005    elect           LinkSys Router   49.95
25    E006    elect   Altec Lansing Speakers  195.95
27    E007    elect               LG 55 UDTV  350.00
28    E008    elect       Dell All-in-One PC  495.00
29    E009    elect    Brother Laser Printer   99.00
   item_id category                description   price
2     C001    cloth                Armani Suit  800.00
8     C002    cloth                      Pants   39.95
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
15    C005    cloth             Wrangler Jeans   24.50
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
24    C010    cloth  New Balance Trail Runners   69.95
   item_id category    description  price
0     B001     book  Patriot Games  15.95
1     B002     book         Origin  19.95
3     B003     book    Animal Farm   9.97
4     B004     book          Grant  22.50
9     B005     book  Prairie Fires  18.95
16    B005     book        Ragtime  17.25
26    B006     book   Future Shock   8.95
   item_id category             description  price
7     F001     food  Moose Drool Ale 6-pack   9.95
13    F002     food            Jumbo shrimp  12.50
17    F003     food         Fusili - 16 oz.   2.95
23    F004     food              Lamb Chops  21.95
   item_id category                description   price
2     C001    cloth                Armani Suit  800.00
8     C002    cloth                      Pants   39.95
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
15    C005    cloth             Wrangler Jeans   24.50
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
24    C010    cloth  New Balance Trail Runners   69.95
   item_id category                description   price
2     C001    cloth                Armani Suit  800.00
8     C002    cloth                      Pants   39.95
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
15    C005    cloth             Wrangler Jeans   24.50
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
24    C010    cloth  New Balance Trail Runners   69.95
   item_id category                description   price
2     C001    cloth                Armani Suit  800.00
8     C002    cloth                      Pants   39.95
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
15    C005    cloth             Wrangler Jeans   24.50
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
24    C010    cloth  New Balance Trail Runners   69.95
   item_id category                description   price
2     C001    cloth                Armani Suit  800.00
8     C002    cloth                      Pants   39.95
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
15    C005    cloth             Wrangler Jeans   24.50
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
24    C010    cloth  New Balance Trail Runners   69.95
   item_id category              description   price
5     E001    elect              EyePhone 10  795.00
6     E002    elect  First Alert Smoke Alarm   29.95
10    E003    elect       Sony Prtable Radio   15.00
14    E004    elect                HP Laptop  350.00
22    E005    elect           LinkSys Router   49.95
25    E006    elect   Altec Lansing Speakers  195.95
27    E007    elect               LG 55 UDTV  350.00
28    E008    elect       Dell All-in-One PC  495.00
29    E009    elect    Brother Laser Printer   99.00
   item_id category             description  price
7     F001     food  Moose Drool Ale 6-pack   9.95
13    F002     food            Jumbo shrimp  12.50
17    F003     food         Fusili - 16 oz.   2.95
23    F004     food              Lamb Chops  21.95
   item_id category                description   price
2     C001    cloth                Armani Suit  800.00
8     C002    cloth                      Pants   39.95
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
15    C005    cloth             Wrangler Jeans   24.50
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
24    C010    cloth  New Balance Trail Runners   69.95
   item_id category              description   price
5     E001    elect              EyePhone 10  795.00
6     E002    elect  First Alert Smoke Alarm   29.95
10    E003    elect       Sony Prtable Radio   15.00
14    E004    elect                HP Laptop  350.00
22    E005    elect           LinkSys Router   49.95
25    E006    elect   Altec Lansing Speakers  195.95
27    E007    elect               LG 55 UDTV  350.00
28    E008    elect       Dell All-in-One PC  495.00
29    E009    elect    Brother Laser Printer   99.00
   item_id category    description  price
0     B001     book  Patriot Games  15.95
1     B002     book         Origin  19.95
3     B003     book    Animal Farm   9.97
4     B004     book          Grant  22.50
9     B005     book  Prairie Fires  18.95
16    B005     book        Ragtime  17.25
26    B006     book   Future Shock   8.95
   item_id category              description   price
5     E001    elect              EyePhone 10  795.00
6     E002    elect  First Alert Smoke Alarm   29.95
10    E003    elect       Sony Prtable Radio   15.00
14    E004    elect                HP Laptop  350.00
22    E005    elect           LinkSys Router   49.95
25    E006    elect   Altec Lansing Speakers  195.95
27    E007    elect               LG 55 UDTV  350.00
28    E008    elect       Dell All-in-One PC  495.00
29    E009    elect    Brother Laser Printer   99.00
   item_id category              description   price
5     E001    elect              EyePhone 10  795.00
6     E002    elect  First Alert Smoke Alarm   29.95
10    E003    elect       Sony Prtable Radio   15.00
14    E004    elect                HP Laptop  350.00
22    E005    elect           LinkSys Router   49.95
25    E006    elect   Altec Lansing Speakers  195.95
27    E007    elect               LG 55 UDTV  350.00
28    E008    elect       Dell All-in-One PC  495.00
29    E009    elect    Brother Laser Printer   99.00
   item_id category              description   price
5     E001    elect              EyePhone 10  795.00
6     E002    elect  First Alert Smoke Alarm   29.95
10    E003    elect       Sony Prtable Radio   15.00
14    E004    elect                HP Laptop  350.00
22    E005    elect           LinkSys Router   49.95
25    E006    elect   Altec Lansing Speakers  195.95
27    E007    elect               LG 55 UDTV  350.00
28    E008    elect       Dell All-in-One PC  495.00
29    E009    elect    Brother Laser Printer   99.00
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
   item_id category              description   price
5     E001    elect              EyePhone 10  795.00
6     E002    elect  First Alert Smoke Alarm   29.95
10    E003    elect       Sony Prtable Radio   15.00
14    E004    elect                HP Laptop  350.00
22    E005    elect           LinkSys Router   49.95
25    E006    elect   Altec Lansing Speakers  195.95
27    E007    elect               LG 55 UDTV  350.00
28    E008    elect       Dell All-in-One PC  495.00
29    E009    elect    Brother Laser Printer   99.00
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x032D17D0>
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
                                description   price
category item_id                                   
book     B001                 Patriot Games   15.95
         B002                        Origin   19.95
         B003                   Animal Farm    9.97
         B004                         Grant   22.50
         B005                 Prairie Fires   18.95
         B006                  Future Shock    8.95
cloth    C001                   Armani Suit  800.00
         C002                         Pants   39.95
         C003           Vasque Hiking Boots  109.00
         C004                      Wool Hat   14.00
         C005                Wrangler Jeans   24.50
         C006                  Nike T-shirt   19.00
         C007               Gore-Tex Gloves   39.00
         C008      North Face Fleece Jacket   89.95
         C009     Nationals Logo Sweatshirt   49.00
         C010     New Balance Trail Runners   69.95
elect    E001                   EyePhone 10  795.00
         E002       First Alert Smoke Alarm   29.95
         E003            Sony Prtable Radio   15.00
         E004                     HP Laptop  350.00
         E005                LinkSys Router   49.95
         E006        Altec Lansing Speakers  195.95
         E007                    LG 55 UDTV  350.00
         E008            Dell All-in-One PC  495.00
         E009         Brother Laser Printer   99.00
food     F001        Moose Drool Ale 6-pack    9.95
         F002                  Jumbo shrimp   12.50
         F003               Fusili - 16 oz.    2.95
         F004                    Lamb Chops   21.95
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
         item_id             description   price
category                                        
book        B001           Patriot Games   15.95
cloth       C001             Armani Suit  800.00
elect       E001             EyePhone 10  795.00
food        F001  Moose Drool Ale 6-pack    9.95
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
                                description   price
category item_id                                   
book     B001                 Patriot Games   15.95
         B002                        Origin   19.95
         B003                   Animal Farm    9.97
         B004                         Grant   22.50
         B005                 Prairie Fires   18.95
         B006                  Future Shock    8.95
cloth    C001                   Armani Suit  800.00
         C002                         Pants   39.95
         C003           Vasque Hiking Boots  109.00
         C004                      Wool Hat   14.00
         C005                Wrangler Jeans   24.50
         C006                  Nike T-shirt   19.00
         C007               Gore-Tex Gloves   39.00
         C008      North Face Fleece Jacket   89.95
         C009     Nationals Logo Sweatshirt   49.00
         C010     New Balance Trail Runners   69.95
elect    E001                   EyePhone 10  795.00
         E002       First Alert Smoke Alarm   29.95
         E003            Sony Prtable Radio   15.00
         E004                     HP Laptop  350.00
         E005                LinkSys Router   49.95
         E006        Altec Lansing Speakers  195.95
         E007                    LG 55 UDTV  350.00
         E008            Dell All-in-One PC  495.00
         E009         Brother Laser Printer   99.00
food     F001        Moose Drool Ale 6-pack    9.95
         F002                  Jumbo shrimp   12.50
         F003               Fusili - 16 oz.    2.95
         F004                    Lamb Chops   21.95
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
{'description': {('book', 'B001'): 'Patriot Games', ('book', 'B002'): 'Origin', ('book', 'B003'): 'Animal Farm', ('book', 'B004'): 'Grant', ('book', 'B005'): 'Prairie Fires', ('book', 'B006'): 'Future Shock', ('cloth', 'C001'): 'Armani Suit', ('cloth', 'C002'): 'Pants', ('cloth', 'C003'): 'Vasque Hiking Boots', ('cloth', 'C004'): 'Wool Hat', ('cloth', 'C005'): 'Wrangler Jeans', ('cloth', 'C006'): 'Nike T-shirt', ('cloth', 'C007'): 'Gore-Tex Gloves', ('cloth', 'C008'): 'North Face Fleece Jacket', ('cloth', 'C009'): 'Nationals Logo Sweatshirt', ('cloth', 'C010'): 'New Balance Trail Runners', ('elect', 'E001'): 'EyePhone 10', ('elect', 'E002'): 'First Alert Smoke Alarm', ('elect', 'E003'): 'Sony Prtable Radio', ('elect', 'E004'): 'HP Laptop', ('elect', 'E005'): 'LinkSys Router', ('elect', 'E006'): 'Altec Lansing Speakers', ('elect', 'E007'): 'LG 55 UDTV', ('elect', 'E008'): 'Dell All-in-One PC', ('elect', 'E009'): 'Brother Laser Printer', ('food', 'F001'): 'Moose Drool Ale 6-pack', ('food', 'F002'): 'Jumbo shrimp', ('food', 'F003'): 'Fusili - 16 oz.', ('food', 'F004'): 'Lamb Chops'}, 'price': {('book', 'B001'): 15.95, ('book', 'B002'): 19.95, ('book', 'B003'): 9.97, ('book', 'B004'): 22.5, ('book', 'B005'): 18.95, ('book', 'B006'): 8.95, ('cloth', 'C001'): 800.0, ('cloth', 'C002'): 39.95, ('cloth', 'C003'): 109.0, ('cloth', 'C004'): 14.0, ('cloth', 'C005'): 24.5, ('cloth', 'C006'): 19.0, ('cloth', 'C007'): 39.0, ('cloth', 'C008'): 89.95, ('cloth', 'C009'): 49.0, ('cloth', 'C010'): 69.95, ('elect', 'E001'): 795.0, ('elect', 'E002'): 29.95, ('elect', 'E003'): 15.0, ('elect', 'E004'): 350.0, ('elect', 'E005'): 49.95, ('elect', 'E006'): 195.95, ('elect', 'E007'): 350.0, ('elect', 'E008'): 495.0, ('elect', 'E009'): 99.0, ('food', 'F001'): 9.95, ('food', 'F002'): 12.5, ('food', 'F003'): 2.95, ('food', 'F004'): 21.95}}
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
Traceback (most recent call last):
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 91, in <module>
    start()
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 69, in start
    categorywise_df = ((df.groupby(['category', 'item_id'])).first()).tolist()
  File "C:\Users\Inderdev kumar\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'tolist'
>>> 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
[['Patriot Games', 15.95], ['Origin', 19.95], ['Animal Farm', 9.97], ['Grant', 22.5], ['Prairie Fires', 18.95], ['Future Shock', 8.95], ['Armani Suit', 800.0], ['Pants', 39.95], ['Vasque Hiking Boots', 109.0], ['Wool Hat', 14.0], ['Wrangler Jeans', 24.5], ['Nike T-shirt', 19.0], ['Gore-Tex Gloves', 39.0], ['North Face Fleece Jacket', 89.95], ['Nationals Logo Sweatshirt', 49.0], ['New Balance Trail Runners', 69.95], ['EyePhone 10', 795.0], ['First Alert Smoke Alarm', 29.95], ['Sony Prtable Radio', 15.0], ['HP Laptop', 350.0], ['LinkSys Router', 49.95], ['Altec Lansing Speakers', 195.95], ['LG 55 UDTV', 350.0], ['Dell All-in-One PC', 495.0], ['Brother Laser Printer', 99.0], ['Moose Drool Ale 6-pack', 9.95], ['Jumbo shrimp', 12.5], ['Fusili - 16 oz.', 2.95], ['Lamb Chops', 21.95]]
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
Empty DataFrame
Columns: []
Index: [(book, B001), (book, B002), (book, B003), (book, B004), (book, B005), (book, B006), (cloth, C001), (cloth, C002), (cloth, C003), (cloth, C004), (cloth, C005), (cloth, C006), (cloth, C007), (cloth, C008), (cloth, C009), (cloth, C010), (elect, E001), (elect, E002), (elect, E003), (elect, E004), (elect, E005), (elect, E006), (elect, E007), (elect, E008), (elect, E009), (food, F001), (food, F002), (food, F003), (food, F004)]
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
MultiIndex([( 'book', 'B001'),
            ( 'book', 'B002'),
            ( 'book', 'B003'),
            ( 'book', 'B004'),
            ( 'book', 'B005'),
            ( 'book', 'B006'),
            ('cloth', 'C001'),
            ('cloth', 'C002'),
            ('cloth', 'C003'),
            ('cloth', 'C004'),
            ('cloth', 'C005'),
            ('cloth', 'C006'),
            ('cloth', 'C007'),
            ('cloth', 'C008'),
            ('cloth', 'C009'),
            ('cloth', 'C010'),
            ('elect', 'E001'),
            ('elect', 'E002'),
            ('elect', 'E003'),
            ('elect', 'E004'),
            ('elect', 'E005'),
            ('elect', 'E006'),
            ('elect', 'E007'),
            ('elect', 'E008'),
            ('elect', 'E009'),
            ( 'food', 'F001'),
            ( 'food', 'F002'),
            ( 'food', 'F003'),
            ( 'food', 'F004')],
           names=['category', 'item_id'])
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
[('book', 'B001'), ('book', 'B002'), ('book', 'B003'), ('book', 'B004'), ('book', 'B005'), ('book', 'B006'), ('cloth', 'C001'), ('cloth', 'C002'), ('cloth', 'C003'), ('cloth', 'C004'), ('cloth', 'C005'), ('cloth', 'C006'), ('cloth', 'C007'), ('cloth', 'C008'), ('cloth', 'C009'), ('cloth', 'C010'), ('elect', 'E001'), ('elect', 'E002'), ('elect', 'E003'), ('elect', 'E004'), ('elect', 'E005'), ('elect', 'E006'), ('elect', 'E007'), ('elect', 'E008'), ('elect', 'E009'), ('food', 'F001'), ('food', 'F002'), ('food', 'F003'), ('food', 'F004')]
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
{'book': 'B006', 'cloth': 'C010', 'elect': 'E009', 'food': 'F004'}
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
{'book': 'B006', 'cloth': 'C010', 'elect': 'E009', 'food': 'F004'}
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
Traceback (most recent call last):
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 97, in <module>
    start()
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 71, in start
    category_wise_list= categorywise_df.index.values.todict()
AttributeError: 'numpy.ndarray' object has no attribute 'todict'
>>> 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
Traceback (most recent call last):
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 97, in <module>
    start()
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 71, in start
    category_wise_list= categorywise_df.index.values.todict()
AttributeError: 'numpy.ndarray' object has no attribute 'todict'
>>> 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
{'item_id': ['B001', 'B002', 'C001', 'B003', 'B004', 'E001', 'E002', 'F001', 'C002', 'B005', 'E003', 'C003', 'C004', 'F002', 'E004', 'C005', 'B005', 'F003', 'C006', 'C007', 'C008', 'C009', 'E005', 'F004', 'C010', 'E006', 'B006', 'E007', 'E008', 'E009'], 'category': ['book', 'book', 'cloth', 'book', 'book', 'elect', 'elect', 'food', 'cloth', 'book', 'elect', 'cloth', 'cloth', 'food', 'elect', 'cloth', 'book', 'food', 'cloth', 'cloth', 'cloth', 'cloth', 'elect', 'food', 'cloth', 'elect', 'book', 'elect', 'elect', 'elect']}
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
Traceback (most recent call last):
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 96, in <module>
    start()
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 72, in start
    category_wise_dict= {item[0]: [] for item in category_wise_list}
NameError: name 'category_wise_list' is not defined
>>> 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
{'book': [], 'cloth': [], 'elect': [], 'food': []}
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
Traceback (most recent call last):
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 101, in <module>
    start()
  File "F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py", line 74, in start
    if key not in category_wise_dict:
NameError: name 'key' is not defined
>>> 
 RESTART: F:\Python_Projects\course_hro_proects\python\november_2020\08_nvember\amazon_online_Shopping\utility.py 
   item_id category                description   price
0     B001     book              Patriot Games   15.95
1     B002     book                     Origin   19.95
2     C001    cloth                Armani Suit  800.00
3     B003     book                Animal Farm    9.97
4     B004     book                      Grant   22.50
5     E001    elect                EyePhone 10  795.00
6     E002    elect    First Alert Smoke Alarm   29.95
7     F001     food     Moose Drool Ale 6-pack    9.95
8     C002    cloth                      Pants   39.95
9     B005     book              Prairie Fires   18.95
10    E003    elect         Sony Prtable Radio   15.00
11    C003    cloth        Vasque Hiking Boots  109.00
12    C004    cloth                   Wool Hat   14.00
13    F002     food               Jumbo shrimp   12.50
14    E004    elect                  HP Laptop  350.00
15    C005    cloth             Wrangler Jeans   24.50
16    B005     book                    Ragtime   17.25
17    F003     food            Fusili - 16 oz.    2.95
18    C006    cloth               Nike T-shirt   19.00
19    C007    cloth            Gore-Tex Gloves   39.00
20    C008    cloth   North Face Fleece Jacket   89.95
21    C009    cloth  Nationals Logo Sweatshirt   49.00
22    E005    elect             LinkSys Router   49.95
23    F004     food                 Lamb Chops   21.95
24    C010    cloth  New Balance Trail Runners   69.95
25    E006    elect     Altec Lansing Speakers  195.95
26    B006     book               Future Shock    8.95
27    E007    elect                 LG 55 UDTV  350.00
28    E008    elect         Dell All-in-One PC  495.00
29    E009    elect      Brother Laser Printer   99.00
Welcome to shopping at Amazing
we sell items in the following categories:  [['B001', 'book', 'Patriot Games', 15.95], ['B002', 'book', 'Origin', 19.95], ['C001', 'cloth', 'Armani Suit', 800.0], ['B003', 'book', 'Animal Farm', 9.97], ['B004', 'book', 'Grant', 22.5], ['E001', 'elect', 'EyePhone 10', 795.0], ['E002', 'elect', 'First Alert Smoke Alarm', 29.95], ['F001', 'food', 'Moose Drool Ale 6-pack', 9.95], ['C002', 'cloth', 'Pants', 39.95], ['B005', 'book', 'Prairie Fires', 18.95], ['E003', 'elect', 'Sony Prtable Radio', 15.0], ['C003', 'cloth', 'Vasque Hiking Boots', 109.0], ['C004', 'cloth', 'Wool Hat', 14.0], ['F002', 'food', 'Jumbo shrimp', 12.5], ['E004', 'elect', 'HP Laptop', 350.0], ['C005', 'cloth', 'Wrangler Jeans', 24.5], ['B005', 'book', 'Ragtime', 17.25], ['F003', 'food', 'Fusili - 16 oz.', 2.95], ['C006', 'cloth', 'Nike T-shirt', 19.0], ['C007', 'cloth', 'Gore-Tex Gloves', 39.0], ['C008', 'cloth', 'North Face Fleece Jacket', 89.95], ['C009', 'cloth', 'Nationals Logo Sweatshirt', 49.0], ['E005', 'elect', 'LinkSys Router', 49.95], ['F004', 'food', 'Lamb Chops', 21.95], ['C010', 'cloth', 'New Balance Trail Runners', 69.95], ['E006', 'elect', 'Altec Lansing Speakers', 195.95], ['B006', 'book', 'Future Shock', 8.95], ['E007', 'elect', 'LG 55 UDTV', 350.0], ['E008', 'elect', 'Dell All-in-One PC', 495.0], ['E009', 'elect', 'Brother Laser Printer', 99.0]]
for ('B001', 'book')
  item_id category    description  price
0    B001     book  Patriot Games  15.95
for ('B002', 'book')
  item_id category description  price
1    B002     book      Origin  19.95
for ('B003', 'book')
  item_id category  description  price
3    B003     book  Animal Farm   9.97
for ('B004', 'book')
  item_id category description  price
4    B004     book       Grant   22.5
for ('B005', 'book')
   item_id category    description  price
9     B005     book  Prairie Fires  18.95
16    B005     book        Ragtime  17.25
for ('B006', 'book')
   item_id category   description  price
26    B006     book  Future Shock   8.95
for ('C001', 'cloth')
  item_id category  description  price
2    C001    cloth  Armani Suit  800.0
for ('C002', 'cloth')
  item_id category description  price
8    C002    cloth       Pants  39.95
for ('C003', 'cloth')
   item_id category          description  price
11    C003    cloth  Vasque Hiking Boots  109.0
for ('C004', 'cloth')
   item_id category description  price
12    C004    cloth    Wool Hat   14.0
for ('C005', 'cloth')
   item_id category     description  price
15    C005    cloth  Wrangler Jeans   24.5
for ('C006', 'cloth')
   item_id category   description  price
18    C006    cloth  Nike T-shirt   19.0
for ('C007', 'cloth')
   item_id category      description  price
19    C007    cloth  Gore-Tex Gloves   39.0
for ('C008', 'cloth')
   item_id category               description  price
20    C008    cloth  North Face Fleece Jacket  89.95
for ('C009', 'cloth')
   item_id category                description  price
21    C009    cloth  Nationals Logo Sweatshirt   49.0
for ('C010', 'cloth')
   item_id category                description  price
24    C010    cloth  New Balance Trail Runners  69.95
for ('E001', 'elect')
  item_id category  description  price
5    E001    elect  EyePhone 10  795.0
for ('E002', 'elect')
  item_id category              description  price
6    E002    elect  First Alert Smoke Alarm  29.95
for ('E003', 'elect')
   item_id category         description  price
10    E003    elect  Sony Prtable Radio   15.0
for ('E004', 'elect')
   item_id category description  price
14    E004    elect   HP Laptop  350.0
for ('E005', 'elect')
   item_id category     description  price
22    E005    elect  LinkSys Router  49.95
for ('E006', 'elect')
   item_id category             description   price
25    E006    elect  Altec Lansing Speakers  195.95
for ('E007', 'elect')
   item_id category description  price
27    E007    elect  LG 55 UDTV  350.0
for ('E008', 'elect')
   item_id category         description  price
28    E008    elect  Dell All-in-One PC  495.0
for ('E009', 'elect')
   item_id category            description  price
29    E009    elect  Brother Laser Printer   99.0
for ('F001', 'food')
  item_id category             description  price
7    F001     food  Moose Drool Ale 6-pack   9.95
for ('F002', 'food')
   item_id category   description  price
13    F002     food  Jumbo shrimp   12.5
for ('F003', 'food')
   item_id category      description  price
17    F003     food  Fusili - 16 oz.   2.95
for ('F004', 'food')
   item_id category description  price
23    F004     food  Lamb Chops  21.95
Please enter a category name or input 'checkout' to quit: 
 RESTART: F:/Python_Projects/course_hro_proects/python/november_2020/08_nvember/extreme temp increase/extreme temp increase.py 
                                                                                                            Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);NOx(GT);PT08.S3(NOx);NO2(GT);PT08.S4(NO2);PT08.S5(O3);T;RH;AH;;
10/03/2004;18.00.00;2            6;1360;150;11                 9;1046;166;1056;113;1692;1268;13 6;48 9;0                                                7578;;                                                                          
10/03/2004;19.00.00;2;1292;112;9 4;955;103;1174;92;1559;972;13 3;47                             7;0  7255;;                                                NaN                                                                          
10/03/2004;20.00.00;2            2;1402;88;9                   0;939;131;1140;114;1555;1074;11  9;54 0;0                                                7502;;                                                                          
10/03/2004;21.00.00;2            2;1376;80;9                   2;948;172;1092;122;1584;1203;11  0;60 0;0                                                7867;;                                                                          
10/03/2004;22.00.00;1            6;1272;51;6                   5;836;131;1205;116;1490;1110;11  2;59 6;0                                                7888;;                                                                          
>>> 
 RESTART: F:/Python_Projects/course_hro_proects/python/november_2020/08_nvember/extreme temp increase/extreme temp increase.py 
Traceback (most recent call last):
  File "F:/Python_Projects/course_hro_proects/python/november_2020/08_nvember/extreme temp increase/extreme temp increase.py", line 3, in <module>
    df= pd.read_csv("AirQualityUCI.xlsx")
  File "C:\Users\Inderdev kumar\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 685, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\Inderdev kumar\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 463, in _read
    data = parser.read(nrows)
  File "C:\Users\Inderdev kumar\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1154, in read
    ret = self._engine.read(nrows)
  File "C:\Users\Inderdev kumar\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 2059, in read
    data = self._reader.read(nrows)
  File "pandas\_libs\parsers.pyx", line 881, in pandas._libs.parsers.TextReader.read
  File "pandas\_libs\parsers.pyx", line 896, in pandas._libs.parsers.TextReader._read_low_memory
  File "pandas\_libs\parsers.pyx", line 950, in pandas._libs.parsers.TextReader._read_rows
  File "pandas\_libs\parsers.pyx", line 937, in pandas._libs.parsers.TextReader._tokenize_rows
  File "pandas\_libs\parsers.pyx", line 2132, in pandas._libs.parsers.raise_parser_error
pandas.errors.ParserError: Error tokenizing data. C error: Expected 1 fields in line 3, saw 2

>>> 
 RESTART: F:/Python_Projects/course_hro_proects/python/november_2020/08_nvember/extreme temp increase/extreme temp increase.py 
        Date      Time  CO(GT)  ...      T         RH        AH
0 2004-03-10  18:00:00     2.6  ...  13.60  48.875001  0.757754
1 2004-03-10  19:00:00     2.0  ...  13.30  47.700000  0.725487
2 2004-03-10  20:00:00     2.2  ...  11.90  53.975000  0.750239
3 2004-03-10  21:00:00     2.2  ...  11.00  60.000000  0.786713
4 2004-03-10  22:00:00     1.6  ...  11.15  59.575001  0.788794

[5 rows x 15 columns]
>>> 
 RESTART: F:/Python_Projects/course_hro_proects/python/november_2020/08_nvember/extreme temp increase/extreme temp increase.py 
        Date      Time      T
0 2004-03-10  18:00:00  13.60
1 2004-03-10  19:00:00  13.30
2 2004-03-10  20:00:00  11.90
3 2004-03-10  21:00:00  11.00
4 2004-03-10  22:00:00  11.15
>>> 
 RESTART: F:/Python_Projects/course_hro_proects/python/november_2020/08_nvember/extreme temp increase/extreme temp increase.py 
        Date      Time      T
0 2004-03-10  18:00:00  13.60
1 2004-03-10  19:00:00  13.30
2 2004-03-10  20:00:00  11.90
3 2004-03-10  21:00:00  11.00
4 2004-03-10  22:00:00  11.15
>>> 
 RESTART: F:/Python_Projects/course_hro_proects/python/november_2020/08_nvember/extreme temp increase/extreme temp increase.py 
         Date      Time       T
0  2004-03-10  18:00:00  13.600
1  2004-03-10  19:00:00  13.300
2  2004-03-10  20:00:00  11.900
3  2004-03-10  21:00:00  11.000
4  2004-03-10  22:00:00  11.150
5  2004-03-10  23:00:00  11.175
6  2004-03-11  00:00:00  11.325
7  2004-03-11  01:00:00  10.675
8  2004-03-11  02:00:00  10.650
9  2004-03-11  03:00:00  10.250
10 2004-03-11  04:00:00  10.075
11 2004-03-11  05:00:00  11.000
12 2004-03-11  06:00:00  10.450
13 2004-03-11  07:00:00  10.200
14 2004-03-11  08:00:00  10.750
>>> 
 RESTART: F:/Python_Projects/course_hro_proects/python/november_2020/08_nvember/extreme temp increase/change_population.py 
1. Display all states and it's data Alphabetically
2. Search for a specific state
3. Show Bar graph of top 5 states with highest population
4. Update overall population of specific state
5. Exit the program
Choose an option: 4
Enter the state you want to update the population for: 3
Enter the population you want to increase: 10
1. Display all states and it's data Alphabetically
2. Search for a specific state
3. Show Bar graph of top 5 states with highest population
4. Update overall population of specific state
5. Exit the program
Choose an option: 1
state: Alabama
Capital: Montgomery
State Flower: Camellia
population: 4908620

state: Alaska
Capital: Juneau
State Flower: Forget Me Not
population: 734002

state: Arizona
Capital: Phoenix
State Flower: Saguaro Cactus Blossom
population: 7378490

state: Arkansas
Capital: Little Rock
State Flower: Apple Blossom
population: 3039000

state: California
Capital: Sacramento
State Flower: California Poppy
population: 39937500

state: Colorado
Capital: Denver
State Flower: White and Lavender Columbine
population: 5845530

state: Connecticut
Capital: Hartford
State Flower: Mountain Laurel
population: 3563080

state: Delaware
Capital: Dover
State Flower: Peach Blossom
population: 982895

state: Florida
Capital: Tallahassee
State Flower: Orange Blossom
population: 21993000

state: Georgia
Capital: Atlanta
State Flower: Cherokee Rose
population: 10736100

state: Hawaii
Capital: Honolulu
State Flower: Hibiscus
population: 1412690

state: Idaho
Capital: Boise
State Flower: Syringa
population: 1826160

state: Illinois
Capital: Springfield
State Flower: Purple Violet
population: 12659700

state: Indiana
Capital: Indianapolis
State Flower: Peony
population: 6745350

state: Iowa
Capital: Des Moines
State Flower: Wild Prairie Rose
population: 3179850

state: Kansas
Capital: Topeka
State Flower: Sunflower
population: 2910360

state: Kentucky
Capital: Frankfort
State Flower: Goldenrod
population: 4499690

state: Louisiana
Capital: Baton Rouge
State Flower: Magnolia
population: 4645180

state: Maine
Capital: Augusta
State Flower: White Pine Cone and Tassel
population: 1345790

state: Maryland
Capital: Annapolis
State Flower: Black-Eyed Susan
population: 6083120

state: Massachusetts
Capital: Boston
State Flower: Mayflower
population: 6976600

state: Michigan
Capital: Lansing
State Flower: Apple Blossom
population: 10045000

state: Minnesota
Capital: Saint Paul
State Flower: Pink and White Lady Slipper
population: 5700670

state: Mississippi
Capital: Jackson
State Flower: Magnolia
population: 2989260

state: Missouri
Capital: Jefferson City
State Flower: White Hawthorn Blossom
population: 6169270

state: Montana
Capital: Helena
State Flower: Bitterroot
population: 1086760

state: Nebraska
Capital: Lincoln
State Flower: Goldenrod
population: 1952570

state: Nevada
Capital: Carson City
State Flower: Sagebrush
population: 3139660

state: New Hampshire
Capital: Concord
State Flower: Purple Lilac
population: 1371250

state: New Jersey
Capital: Trenton
State Flower: Violet
population: 8936570

state: New Mexico
Capital: Santa Fe
State Flower: Yucca Flower
population: 2096640

state: New York
Capital: Albany
State Flower: Rose
population: 19440500

state: North Carolina
Capital: Raleigh
State Flower: Dogwood
population: 10611900

state: Ohio
Capital: Columbus
State Flower: Scarlet Carnation
population: 11747700

state: Oklahoma
Capital: Oklahoma City
State Flower: Mistletoe
population: 3954820

state: Oregon
Capital: Salem
State Flower: Oregon Grape
population: 4301090

state: Pennsylvania
Capital: Harrisburg
State Flower: Mountain Laurel
population: 12820900

state: Rhode Island
Capital: Providence
State Flower: Violet
population: 1056160

state: South Carolina
Capital: Columbia
State Flower: Yellow Jessamine
population: 5210100

state: North Dakota
Capital: Bismarck
State Flower: Wild Prairie Rose
population: 761723

state: South Dakota
Capital: Pierre
State Flower: Pasque Flower
population: 903027

state: Tennessee
Capital: Nashville
State Flower: Iris
population: 6897580

state: Texas
Capital: Austin
State Flower: Bluebonnet
population: 29472300

state: Utah
Capital: Salt Lake City
State Flower: Sego Lily
population: 3282120

state: Tennessee
Capital: Nashville
State Flower: Iris
population: 6897580

state: Vermont
Capital: Montpelier
State Flower: Red Clover
population: 628061

state: Virginia
Capital: Richmond
State Flower: Dogwood
population: 8626210

state: Washington
Capital: Olympia
State Flower: Pink Rhododendron
population: 7797100

state: West Virginia
Capital: Charleston
State Flower: Rhododendron
population: 1778070

state: Wisconsin
Capital: Madison
State Flower: Wood Violet
population: 5851750

state: Wyoming
Capital: Cheyenne
State Flower: Indian Paintbrush
population: 567025

1. Display all states and it's data Alphabetically
2. Search for a specific state
3. Show Bar graph of top 5 states with highest population
4. Update overall population of specific state
5. Exit the program
Choose an option: 2
Enter the state you want to search: Wyoming
state: Wyoming
Capital: Cheyenne
State Flower: Indian Paintbrush
population: 567025

1. Display all states and it's data Alphabetically
2. Search for a specific state
3. Show Bar graph of top 5 states with highest population
4. Update overall population of specific state
5. Exit the program
Choose an option: 3
1. Display all states and it's data Alphabetically
2. Search for a specific state
3. Show Bar graph of top 5 states with highest population
4. Update overall population of specific state
5. Exit the program
Choose an option: 4
Enter the state you want to update the population for: Wyoming
Enter the population you want to increase: 10
1. Display all states and it's data Alphabetically
2. Search for a specific state
3. Show Bar graph of top 5 states with highest population
4. Update overall population of specific state
5. Exit the program
Choose an option: 2
Enter the state you want to search: Wyoming
state: Wyoming
Capital: Cheyenne
State Flower: Indian Paintbrush
population: 567035

1. Display all states and it's data Alphabetically
2. Search for a specific state
3. Show Bar graph of top 5 states with highest population
4. Update overall population of specific state
5. Exit the program
Choose an option: 5
Thanks for using the program
>>> 
 RESTART: F:/Python_Projects/course_hro_proects/python/november_2020/08_nvember/extreme temp increase/change_population.py 
1. Display all states and it's data Alphabetically
2. Search for a specific state
3. Show Bar graph of top 5 states with highest population
4. Update overall population of specific state
5. Exit the program
Choose an option: 3
1. Display all states and it's data Alphabetically
2. Search for a specific state
3. Show Bar graph of top 5 states with highest population
4. Update overall population of specific state
5. Exit the program
Choose an option: 4
Enter the state you want to update the population for: Wyoming
Enter the population you want to increase: 10
1. Display all states and it's data Alphabetically
2. Search for a specific state
3. Show Bar graph of top 5 states with highest population
4. Update overall population of specific state
5. Exit the program
Choose an option: 2
Enter the state you want to search: Wyoming
state: Wyoming
Capital: Cheyenne
State Flower: Indian Paintbrush
population: 567035

1. Display all states and it's data Alphabetically
2. Search for a specific state
3. Show Bar graph of top 5 states with highest population
4. Update overall population of specific state
5. Exit the program
Choose an option: 3
