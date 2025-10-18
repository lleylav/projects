#include <stdio.h>

struct Movie {
    int movie_id;
    float rating;
    int duration;
    int release_year;
};

int main () {
    printf("==========================================\n");
    printf("== TASK 2: ==\n");
    printf("==========================================\n");

    FILE *infile;
    infile = fopen("movies.txt", "r");
    if (infile==NULL) {
        printf("Problem opening file\n");
        return 1;
    }
    char ch;
    int num_movies = 0;
    while (ch!=EOF) {
        ch = getc(infile);
        if (ch=='\n') {
            num_movies += 1;
        }
    }
    printf("Movie data loaded successfully! (%d movies)\n", num_movies);

    struct Movie movies[num_movies];

    FILE *infile1;
    infile1 = fopen("movies.txt", "r");
    if (infile1==NULL) {
        printf("Problem opening file\n");
        return 1;
    }

    for (int i=0; i<num_movies; i++) {
        fscanf(infile1, "%d %f %d %d", &movies[i].movie_id, &movies[i].rating, &movies[i].duration, &movies[i].release_year);
    }
    fclose(infile1);
    fclose(infile);
    int option;

    while (1) {
        printf("\n====Movie collection menu===\n");
        printf("1. Display all movies\n");
        printf("2. Search for a movie by ID\n");
        printf("3. Find highest and lowest rated movies\n");
        printf("4. Display total number of movies\n");
        printf("5. Display average rating\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &option);
        if (option==1) {
            printf("\nMovies in collection:\n");
            for (int i=0; i<num_movies; i++) {
                printf("ID: %d | Rating: %.1f | Duration: %d min | Year: %d\n", movies[i].movie_id, movies[i].rating, movies[i].duration, movies[i].release_year);
            }
        } else if (option==2) {
            int id;
            printf("Enter movie ID to search: ");
            scanf("%d", &id);
            if (id<=num_movies) {
                printf("Movie found:\n");
                printf("ID: %d | Rating: %.1f | Duration: %d min | Year: %d\n", movies[id-1].movie_id, movies[id-1].rating, movies[id-1].duration, movies[id-1].release_year);
            } else {
                printf("Movie with ID %d not found\n", id);
            }
        } else if (option==3) {
            int highest_id, lowest_id;
            float highest_rating = 0.0, lowest_rating = movies[0].rating;
            for (int i=0; i<num_movies; i++) {
                if (movies[i].rating>highest_rating) {
                    highest_rating = movies[i].rating;
                    highest_id = i+1;
                }
            }
            for (int i=1; i<num_movies; i++) {
                if (movies[i].rating<lowest_rating) {
                    lowest_rating = movies[i].rating;
                    lowest_id = i+1;
                }
            }
            printf("Highest rated movie: ID %d (Rating: %.1f)\n", highest_id, highest_rating);
            printf("Lowest rated movie: ID %d (Rating: %.1f)\n", lowest_id, lowest_rating);
        } else if (option==4) {
            printf("Total number of movies: %d\n", num_movies);
        } else if (option==5) {
            float sum = 0.0;
            float avg_rating;
            for (int i=0; i<num_movies; i++) {
                sum += movies[i].rating;
            }
            avg_rating = sum/num_movies;
            printf("Average rating: %.2f\n", avg_rating);
        } else if (option==6) {
            printf("Exiting program. Goodbye!\n");
            break;
        }
    }
    return 0;
}