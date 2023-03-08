import lotrsdk



def print_menu():
    print(""""Choose an option(type the number):
     1. get all movies
     2. get a specific movie
     3. get all quotes from a movie(only works with thrilogy)
""")
while True:

    print_menu()
    response = input()
    print(f"response: {response}")
    if response != '1' and response != '2' and response != '3':
        print("Please submit the number of the data that you want")
    elif response == '1':
        lotrsdk.get_movies()
    elif response == '2':
        print("Please choose the id of the movie you want the data from(Check the documentation for which id is for each movie)")
        movie_id = input()
        lotrsdk.get_one_movie(movie_id)
    elif response == '3':
        print("Please choose the id of the movie you want the quotes from(Check the documentation for which id is for each movie)")
        movie_id = input()
        lotrsdk.get_quote_fom_movie(movie_id)

