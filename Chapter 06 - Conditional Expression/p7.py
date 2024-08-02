# Write a program to find out whether a given post is talking about “Debo” or not.

post = input("Enter your post: ")

if ("Debo".lower() in post.lower()):
    print("This post is talking about Debo")
else:
    print("This post is not talking about Debo")
