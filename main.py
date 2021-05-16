from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

hundred_greatest_movies_endpoint = "https://www.empireonline.com/movies/features/best-movies-2/"

driver.get(hundred_greatest_movies_endpoint)
# //*[@id="__next"]/main/article/div[5]/div[2]/div[2]/h3
abc = driver.find_element_by_class_name("jsx-4245974604")
print(abc.text)
movies_list = []
for i in range(1, 150):
    if i % 3 == 0:
        i += 1
    else:
        elem = driver.find_element_by_xpath(f'//*[@id="__next"]/main/article/div[5]/div[2]/div[{i}]/h3')
        movies_list.append(elem.text)

movies = movies_list[::-1]

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

