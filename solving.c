#include <stdio.h>
#include <string.h>

#define MAX_BOOKS 100
#define MAX_MEMBERS 100

// Structure for Book
struct Book {
    int id;
    char title[100];
    char author[100];
};

// Structure for Member
struct Member {
    int id;
    char name[100];
};

// Global arrays to hold books and members
struct Book books[MAX_BOOKS];
struct Member members[MAX_MEMBERS];
int bookCount = 0;
int memberCount = 0;

// Function to add a book
void addBook() {
    if (bookCount < MAX_BOOKS) {
        printf("Enter Book ID: ");
        scanf("%d", &books[bookCount].id);
        printf("Enter Book Title: ");
        getchar();  // Clear the newline character
        fgets(books[bookCount].title, sizeof(books[bookCount].title), stdin);
        books[bookCount].title[strcspn(books[bookCount].title, "\n")] = 0;  // Remove newline
        printf("Enter Author Name: ");
        fgets(books[bookCount].author, sizeof(books[bookCount].author), stdin);
        books[bookCount].author[strcspn(books[bookCount].author, "\n")] = 0;  // Remove newline
        bookCount++;
        printf("Book added successfully!\n");
    } else {
        printf("Library is full, cannot add more books.\n");
    }
}

// Function to display all books
void displayBooks() {
    if (bookCount == 0) {
        printf("No books available.\n");
    } else {
        printf("\nBooks in Library:\n");
        for (int i = 0; i < bookCount; i++) {
            printf("ID: %d, Title: %s, Author: %s\n", books[i].id, books[i].title, books[i].author);
        }
    }
}

// Function to add a member
void addMember() {
    if (memberCount < MAX_MEMBERS) {
        printf("Enter Member ID: ");
        scanf("%d", &members[memberCount].id);
        printf("Enter Member Name: ");
        getchar();  // Clear the newline character
        fgets(members[memberCount].name, sizeof(members[memberCount].name), stdin);
        members[memberCount].name[strcspn(members[memberCount].name, "\n")] = 0;  // Remove newline
        memberCount++;
        printf("Member added successfully!\n");
    } else {
        printf("Member list is full, cannot add more members.\n");
    }
}

// Function to display all members
void displayMembers() {
    if (memberCount == 0) {
        printf("No members available.\n");
    } else {
        printf("\nMembers in Library:\n");
        for (int i = 0; i < memberCount; i++) {
            printf("ID: %d, Name: %s\n", members[i].id, members[i].name);
        }
    }
}

// Main function
int main() {
    int choice;

    do {
        printf("\nLibrary Management System\n");
        printf("1. Add Book\n");
        printf("2. Display Books\n");
        printf("3. Add Member\n");
        printf("4. Display Members\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addBook();
                break;
            case 2:
                displayBooks();
                break;
            case 3:
                addMember();
                break;
            case 4:
                displayMembers();
                break;
            case 5:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    } while (choice != 5);

    return 0;
}
