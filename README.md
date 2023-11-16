# Data Set Details
The origin of my data is [AirBnB of New York City, New York, United States](http://data.insideairbnb.com/united-states/ny/new-york-city/2023-10-01/data/listings.csv.gz)
And I gunzip it to get the file [listings.csv](./data/listings.csv).
The original data is in CSV format and the first 20 rows look like the following:
| id | listing_url | scrape_id | last_scraped | source | name | description | neighborhood_overview | picture_url | host_id | host_url | host_name | host_since | host_location | host_about | host_response_time | host_response_rate | host_acceptance_rate | host_is_superhost | host_thumbnail_url | host_picture_url | host_neighbourhood | host_listings_count | host_total_listings_count | host_verifications | host_has_profile_pic | host_identity_verified | neighbourhood | neighbourhood_cleansed | neighbourhood_group_cleansed | latitude | longitude | property_type | room_type | accommodates | bathrooms | bathrooms_text | bedrooms | beds | amenities | price | minimum_nights | maximum_nights | minimum_minimum_nights | maximum_minimum_nights | minimum_maximum_nights | maximum_maximum_nights | minimum_nights_avg_ntm | maximum_nights_avg_ntm | calendar_updated | has_availability | availability_30 | availability_60 | availability_90 | availability_365 | calendar_last_scraped | number_of_reviews | number_of_reviews_ltm | number_of_reviews_l30d | first_review | last_review | review_scores_rating | review_scores_accuracy | review_scores_cleanliness | review_scores_checkin | review_scores_communication | review_scores_location | review_scores_value | license | instant_bookable | calculated_host_listings_count | calculated_host_listings_count_entire_homes | calculated_host_listings_count_private_rooms | calculated_host_listings_count_shared_rooms | reviews_per_month |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9630344 | https://www.airbnb.com/rooms/9630344 | 20231001204715 | 2023-10-02 | city scrape | Rental unit in Brooklyn  · ★4.80 · 1 bedroom · 1 b | Enjoy your own private bedroom in our 2 bedroom lu | Easy access to subway. Trendy and yet quiet. | https://a0.muscache.com/pictures/496cf3f1-7d0d-4c7 | 47783628 | https://www.airbnb.com/users/show/47783628 | Tiffannie | 2015-10-30 | New York, NY |  | N/A | N/A | N/A | f | https://a0.muscache.com/im/pictures/user/5c087186- | https://a0.muscache.com/im/pictures/user/5c087186- |  | 1 | 2 | ['email', 'phone'] | t | f | Brooklyn , New York, United States | Bushwick | Brooklyn | 40.68457 | -73.91181 | Private room in rental unit | Private room | 1 |  | 1 shared bath |  | 1 | ["Body soap", "Dryer", "Refrigerator", "Wifi", "Di | $65.00 | 30 | 30 | 30 | 30 | 30 | 30 | 30.0 | 30.0 |  | t | 29 | 59 | 89 | 364 | 2023-10-02 | 5 | 0 | 0 | 2016-08-14 | 2018-04-30 | 4.8 | 4.6 | 5.0 | 5.0 | 5.0 | 4.8 | 5.0 |  | f | 1 | 0 | 1 | 0 | 0.06 |
| 3533741 | https://www.airbnb.com/rooms/3533741 | 20231001204715 | 2023-10-02 | previous scrape | Rental unit in New York · 1 bedroom · 1 bed · 1 ba | Come stay in the heart of historic Hells Kitchen i |  | https://a0.muscache.com/pictures/45157664/862abe46 | 17791294 | https://www.airbnb.com/users/show/17791294 | Taylor | 2014-07-07 | New York, NY |  | N/A | N/A | N/A | f | https://a0.muscache.com/im/pictures/user/e204b885- | https://a0.muscache.com/im/pictures/user/e204b885- | Hell's Kitchen | 1 | 1 | ['email', 'phone'] | t | t |  | Hell's Kitchen | Manhattan | 40.76878 | -73.98719 | Private room in rental unit | Private room | 2 |  | 1 bath | 1 | 1 | ["Smoke alarm", "Kitchen", "Air conditioning", "Ca | $110.00 | 30 | 1125 | 30 | 30 | 1125 | 1125 | 30.0 | 1125.0 |  | f | 0 | 0 | 0 | 0 | 2023-10-02 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  | f | 1 | 0 | 1 | 0 |  |
| 9731039 | https://www.airbnb.com/rooms/9731039 | 20231001204715 | 2023-10-02 | previous scrape | Rental unit in Queens · Studio · 1 bed · 1 bath | Studio Apartment in the heart of Sunnyside: off th |  | https://a0.muscache.com/pictures/81a96b92-d357-4da | 50213378 | https://www.airbnb.com/users/show/50213378 | Mark | 2015-11-30 | New York, NY |  | N/A | N/A | N/A | f | https://a0.muscache.com/im/pictures/user/65d7785a- | https://a0.muscache.com/im/pictures/user/65d7785a- | Sunnyside | 1 | 1 | ['email', 'phone'] | t | f |  | Sunnyside | Queens | 40.74343 | -73.91865 | Entire rental unit | Entire home/apt | 1 |  | 1 bath |  | 1 | ["Smoke alarm", "Kitchen", "Washer", "TV", "Air co | $99.00 | 30 | 1125 | 30 | 30 | 1125 | 1125 | 30.0 | 1125.0 |  | t | 0 | 0 | 0 | 0 | 2023-10-02 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  | f | 1 | 1 | 0 | 0 |  |
| 21736164 | https://www.airbnb.com/rooms/21736164 | 20231001204715 | 2023-10-02 | previous scrape | Rental unit in Brooklyn · 1 bedroom · 1 bed · 1 ba | Light-filled, high-ceilinged 1BR brownstone apartm | The neighborhood is vibrant, multicultural, and fr | https://a0.muscache.com/pictures/4e3ee5e2-baa1-469 | 4298654 | https://www.airbnb.com/users/show/4298654 | Sam | 2012-12-01 | New York, NY | Lawyer / musician / appreciator of native ferns. | N/A | N/A | N/A | f | https://a0.muscache.com/im/users/4298654/profile_p | https://a0.muscache.com/im/users/4298654/profile_p | Bedford-Stuyvesant | 1 | 2 | ['email', 'phone', 'work_email'] | t | t | Brooklyn, New York, United States | Bedford-Stuyvesant | Brooklyn | 40.6818 | -73.93121 | Entire rental unit | Entire home/apt | 2 |  | 1 bath | 1 | 1 | ["Smoke alarm", "Kitchen", "Shampoo", "Long term s | $70.00 | 45 | 1125 | 45 | 45 | 1125 | 1125 | 45.0 | 1125.0 |  | t | 0 | 0 | 0 | 0 | 2023-10-02 | 2 | 0 | 0 | 2018-01-07 | 2019-01-20 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 |  | f | 1 | 1 | 0 | 0 | 0.03 |
| 22280002 | https://www.airbnb.com/rooms/22280002 | 20231001204715 | 2023-10-01 | city scrape | Rental unit in Brooklyn · ★4.98 · 1 bedroom · 2 be | This is a comfortable super spacious sunny 1 bedro | Welcome to the enchanting neighborhood of Stuyvesa | https://a0.muscache.com/pictures/b187bce7-ded7-447 | 67373899 | https://www.airbnb.com/users/show/67373899 | Will | 2016-04-15 | New York, NY | Globetrotter. | N/A | N/A | 100% | t | https://a0.muscache.com/im/pictures/user/41ec96fc- | https://a0.muscache.com/im/pictures/user/41ec96fc- | Bedford-Stuyvesant | 1 | 1 | ['email', 'phone'] | t | t | Brooklyn, New York, United States | Bedford-Stuyvesant | Brooklyn | 40.68209 | -73.94279 | Entire rental unit | Entire home/apt | 4 |  | 1 bath | 1 | 2 | ["Clothing storage: closet and dresser", "Microwav | $170.00 | 30 | 180 | 30 | 30 | 1125 | 1125 | 30.0 | 1125.0 |  | t | 3 | 20 | 35 | 96 | 2023-10-01 | 88 | 14 | 0 | 2017-12-30 | 2023-06-20 | 4.98 | 5.0 | 4.99 | 4.95 | 4.91 | 4.94 | 4.92 |  | f | 1 | 1 | 0 | 0 | 1.26 |
| 53903662 | https://www.airbnb.com/rooms/53903662 | 20231001204715 | 2023-10-02 | city scrape | Condo in New York · ★4.43 · 1 bedroom · 1 bed · 1  | This room is in a full floor, 4 bedroom apartment. | The East Village is located in Downtown Manhattan  | https://a0.muscache.com/pictures/61ebc358-7be7-46d | 74338125 | https://www.airbnb.com/users/show/74338125 | Alex | 2016-05-27 | New York, NY |  | within an hour | 100% | 99% | f | https://a0.muscache.com/im/pictures/user/a7674deb- | https://a0.muscache.com/im/pictures/user/a7674deb- |  | 2 | 9 | ['email', 'phone'] | t | t | New York, United States | East Village | Manhattan | 40.72625 | -73.98691 | Private room in condo | Private room | 1 |  | 1 shared bath |  | 1 | ["Microwave", "Baking sheet", "Cleaning products", | $140.00 | 1 | 28 | 1 | 1 | 28 | 28 | 1.0 | 28.0 |  | t | 12 | 38 | 68 | 343 | 2023-10-02 | 61 | 31 | 1 | 2022-01-02 | 2023-09-03 | 4.43 | 4.51 | 4.07 | 4.51 | 4.51 | 4.85 | 4.44 |  | t | 2 | 0 | 2 | 0 | 2.86 |
| 53722728 | https://www.airbnb.com/rooms/53722728 | 20231001204715 | 2023-10-02 | city scrape | Condo in New York · ★4.29 · 1 bedroom · 1 bed · 1  | This room is in a full floor, 4 bedroom apartment. | The East Village is located in Downtown Manhattan  | https://a0.muscache.com/pictures/6633c373-1642-413 | 74338125 | https://www.airbnb.com/users/show/74338125 | Alex | 2016-05-27 | New York, NY |  | within an hour | 100% | 99% | f | https://a0.muscache.com/im/pictures/user/a7674deb- | https://a0.muscache.com/im/pictures/user/a7674deb- |  | 2 | 9 | ['email', 'phone'] | t | t | New York, United States | East Village | Manhattan | 40.72813 | -73.98801 | Private room in condo | Private room | 1 |  | 1 shared bath |  | 1 | ["Microwave", "Baking sheet", "Cleaning products", | $125.00 | 1 | 28 | 1 | 1 | 28 | 28 | 1.0 | 28.0 |  | t | 5 | 31 | 58 | 333 | 2023-10-02 | 41 | 9 | 3 | 2021-12-18 | 2023-09-10 | 4.29 | 4.41 | 4.1 | 4.41 | 4.41 | 4.8 | 4.15 |  | f | 2 | 0 | 2 | 0 | 1.88 |
| 41803993 | https://www.airbnb.com/rooms/41803993 | 20231001204715 | 2023-10-02 | previous scrape | Rental unit in Queens · ★5.0 · 1 bedroom · 1 bed · | This is a clean and very comfortable bedroom in Qu | I love living here because of the practicality of  | https://a0.muscache.com/pictures/d96aecf7-fc40-4bf | 284354626 | https://www.airbnb.com/users/show/284354626 | Nelissa | 2019-08-09 | New York, United States | A very respectful person, who loves to know differ | N/A | N/A | N/A | f | https://a0.muscache.com/im/pictures/user/a2291363- | https://a0.muscache.com/im/pictures/user/a2291363- | Corona | 1 | 2 | ['email', 'phone'] | t | f | Queens, New York, United States | Jackson Heights | Queens | 40.75413 | -73.86037 | Private room in rental unit | Private room | 2 |  | 1 shared bath |  | 1 | ["Refrigerator", "Wifi", "Dishes and silverware",  | $43.00 | 30 | 1125 | 30 | 30 | 1125 | 1125 | 30.0 | 1125.0 |  | f | 0 | 0 | 0 | 0 | 2023-10-02 | 3 | 0 | 0 | 2020-02-17 | 2020-03-09 | 5.0 | 4.67 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 |  | f | 1 | 0 | 1 | 0 | 0.07 |
| 3539618 | https://www.airbnb.com/rooms/3539618 | 20231001204715 | 2023-10-02 | previous scrape | Rental unit in New York · ★4.67 · Studio · 1 bed · | This is a large alcove studio in a new building. I |  | https://a0.muscache.com/pictures/44646761/af5ffcf2 | 506909 | https://www.airbnb.com/users/show/506909 | Nevena | 2011-04-13 | New York, NY |  | N/A | N/A | N/A | f | https://a0.muscache.com/im/users/506909/profile_pi | https://a0.muscache.com/im/users/506909/profile_pi | Kips Bay | 1 | 2 | ['email', 'phone'] | t | t |  | Kips Bay | Manhattan | 40.73779 | -73.98032 | Entire rental unit | Entire home/apt | 2 |  | 1 bath |  | 1 | ["Smoke alarm", "Kitchen", "Washer", "Essentials", | $170.00 | 30 | 1125 | 30 | 30 | 1125 | 1125 | 30.0 | 1125.0 |  | t | 0 | 0 | 0 | 0 | 2023-10-02 | 9 | 0 | 0 | 2014-08-07 | 2015-05-21 | 4.67 | 4.56 | 4.78 | 4.89 | 4.78 | 4.67 | 4.88 |  | f | 1 | 1 | 0 | 0 | 0.08 |
| 9710620 | https://www.airbnb.com/rooms/9710620 | 20231001204715 | 2023-10-02 | previous scrape | Rental unit in Brooklyn · ★5.0 · 1 bedroom · 2 bed | If you request a stay, please send an intro with w | Vibrant part of Crown Heights, steps to all the ca | https://a0.muscache.com/pictures/miso/Hosting-9710 | 7027191 | https://www.airbnb.com/users/show/7027191 | Matthew | 2013-06-20 | New York, NY | Freelance filmmaker living in Brooklyn, originally | N/A | N/A | 0% | f | https://a0.muscache.com/im/pictures/user/34245133- | https://a0.muscache.com/im/pictures/user/34245133- | Crown Heights | 1 | 1 | ['email', 'phone'] | t | f | Brooklyn, New York, United States | Crown Heights | Brooklyn | 40.67742 | -73.94956 | Entire rental unit | Entire home/apt | 2 |  | 1 bath | 1 | 2 | ["Clothing storage: closet and dresser", "Baking s | $72.00 | 30 | 90 | 30 | 30 | 90 | 90 | 30.0 | 90.0 |  | t | 0 | 0 | 0 | 0 | 2023-10-02 | 6 | 0 | 0 | 2016-01-05 | 2022-04-02 | 5.0 | 5.0 | 4.83 | 5.0 | 5.0 | 5.0 | 5.0 |  | f | 1 | 1 | 0 | 0 | 0.06 |
| 675959117355164668 | https://www.airbnb.com/rooms/675959117355164668 | 20231001204715 | 2023-10-02 | city scrape | Rental unit in New York · 1 bedroom · 1 bed · 1 pr | Enjoy convenience in this centrally-located Hell’s | Convenient and filled with food options and colorf | https://a0.muscache.com/pictures/d969a120-e590-478 | 1863597 | https://www.airbnb.com/users/show/1863597 | Nicole | 2012-03-05 | New York, NY | i am responsible and level headed | within a day | 75% | 0% | f | https://a0.muscache.com/im/users/1863597/profile_p | https://a0.muscache.com/im/users/1863597/profile_p |  | 1 | 5 | ['email', 'phone'] | t | t | New York, United States | Hell's Kitchen | Manhattan | 40.76539 | -73.98681 | Private room in rental unit | Private room | 1 |  | 1 private bath |  | 1 | ["Smoke alarm", "Kitchen", "55\" HDTV", "Carbon mo | $137.00 | 30 | 365 | 30 | 30 | 365 | 365 | 30.0 | 365.0 |  | t | 21 | 32 | 62 | 152 | 2023-10-02 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  | f | 1 | 0 | 1 | 0 |  |
| 779600270049151163 | https://www.airbnb.com/rooms/779600270049151163 | 20231001204715 | 2023-10-02 | city scrape | Home in Queens · ★4.97 · 5 bedrooms · 7 beds · 1 b | Kick back and relax in this calm, stylish space. F | Bayside, Queens is a beautiful and peaceful neighb | https://a0.muscache.com/pictures/miso/Hosting-7796 | 49654304 | https://www.airbnb.com/users/show/49654304 | Seth | 2015-11-22 | New York, NY |  | within an hour | 100% | 95% | t | https://a0.muscache.com/im/pictures/user/f2e02949- | https://a0.muscache.com/im/pictures/user/f2e02949- | Flushing | 1 | 1 | ['email', 'phone'] | t | t | Queens, New York, United States | Bayside | Queens | 40.76529849242509 | -73.76707003373029 | Entire home | Entire home/apt | 10 |  | 1 bath | 5 | 7 | ["Microwave", "Baking sheet", "Self check-in", "Cl | $400.00 | 30 | 365 | 30 | 30 | 365 | 365 | 30.0 | 365.0 |  | t | 30 | 30 | 60 | 60 | 2023-10-02 | 36 | 36 | 1 | 2023-02-19 | 2023-09-04 | 4.97 | 4.94 | 4.94 | 4.97 | 5.0 | 4.97 | 4.86 |  | f | 1 | 1 | 0 | 0 | 4.78 |
| 35430378 | https://www.airbnb.com/rooms/35430378 | 20231001204715 | 2023-10-02 | city scrape | Home in Laurelton , Queens  · ★4.70 · 1 bedroom ·  | Convenient, quiet ,sparkling clean and relaxing  r | Quiet residential neighborhood  with tree lined St | https://a0.muscache.com/pictures/d680bb80-412f-4ca | 266645207 | https://www.airbnb.com/users/show/266645207 | Michael And Carrol | 2019-06-05 |  | We are fun loving family  who love hosting people  | within an hour | 90% | 96% | f | https://a0.muscache.com/im/pictures/user/User-2666 | https://a0.muscache.com/im/pictures/user/User-2666 | Jamaica | 2 | 5 | ['email', 'phone'] | t | f | Laurelton , Queens , New York, United States | Springfield Gardens | Queens | 40.66262 | -73.7488 | Private room in home | Private room | 1 |  | 1 shared bath |  | 1 | ["Clothing storage: closet and dresser", "Microwav | $75.00 | 30 | 30 | 30 | 30 | 1125 | 1125 | 30.0 | 1125.0 |  | t | 30 | 60 | 89 | 364 | 2023-10-02 | 63 | 28 | 1 | 2019-07-18 | 2023-09-03 | 4.7 | 4.76 | 4.83 | 4.73 | 4.71 | 4.75 | 4.68 |  | f | 2 | 0 | 2 | 0 | 1.23 |
| 36426788 | https://www.airbnb.com/rooms/36426788 | 20231001204715 | 2023-10-02 | city scrape | Home in Laurelton  · ★4.40 · 1 bedroom · 1 bed · 1 | Comfy, cozy, relaxing room located on the second f | Quiet neighborhood located in  Beautiful Laurelton | https://a0.muscache.com/pictures/f9fcdb1f-6ab2-42d | 266645207 | https://www.airbnb.com/users/show/266645207 | Michael And Carrol | 2019-06-05 |  | We are fun loving family  who love hosting people  | within an hour | 90% | 96% | f | https://a0.muscache.com/im/pictures/user/User-2666 | https://a0.muscache.com/im/pictures/user/User-2666 | Jamaica | 2 | 5 | ['email', 'phone'] | t | f | Laurelton , New York, United States | Laurelton | Queens | 40.67025 | -73.74414 | Private room in home | Private room | 1 |  | 1 shared bath |  | 1 | ["Clothing storage: closet and dresser", "Microwav | $74.00 | 30 | 30 | 30 | 30 | 1125 | 1125 | 30.0 | 1125.0 |  | t | 30 | 60 | 90 | 365 | 2023-10-02 | 45 | 13 | 2 | 2019-08-04 | 2023-09-03 | 4.4 | 4.36 | 4.64 | 4.36 | 4.47 | 4.42 | 4.33 |  | f | 2 | 0 | 2 | 0 | 0.89 |
| 793641370570289731 | https://www.airbnb.com/rooms/793641370570289731 | 20231001204715 | 2023-10-01 | city scrape | Rental unit in Brooklyn · 1 bedroom · 1 bed · 1 ba | Welcome to Hotel Indigo Williamsburg  <br />Among  | ▶What's nearby <br />• In Williamsburg <br />• Bro | https://a0.muscache.com/pictures/prohost-api/Hosti | 442517492 | https://www.airbnb.com/users/show/442517492 | Hotel Indigo Williamsburg | 2022-01-28 | Waynesville, NC |  | within an hour | 100% | 99% | f | https://a0.muscache.com/im/pictures/user/1cc91a56- | https://a0.muscache.com/im/pictures/user/1cc91a56- | Williamsburg | 3 | 8 | ['phone'] | t | t | Brooklyn, New York, United States | Williamsburg | Brooklyn | 40.714463632200534 | -73.9513380099022 | Entire rental unit | Entire home/apt | 2 |  | 1 bath | 1 | 1 | ["Pool", "Body soap", "Refrigerator", "Wifi", "Gym | $833.00 | 1 | 365 | 1 | 1 | 365 | 365 | 1.0 | 365.0 |  | t | 28 | 28 | 31 | 288 | 2023-10-01 | 1 | 1 | 0 | 2023-05-20 | 2023-05-20 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | Exempt | t | 3 | 3 | 0 | 0 | 0.22 |
| 791933017132228878 | https://www.airbnb.com/rooms/791933017132228878 | 20231001204715 | 2023-10-01 | city scrape | Rental unit in Brooklyn · ★4.67 · 1 bedroom · 2 be | Welcome to Hotel Indigo Williamsburg LLC <br />Amo | ▶What's nearby <br />• In Williamsburg <br />• Bro | https://a0.muscache.com/pictures/prohost-api/Hosti | 442517492 | https://www.airbnb.com/users/show/442517492 | Hotel Indigo Williamsburg | 2022-01-28 | Waynesville, NC |  | within an hour | 100% | 99% | f | https://a0.muscache.com/im/pictures/user/1cc91a56- | https://a0.muscache.com/im/pictures/user/1cc91a56- | Williamsburg | 3 | 8 | ['phone'] | t | t | Brooklyn, New York, United States | Williamsburg | Brooklyn | 40.713428622981766 | -73.95141847068068 | Entire rental unit | Entire home/apt | 4 |  | 1 bath | 1 | 2 | ["Pool", "Body soap", "Refrigerator", "Wifi", "Gym | $537.00 | 1 | 365 | 1 | 1 | 365 | 365 | 1.0 | 365.0 |  | t | 23 | 51 | 52 | 52 | 2023-10-01 | 12 | 12 | 4 | 2023-04-23 | 2023-09-24 | 4.67 | 4.83 | 4.92 | 4.92 | 4.92 | 4.83 | 4.33 | Exempt | t | 3 | 3 | 0 | 0 | 2.22 |
| 793638699862272241 | https://www.airbnb.com/rooms/793638699862272241 | 20231001204715 | 2023-10-01 | city scrape | Rental unit in Brooklyn · ★4.68 · 1 bedroom · 1 be | Welcome to Hotel Indigo Williamsburg LLC <br />Amo | ▶What's nearby <br />• In Williamsburg <br />• Bro | https://a0.muscache.com/pictures/prohost-api/Hosti | 442517492 | https://www.airbnb.com/users/show/442517492 | Hotel Indigo Williamsburg | 2022-01-28 | Waynesville, NC |  | within an hour | 100% | 99% | f | https://a0.muscache.com/im/pictures/user/1cc91a56- | https://a0.muscache.com/im/pictures/user/1cc91a56- | Williamsburg | 3 | 8 | ['phone'] | t | t | Brooklyn, New York, United States | Williamsburg | Brooklyn | 40.71323636227395 | -73.953068106665 | Entire rental unit | Entire home/apt | 2 |  | 1 bath | 1 | 1 | ["Pool", "Body soap", "Refrigerator", "Wifi", "Gym | $503.00 | 1 | 365 | 1 | 1 | 365 | 365 | 1.0 | 365.0 |  | t | 28 | 28 | 28 | 28 | 2023-10-01 | 22 | 22 | 0 | 2023-03-14 | 2023-08-18 | 4.68 | 4.73 | 4.91 | 4.77 | 4.73 | 4.77 | 4.55 | Exempt | t | 3 | 3 | 0 | 0 | 3.27 |
| 41802649 | https://www.airbnb.com/rooms/41802649 | 20231001204715 | 2023-10-02 | previous scrape | Rental unit in Brooklyn · ★4.86 · 1 bedroom · 1 be | Beautiful brownstone building walk up 3rd floor.<b | There is popular bagel store just half block away, | https://a0.muscache.com/pictures/09834095-0ca3-4fa | 34238426 | https://www.airbnb.com/users/show/34238426 | Chelsea | 2015-05-26 | United States | Easy going  | N/A | N/A | N/A | f | https://a0.muscache.com/im/pictures/user/a4cee03b- | https://a0.muscache.com/im/pictures/user/a4cee03b- | Clinton Hill | 1 | 8 | ['email', 'phone'] | t | t | Brooklyn, New York, United States | Clinton Hill | Brooklyn | 40.68305 | -73.96615 | Private room in rental unit | Private room | 2 |  | 1 shared bath |  | 1 | ["Microwave", "Bread maker", "Private living room" | $55.00 | 30 | 30 | 30 | 30 | 30 | 30 | 30.0 | 30.0 |  | f | 0 | 0 | 0 | 0 | 2023-10-02 | 9 | 0 | 0 | 2020-02-05 | 2020-03-10 | 4.86 | 4.86 | 4.71 | 5.0 | 5.0 | 4.86 | 4.86 |  | f | 1 | 0 | 1 | 0 | 0.20 |
| 702924842152964466 | https://www.airbnb.com/rooms/702924842152964466 | 20231001204715 | 2023-10-02 | previous scrape | Rental unit in Queens · ★4.96 · 1 bedroom · 1 bed  | Relax and enjoy this airy private bedroom in a sha | This is a wonderfully diverse area with many famil | https://a0.muscache.com/pictures/airflow/Hosting-7 | 413981013 | https://www.airbnb.com/users/show/413981013 | Caroline | 2021-07-19 | New York, NY | Hello! I'm a middle school ESL teacher in Bushwick | within an hour | 100% | 98% | t | https://a0.muscache.com/im/pictures/user/ad55a1a7- | https://a0.muscache.com/im/pictures/user/ad55a1a7- | Flushing | 1 | 1 | ['phone'] | t | t | Queens, New York, United States | Ridgewood | Queens | 40.70411 | -73.91063 | Private room in rental unit | Private room | 2 |  | 1 shared bath |  | 1 | ["Dove sensitive skin body soap", "Microwave", "Se | $95.00 | 6 | 90 | 3 | 6 | 1125 | 1125 | 6.0 | 1125.0 |  | t | 0 | 0 | 2 | 2 | 2023-10-02 | 23 | 20 | 0 | 2022-09-10 | 2023-05-23 | 4.96 | 4.96 | 5.0 | 5.0 | 4.96 | 4.83 | 5.0 |  | f | 1 | 0 | 1 | 0 | 1.78 |

## Data Scrubing 
Since the dataset is quite large, we first wrote a python program to perform a data scrubbing of the raw data, removing unnecessary columns and dealing with missing values, as shown in the [data_scrubbing](./data_scrubbing.py) file shown here. We used pandas to drop the columns that are not important to make this data more readable. For example we drop the column 'scrape_id'. The code is shown below:
```python
data = data.drop('scrape_id', axis=1)
```
And also, since the price column is a string with the sign "$" and ",", we converted it to a float and removed the dollar sign. The code is shown below:
```python
try:
    data['price'] = data['price'].str.replace('$', '', regex=False)
    data['price'] = data['price'].str.replace(',', '', regex=False)
    data['price'] = data['price'].astype(float)
except ValueError as e:
    print(f"Error converting price to float: {e}")
```
Then, we imported the cleaned data into mongodb.

# Data Analysis
## Data Analysis 1
### Question
show exactly two documents from the collection in any order
The code is shown below:
```python
db.listings.find().limit(2)
```
### Result
```bash
[
{_id: ObjectId("6551431ab37547ad9a4f3707"),
    id: 21736164,
    name: 'Rental unit in Brooklyn · 1 bedroom · 1 bed · 1 bath',
    host_id: 4298654,
    host_name: 'Sam',
    host_location: 'New York, NY',
    host_is_superhost: 'f',
    neighbourhood: 'Brooklyn, New York, United States',
    neighbourhood_cleansed: 'Bedford-Stuyvesant',
    neighbourhood_group_cleansed: 'Brooklyn',
    latitude: 40.6818,
    longitude: -73.93121,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms_text: '1 bath',
    bedrooms: 1,
    beds: 1,
    amenities: '["Smoke alarm", "Kitchen", "Shampoo", "Long term stays allowed", "Essentials", "Air conditioning", "Hangers", "Carbon monoxide alarm", "Hot water", "Wifi", "Free street parking", "Heating", "Iron", "Hair dryer"]',
    price: 70,
    minimum_nights: 45,
    maximum_nights: 1125,
    minimum_minimum_nights: 45,
    maximum_minimum_nights: 45,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 45,
    maximum_nights_avg_ntm: 1125,
    has_availability: 't',
    availability_30: 0,
    availability_60: 0,
    availability_90: 0,
    availability_365: 0,
    number_of_reviews: 2,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    review_scores_rating: 5,
    review_scores_accuracy: 5,
    review_scores_cleanliness: 5,
    review_scores_checkin: 5,
    review_scores_communication: 5,
    review_scores_location: 5,
    review_scores_value: 5,
    instant_bookable: 'f',
    reviews_per_month: 0.03
  },
  {
    _id: ObjectId("6551431ab37547ad9a4f3708"),
    id: 9710620,
    name: 'Rental unit in Brooklyn · ★5.0 · 1 bedroom · 2 beds · 1 bath',
    host_id: 7027191,
    host_name: 'Matthew',
    host_location: 'New York, NY',
    host_is_superhost: 'f',
    neighbourhood: 'Brooklyn, New York, United States',
    neighbourhood_cleansed: 'Crown Heights',
    neighbourhood_group_cleansed: 'Brooklyn',
    latitude: 40.67742,
    longitude: -73.94956,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms_text: '1 bath',
    bedrooms: 1,
    beds: 2,
    amenities: '["Clothing storage: closet and dresser", "Baking sheet", "Cleaning products", "Body soap", "Refrigerator", "Wifi", "Wine glasses", "Extra pillows and blankets", "Dishes and silverware", "Books and reading material", "Hair dryer", "Hot water kettle", "Cooking basics", "Luggage dropoff allowed", "Hangers", "Bed linens", "Free street parking", "Bathtub", "Heating", "Dedicated workspace", "Oven", "Private entrance", "Coffee maker: french press", "Dining table", "Freezer", "Paid parking off premises", "Conditioner", "Essentials", "Hot water", "Shower gel", "Laundromat nearby", "Room-darkening shades", "Kitchen", "Shampoo", "Exercise equipment", "Air conditioning", "Stove", "Iron", "Ethernet connection"]',
    price: 72,
    minimum_nights: 30,
    maximum_nights: 90,
    minimum_minimum_nights: 30,
    maximum_minimum_nights: 30,
    minimum_maximum_nights: 90,
    maximum_maximum_nights: 90,
    minimum_nights_avg_ntm: 30,
    maximum_nights_avg_ntm: 90,
    has_availability: 't',
    availability_30: 0,
    availability_60: 0,
    availability_90: 0,
    availability_365: 0,
    number_of_reviews: 6,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    review_scores_rating: 5,
    review_scores_accuracy: 5,
    review_scores_cleanliness: 4.83,
    review_scores_checkin: 5,
    review_scores_communication: 5,
    review_scores_location: 5,
    review_scores_value: 5,
    instant_bookable: 'f',
    reviews_per_month: 0.06
  }
]
```
## Data Analysis 2
### Question
show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the `pretty()` function.
The code is shown below:
```python
db.listings.find().limit(10).pretty()
```
### Result
```bash 
[
{
    _id: ObjectId("6551431ab37547ad9a4f3707"),
    id: 21736164,
    name: 'Rental unit in Brooklyn · 1 bedroom · 1 bed · 1 bath',
    host_id: 4298654,
    host_name: 'Sam',
    host_location: 'New York, NY',
    host_is_superhost: 'f',
    neighbourhood: 'Brooklyn, New York, United States',
    neighbourhood_cleansed: 'Bedford-Stuyvesant',
    neighbourhood_group_cleansed: 'Brooklyn',
    latitude: 40.6818,
    longitude: -73.93121,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms_text: '1 bath',
    bedrooms: 1,
    beds: 1,
    amenities: '["Smoke alarm", "Kitchen", "Shampoo", "Long term stays allowed", "Essentials", "Air conditioning", "Hangers", "Carbon monoxide alarm", "Hot water", "Wifi", "Free street parking", "Heating", "Iron", "Hair dryer"]',
    price: 70,
    minimum_nights: 45,
    maximum_nights: 1125,
    minimum_minimum_nights: 45,
    maximum_minimum_nights: 45,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 45,
    maximum_nights_avg_ntm: 1125,
    has_availability: 't',
    availability_30: 0,
    availability_60: 0,
    availability_90: 0,
    availability_365: 0,
    number_of_reviews: 2,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    review_scores_rating: 5,
    review_scores_accuracy: 5,
    review_scores_cleanliness: 5,
    review_scores_checkin: 5,
    review_scores_communication: 5,
    review_scores_location: 5,
    review_scores_value: 5,
    instant_bookable: 'f',
    reviews_per_month: 0.03
  },
  {
    _id: ObjectId("6551431ab37547ad9a4f3708"),
    id: 9710620,
    name: 'Rental unit in Brooklyn · ★5.0 · 1 bedroom · 2 beds · 1 bath',
    host_id: 7027191,
    host_name: 'Matthew',
    host_location: 'New York, NY',
    host_is_superhost: 'f',
    neighbourhood: 'Brooklyn, New York, United States',
    neighbourhood_cleansed: 'Crown Heights',
    neighbourhood_group_cleansed: 'Brooklyn',
    latitude: 40.67742,
    longitude: -73.94956,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms_text: '1 bath',
    bedrooms: 1,
    beds: 2,
    amenities: '["Clothing storage: closet and dresser", "Baking sheet", "Cleaning products", "Body soap", "Refrigerator", "Wifi", "Wine glasses", "Extra pillows and blankets", "Dishes and silverware", "Books and reading material", "Hair dryer", "Hot water kettle", "Cooking basics", "Luggage dropoff allowed", "Hangers", "Bed linens", "Free street parking", "Bathtub", "Heating", "Dedicated workspace", "Oven", "Private entrance", "Coffee maker: french press", "Dining table", "Freezer", "Paid parking off premises", "Conditioner", "Essentials", "Hot water", "Shower gel", "Laundromat nearby", "Room-darkening shades", "Kitchen", "Shampoo", "Exercise equipment", "Air conditioning", "Stove", "Iron", "Ethernet connection"]',
    price: 72,
    minimum_nights: 30,
    maximum_nights: 90,
    minimum_minimum_nights: 30,
    maximum_minimum_nights: 30,
    minimum_maximum_nights: 90,
    maximum_maximum_nights: 90,
    minimum_nights_avg_ntm: 30,
    maximum_nights_avg_ntm: 90,
    has_availability: 't',
    availability_30: 0,
    availability_60: 0,
    availability_90: 0,
    availability_365: 0,
    number_of_reviews: 6,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    review_scores_rating: 5,
    review_scores_accuracy: 5,
    review_scores_cleanliness: 4.83,
    review_scores_checkin: 5,
    review_scores_communication: 5,
    review_scores_location: 5,
    review_scores_value: 5,
    instant_bookable: 'f',
    reviews_per_month: 0.06
  },
  {
    _id: ObjectId("6551431ab37547ad9a4f3709"),
    id: 22280002,
    name: 'Rental unit in Brooklyn · ★4.98 · 1 bedroom · 2 beds · 1 bath',
    host_id: 67373899,
    host_name: 'Will',
    host_location: 'New York, NY',
    host_is_superhost: 't',
    neighbourhood: 'Brooklyn, New York, United States',
    neighbourhood_cleansed: 'Bedford-Stuyvesant',
    neighbourhood_group_cleansed: 'Brooklyn',
    latitude: 40.68209,
    longitude: -73.94279,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 4,
    bathrooms_text: '1 bath',
    bedrooms: 1,
    beds: 2,
    amenities: '["Clothing storage: closet and dresser", "Microwave", "Baking sheet", "Self check-in", "Refrigerator", "Wifi", "Wine glasses", "Extra pillows and blankets", "Dishes and silverware", "Hair dryer", "Hot water kettle", "Cooking basics", "Luggage dropoff allowed", "Coffee", "Hangers", "Bed linens", "Paid parking garage off premises", "Free street parking", "Heating", "Dedicated workspace", "HDTV with Roku", "Oven", "Private entrance", "Freezer", "Smoke alarm", "Mini fridge", "Conditioner", "Essentials", "Carbon monoxide alarm", "Coffee maker", "Hot water", "Free parking on premises", "Lockbox", "Laundromat nearby", "Room-darkening shades", "Toaster", "Kitchen", "Shampoo", "Long term stays allowed", "Stove", "Window AC unit", "Iron", "Shower gel"]',
    price: 170,
    minimum_nights: 30,
    maximum_nights: 180,
    minimum_minimum_nights: 30,
    maximum_minimum_nights: 30,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 30,
    maximum_nights_avg_ntm: 1125,
    has_availability: 't',
    availability_30: 3,
    availability_60: 20,
    availability_90: 35,
    availability_365: 96,
    number_of_reviews: 88,
    number_of_reviews_ltm: 14,
    number_of_reviews_l30d: 0,
    review_scores_rating: 4.98,
    review_scores_accuracy: 5,
    review_scores_cleanliness: 4.99,
    review_scores_checkin: 4.95,
    review_scores_communication: 4.91,
    review_scores_location: 4.94,
    review_scores_value: 4.92,
    instant_bookable: 'f',
    reviews_per_month: 1.26
  }
  ...
]
```
## Data Analysis 3
### Question
choose two hosts with the id 67373899 and 49654304 who are superhosts and show their names, host_is_superhost, and host_location.
The code is shown below:
```python
db.listings.find({
    "host_id": { "$in": [506779, 831185] }, 
    "host_is_superhost": "t"
}, {
    "name": 1, 
    "price": 1, 
    "neighbourhood": 1, 
    "host_name": 1, 
    "host_is_superhost": 1
})
\

```
### Result 
```bash
[
{
    _id: ObjectId("6551431ab37547ad9a4f3b01"),
    name: 'Condo in New York · ★4.95 · 2 bedrooms · 2 beds · 2 baths',
    host_name: 'Claudia',
    host_is_superhost: 't',
    neighbourhood: 'New York, United States',
    price: 495
  },
  {
    _id: ObjectId("6551431ab37547ad9a4f3b02"),
    name: 'Condo in New York · ★5.0 · 1 bedroom · 1 bed · 1 bath',
    host_name: 'Claudia',
    host_is_superhost: 't',
    neighbourhood: 'New York, United States',
    price: 350
  },
  {
    _id: ObjectId("6551431ab37547ad9a4f3f37"),
    name: 'Townhouse in Brooklyn · ★4.79 · 2 bedrooms · 3 beds · 2 baths',
    host_name: 'Andrew',
    host_is_superhost: 't',
    neighbourhood: 'Brooklyn, New York, United States',
    price: 566
  }

...
]
```
Significant differences in pricing indicate that even with similar conditions (like being a superhost and location), the valuation of different listings can vary greatly.

## Data Analysis 4
### Question
find all the unique `host_name` values
The code is shown below:
```python
db.listings.distinct("host_name")
```
###Result 
```bash
[
  '-TheQueensCornerLot', '2018Serenity',   'A',
  'A Group',             'A.',             'A.B.',
  'A.T.',                'AFI Apartments', 'AJbnb',
  'Aamer',               'Aaron',          'Abbe',
  'Abby',                'Abe',            'Abe & Gail',
  'Abeer',               'Abena',          'Abhilasha Ashiv',
  'Abigail',             'Abraham',        'Abul',
  'AcHomeAway',          'Ada',            'Adal',
  'Adam',                'Adar',           'Adashima',
  'Address In NYC',      'Ade',            'Adel & Katie',
  'Ademi',               'Adena',          'Adesh',
  'Adi',                 'Aditi',          'Aditya',
  'Admir',               'Adonna',         'Adora',
  'Adreinne',            'Adrian',         'Adriana',
  'Adrianna',            'Adrianne',       'Adrien',
  'Adrienne',            'Aeieyuwa',       'Agatha',
  'Agathe',              'Agnes',          'Agnieszka',
  'Ahmed',               'Ahshar',         'Aiala',
  'Aicha',               'Aida',           'Aidan',
  'Ailee',               'Aimee',          'Ainsley',
  'Airik',               'Aitan',          'Aj',
  'Ajala',               'Ajay',           'Akem & Terry',
  'Akene',               'Akiea',          'Akiko',
  'Akini',               'Akshay',         'Al',
  'AlFatiha',            'Ala',            'Alain',
  'Alan',                'Alana',          'Alauddin',
  'Alba',                'Albert',         'Alberto',
  'Alberto Fernando',    'Alden',          'Aldo',
  'Ale',                 'Alec',           'Alejandra',
  'Alejandro',           'Alek',           'Aleksander',
  'Aleksandra',          'Aleksej',        'Alencar',
  'Aleph',               'Alessandra',     'Alessio',
  'Alev Fanny',          'Alex',           'Alex And Dre',
  'Alex And Nika',
  ... 
]

```
Some names appear to be companies or brands (like 'Global Luxury Suites'), suggesting commercial players in the market alongside individuals. 

## Data Analysis 5
### Question
find all of the places that have more than 2 `beds` in a neighborhood of your choice and ordered by `review_scores_rating` descending. 
The code is shown below:
```python
db.listings.find(
    { "beds": { $gt: 2 }, "neighbourhood": "Brooklyn, New York, United States" }, 
    { "_id": 0, "name": 1, "beds": 1, "review_scores_rating": 1, "price": 1 }
).sort({ "review_scores_rating": -1 }).pretty()
```
### Result
```bash
[
  {
    name: 'Townhouse in Brooklyn · 4 bedrooms · 4 beds · 2.5 baths',
    beds: 4,
    price: 680,
    review_scores_rating: 5
  },
  {
    name: 'Rental unit in Brooklyn · 4 bedrooms · 6 beds · 2 baths',
    beds: 6,
    price: 185,
    review_scores_rating: 5
  },
  {
    name: 'Condo in Brooklyn · ★5.0 · 3 bedrooms · 3 beds · 2.5 baths',
    beds: 3,
    price: 336,
    review_scores_rating: 5
  }
]
```
Several listings have the highest rating (5), which might indicate well-maintained properties in that area or a tendency towards higher ratings in the scoring system. The number of beds seems to correlate with pricing, where more beds often mean higher prices.

## Data Analysis 6
### Question
show the number of listings per host
The code is shown below:
```python
db.listings.aggregate([
    { $group: { _id: "$host_name", listingCount: { $sum: 1 } } }
])
```
### Result
```bash
[
  { _id: 'Miryam', listingCount: 3 },
  { _id: 'Elien Blue', listingCount: 3 },
  { _id: 'Robin', listingCount: 3 },
  { _id: 'Central Park Apartments', listingCount: 3 },
  { _id: 'Anna And Toby', listingCount: 6 },
  { _id: 'Global Luxury Suites', listingCount: 87 },
  { _id: 'Arlo SoHo', listingCount: 30 },
  { _id: 'Stay With Vibe', listingCount: 6 },
  { _id: 'Hudson River', listingCount: 30 },
  { _id: 'Latif', listingCount: 9 },
  { _id: 'Roslyn', listingCount: 3 },
  { _id: 'Geo And Alex', listingCount: 6 },
  { _id: 'Ziporah', listingCount: 3 },
  { _id: 'Colin And Madelaine', listingCount: 3 },
  { _id: 'Say', listingCount: 3 },
  { _id: 'Ninja & Sung', listingCount: 3 },
  { _id: 'SuperhostRentals', listingCount: 3 },
  { _id: 'Nin', listingCount: 3 },
  { _id: 'Bridge', listingCount: 3 },
  { _id: 'Rove', listingCount: 60 }
]
```
Some hosts (like 'Global Luxury Suites' and 'Arlo SoHo') have a large number of listings, indicating a range from individual to commercial operators in the market.

## Data Analysis 7
### Question
find the average `review_scores_rating` per neighborhood, and only show the ones above a `95`, sorted in descending order of rating.
The code is shown below:
```python
db.listings.aggregate([
    { $group: { _id: "$neighbourhood", averageRating: { $avg: "$review_scores_rating" } } },
    { $match: { averageRating: { $gt: 4.5} } },
    { $sort: { averageRating: -1 } }
])
```
### Result
```bash
[
  { _id: 'Forest Hills, New York, United States', averageRating: 5 },
  { _id: 'Pomona, California, United States', averageRating: 5 },
  {
    _id: 'Williamsburg, Brooklyn , New York, United States',
    averageRating: 5
  }
]

```
Certain neighborhoods (like 'Forest Hills' and 'Williamsburg, Brooklyn') have very high average ratings, suggesting generally higher quality of listings in these areas. The high average ratings indicate general customer satisfaction but might also hint that the rating standards could be lenient or biased in some way.


## Extra Credit
This assignment deserves extra credit because I wrote a python program to to connect to the MongoDB database and perform the queries. The [python file](extra_credit.ipynb) is here. 

I first print the documents in the collection to see what the data looks like and make sure that the environment is set up correctly. 
The code is shown below:
```python
for doc in docs:
    print(doc)
```
Then I use the code to show the same query results as above. And the result is the same. 
You can find the result in my code so that I think I deserve the extra point. 



I completed this assignment with Haotong Wu(hw2933).
