import pandas as pd

# Load the data
file_path = './data/listings.csv'
data = pd.read_csv(file_path)


data = data.drop('listing_url', axis=1)
data = data.drop('scrape_id', axis=1)
data = data.drop('last_scraped', axis=1)
data = data.drop('source', axis=1)
data = data.drop('description', axis=1)
data = data.drop('neighborhood_overview', axis=1)
data = data.drop('picture_url', axis=1)
data = data.drop('host_url', axis=1)
data = data.drop('host_since', axis=1)
#data = data.drop('host_location', axis=1)
data = data.drop('host_about', axis=1)
data = data.drop('host_response_time', axis=1)
data = data.drop('host_response_rate', axis=1)
data = data.drop('host_acceptance_rate', axis=1)
data = data.drop('host_thumbnail_url', axis=1)
data = data.drop('host_picture_url', axis=1)
data = data.drop('host_neighbourhood', axis=1)
data = data.drop('host_listings_count', axis=1)
data = data.drop('host_total_listings_count', axis=1)
data = data.drop('host_verifications', axis=1)
data = data.drop('host_has_profile_pic', axis=1)
data = data.drop('host_identity_verified', axis=1)
data = data.drop('bathrooms', axis=1)
#"price"统一成去掉“$“和”，“的srting类型
# ... [previous code] ...

# "price"统一成去掉“$“和”，“的string类型
try:
    data['price'] = data['price'].str.replace('$', '', regex=False)
    data['price'] = data['price'].str.replace(',', '', regex=False)
    data['price'] = data['price'].astype(float)
except ValueError as e:
    print(f"Error converting price to float: {e}")

# ... [remaining code] ...


data = data.drop('calendar_updated', axis=1)
data = data.drop('calendar_last_scraped', axis=1)
data = data.drop('first_review', axis=1)
data = data.drop('last_review', axis=1)
data = data.drop('license', axis=1)
data = data.drop('calculated_host_listings_count', axis=1)
data = data.drop('calculated_host_listings_count_entire_homes', axis=1)
data = data.drop('calculated_host_listings_count_private_rooms', axis=1)
data = data.drop('calculated_host_listings_count_shared_rooms', axis=1)

#处理缺失值 如果剩下的列中有缺失值，就删除该行
data = data.dropna(axis=0, how='any')
#save the data into a new csv file
data.to_csv('./data/listings_clean.csv', index=False)